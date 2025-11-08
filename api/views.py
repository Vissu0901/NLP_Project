from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .chatbot import ChatBot

# Initialize the chatbot
chatbot = ChatBot()

@api_view(['POST'])
def chat(request):
    """
    Chat endpoint that handles both general conversation and arithmetic calculations.
    Example inputs:
    - "Hello!"
    - "What can you do?"
    - "What is the sum of 5 and 3?"
    - "How are you today?"
    """
    try:
        message = request.data.get('message', '')
        if not message:
            return Response(
                {"error": "Please provide a message"},
                status=status.HTTP_400_BAD_REQUEST
            )

        response = chatbot.generate_response(message)
        return Response(response, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def api_root(request):
    return Response({
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
    })
