# SimpleCalc

SimpleCalc is a premium web based calculator application built with Django. It features a modern, glassmorphic user interface designed for both aesthetic appeal and functional clarity.

## Technology Stack

*   Backend: Django (Python)
*   Frontend: Standard HTML5, CSS3, and Vanilla JavaScript
*   Design: Glassmorphic UI with CSS backdrop filters

## Features

*   Real time calculation processing via a Django backend.
*   Secure expression evaluation with character filtering.
*   Responsive design that adjusts to different screen sizes.
*   Clean, typography focused interface using the Outfit font.

## Installation and Running Locally

To run this project on your local machine, follow these steps:

### 1. Prerequisites

Ensure you have Python 3 installed. You will also need the Django package.

```bash
pip install django
```

### 2. Setup the Database

While this project primarily uses backend logic for calculations, it is good practice to run initial migrations.

```bash
python manage.py migrate
```

### 3. Start the Server

Run the following command to start the Django development server:

```bash
python manage.py runserver
```

### 4. Access the Application

Once the server is running, open your web browser and navigate to:

`http://127.0.0.1:8000/`

## Usage

You can use the on screen buttons or your keyboard to input numerical expressions. Press the equal sign or the Enter key to see the result. If an invalid expression is entered, the calculator will provide a descriptive error message.
