const display = document.getElementById('display');

function appendToDisplay(value) {
    if (display.value === 'Error') {
        display.value = value;
    } else {
        display.value += value;
    }
}

function clearDisplay() {
    display.value = '';
}

async function calculate() {
    const expression = display.value;
    if (!expression) return;

    try {
        const response = await fetch('/calculate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression: expression }),
        });

        const data = await response.json();
        // If the backend returns an error message starting with 'Error:', display it
        // Otherwise, display the result.
        display.value = data.result;
    } catch (error) {
        display.value = 'Error: Connectivity';
    }
}

// Support keyboard input
document.addEventListener('keydown', (event) => {
    const key = event.key;
    const allowedKeys = '0123456789+-*/.EnterBackspaceEscape';

    if (key === 'Enter') {
        calculate();
    } else if (key === 'Backspace') {
        display.value = display.value.slice(0, -1);
    } else if (key === 'Escape') {
        clearDisplay();
    } else if ('0123456789+-*/.'.includes(key)) {
        appendToDisplay(key);
    }
});
