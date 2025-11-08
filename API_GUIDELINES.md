# NLP Arithmetic API Documentation

## Overview
This API provides natural language processing capabilities for performing arithmetic operations. Users can send queries in natural language or simple arithmetic expressions, and the API will process them to return the calculated results.

## Base URL
```
https://your-domain.com/api/
```

## Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns API information and usage guidelines
- **Response Example**:
```json
{
    "message": "Welcome to the NLP Arithmetic API",
    "usage": {
        "endpoint": "/api/calculate/",
        "method": "POST",
        "body": {
            "query": "Your arithmetic question here"
        },
        "examples": [
            "What is the sum of 5 and 3?",
            "multiply six and four",
            "5 plus 3",
            "difference between ten and seven"
        ]
    }
}
```

### 2. Calculate Endpoint
- **URL**: `/calculate/`
- **Method**: `POST`
- **Description**: Processes arithmetic queries in natural language
- **Request Body**:
```json
{
    "query": "string"
}
```

#### Example Requests

1. **Addition**
```json
{
    "query": "What is the sum of five and three?"
}
```

2. **Multiplication**
```json
{
    "query": "multiply 6 and 4"
}
```

3. **Subtraction**
```json
{
    "query": "difference between ten and seven"
}
```

4. **Division**
```json
{
    "query": "divide twenty by five"
}
```

#### Response Format
```json
{
    "result": number,
    "operation": string,
    "numbers": array
}
```

#### Example Response
```json
{
    "result": 8,
    "operation": "+",
    "numbers": [5, 3]
}
```

#### Error Response
```json
{
    "error": "Error message description"
}
```

## Supported Operations

### 1. Addition
- Keywords: "sum", "add", "plus", "addition"
- Example: "What is the sum of 5 and 3?"

### 2. Subtraction
- Keywords: "minus", "subtract", "subtraction", "difference"
- Example: "What is the difference between 10 and 7?"

### 3. Multiplication
- Keywords: "multiply", "multiplication", "times"
- Example: "multiply six and four"

### 4. Division
- Keywords: "divide", "division"
- Example: "divide twenty by five"

## Number Format Support
The API supports both:
- Numeric numbers (e.g., "5", "10", "100")
- Word numbers (e.g., "five", "ten", "hundred")

## Error Handling

### Common Error Cases
1. Missing Query
```json
{
    "error": "Please provide a query"
}
```

2. Invalid Operation
```json
{
    "error": "Could not identify the arithmetic operation"
}
```

3. Insufficient Numbers
```json
{
    "error": "Could not identify enough numbers in the query"
}
```

4. Division by Zero
```json
{
    "error": "Division by zero is not allowed"
}
```

## Rate Limiting
- Default rate limit: 100 requests per minute per IP
- Status code 429 will be returned if rate limit is exceeded

## Best Practices
1. Always send queries in a clear, concise format
2. Include numbers and operations in a natural sentence structure
3. Verify the response format and handle potential errors
4. Implement proper error handling in your client application

## Example Code

### Python
```python
import requests

url = "https://your-domain.com/api/calculate/"
headers = {
    "Content-Type": "application/json"
}
data = {
    "query": "What is the sum of five and three?"
}

response = requests.post(url, json=data, headers=headers)
result = response.json()
print(result)
```

### JavaScript
```javascript
fetch('https://your-domain.com/api/calculate/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        query: 'What is the sum of five and three?'
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

## Support
For additional support or to report issues, please contact:
- Email: support@your-domain.com
- GitHub Issues: https://github.com/your-repo/issues
