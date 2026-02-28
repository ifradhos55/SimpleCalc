from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'calculator/index.html')

@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            expression = data.get('expression', '')
            
            # Remove any unwanted characters and extra whitespace
            expression = expression.replace(' ', '')
            
            # Simple validation to allow only numbers and basic operators
            # In a production environment, use a library like 'numexpr' or 'simpleeval'
            allowed_chars = set("0123456789+-*/.()")
            if not all(c in allowed_chars for c in expression):
                return JsonResponse({'result': 'Error: Invalid characters'})
                
            try:
                # Use a precision-safe way to format the result
                # Note: eval is used here for simplicity as requested, but with character filtering
                raw_result = eval(expression)
                
                # Format the result: round to 8 decimal places and remove trailing zeros
                if isinstance(raw_result, (int, float)):
                    result = format(raw_result, '.8f').rstrip('0').rstrip('.')
                    if result == '-0': result = '0'
                else:
                    result = str(raw_result)
                    
                return JsonResponse({'result': result})
            except ZeroDivisionError:
                return JsonResponse({'result': 'Error: Division by zero'})
            except Exception as e:
                return JsonResponse({'result': 'Error: Syntax error'})
        except Exception as e:
            return JsonResponse({'result': 'Error: Request processing failed'})
    return JsonResponse({'result': 'Invalid request'}, status=400)
