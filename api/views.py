from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import process_arithmetic_query

@api_view(['POST'])
def calculate(request):
    """
    Process natural language arithmetic queries.
    Example inputs:
    - "What is the sum of 5 and 3?"
    - "multiply six and four"
    - "5 plus 3"
    - "difference between ten and seven"
    """
    try:
        query = request.data.get('query', '')
        if not query:
            return Response(
                {"error": "Please provide a query"},
                status=status.HTTP_400_BAD_REQUEST
            )

        result = process_arithmetic_query(query)
        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def api_root(request):
    return Response({
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
    })
