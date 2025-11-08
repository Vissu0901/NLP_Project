# Chatbot API with Arithmetic Capabilities

## Overview
This API provides a conversational chatbot that can engage in general conversation and perform arithmetic operations when requested. The chatbot can recognize different types of user intents and respond appropriately, making it versatile for both casual chat and calculations.

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
    "message": "Welcome to the Chatbot API with Arithmetic Capabilities",
    "usage": {
        "endpoint": "/api/chat/",
        "method": "POST",
        "body": {
            "message": "Your message here"
        },
        "examples": [
            "Hello!",
            "What can you do?",
            "What is the sum of 5 and 3?",
            "multiply six and four",
            "How are you today?"
        ]
    }
}
```

### 2. Chat Endpoint
- **URL**: `/chat/`
- **Method**: `POST`
- **Description**: Handles both general conversation and arithmetic calculations
- **Request Body**:
```json
{
    "message": "string"
}
```

#### Example Requests

1. **Greeting**
```json
{
    "message": "Hello!"
}
```

2. **Arithmetic Query**
```json
{
    "message": "What is the sum of five and three?"
}
```

3. **Capabilities Question**
```json
{
    "message": "What can you do?"
}
```

4. **General Chat**
```json
{
    "message": "How are you today?"
}
```

#### Response Format
For Arithmetic Calculations:
```json
{
    "type": "calculation",
    "message": "I calculated that for you! The result is 8",
    "details": {
        "result": 8,
        "operation": "+",
        "numbers": [5, 3]
    }
}
```

For Chat Responses:
```json
{
    "type": "chat",
    "message": "Hello! I'm your friendly chat assistant. I can help you with calculations and chat about various topics. What's on your mind?"
}
```

For Errors:
```json
{
    "type": "error",
    "message": "Error message description"
}
```

## Supported Features

### 1. General Chat
- Greetings and farewells
- Questions about bot capabilities
- General conversation responses

### 2. Arithmetic Operations
- Addition: "sum", "add", "plus"
- Subtraction: "minus", "subtract", "difference"
- Multiplication: "multiply", "times"
- Division: "divide"

### 3. Number Format Support
- Numeric numbers (e.g., "5", "10", "100")
- Word numbers (e.g., "five", "ten", "hundred")

## Error Handling

### Common Error Cases
1. Missing Message
```json
{
    "error": "Please provide a message"
}
```

2. Calculation Errors
```json
{
    "type": "error",
    "message": "I encountered an error while calculating: Could not identify the arithmetic operation"
}
```

## Best Practices
1. Send clear, concise messages
2. For calculations, include numbers and operations in a natural sentence structure
3. Handle different response types (chat, calculation, error) appropriately
4. Implement proper error handling in your client application

## Example Code

### Python
```python
import requests

url = "https://your-domain.com/api/chat/"
headers = {
    "Content-Type": "application/json"
}
data = {
    "message": "What is the sum of five and three?"
}

response = requests.post(url, json=data, headers=headers)
result = response.json()
print(result)
```

### JavaScript
```javascript
fetch('https://your-domain.com/api/chat/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        message: 'What is the sum of five and three?'
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
