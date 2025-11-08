import spacy
import re
from word2number import w2n

nlp = spacy.load('en_core_web_sm')

def extract_numbers(text):
    """Extract numbers from text, handling both numeric and word forms."""
    numbers = []
    # First, try to find written numbers
    words = text.lower().split()
    current_number = []

    for word in words:
        try:
            num = w2n.word_to_num(word)
            numbers.append(num)
        except ValueError:
            continue

    # Then find numeric numbers
    numeric_numbers = re.findall(r'\d+\.?\d*', text)
    numbers.extend([float(num) for num in numeric_numbers])

    return numbers

def identify_operation(text):
    """Identify the arithmetic operation from the text."""
    text = text.lower()

    # Define operation keywords
    operations = {
        'sum': '+',
        'add': '+',
        'plus': '+',
        'addition': '+',
        'minus': '-',
        'subtract': '-',
        'subtraction': '-',
        'difference': '-',
        'multiply': '*',
        'multiplication': '*',
        'times': '*',
        'divide': '/',
        'division': '/',
    }

    # First check for direct arithmetic expressions
    if any(op in text for op in ['+', '-', '*', '/', 'x']):
        # Handle direct arithmetic expressions
        for op in ['*', '/', '+', '-']:
            if op in text:
                return op
        if 'x' in text:  # Handle 'x' as multiplication
            return '*'

    # Check for operation keywords
    doc = nlp(text)
    for token in doc:
        if token.text.lower() in operations:
            return operations[token.text.lower()]

    # Default to addition if "and" is present
    if ' and ' in text:
        return '+'

    return None

def process_arithmetic_query(text):
    """Process natural language arithmetic query and return result."""
    numbers = extract_numbers(text)
    operation = identify_operation(text)

    if not numbers or len(numbers) < 2:
        return {
            "error": "Could not identify enough numbers in the query",
            "numbers_found": numbers
        }

    if not operation:
        return {
            "error": "Could not identify the arithmetic operation",
            "numbers_found": numbers
        }

    result = numbers[0]
    for num in numbers[1:]:
        if operation == '+':
            result += num
        elif operation == '-':
            result -= num
        elif operation == '*':
            result *= num
        elif operation == '/':
            if num == 0:
                return {"error": "Division by zero is not allowed"}
            result /= num

    return {
        "result": result,
        "operation": operation,
        "numbers": numbers
    }
