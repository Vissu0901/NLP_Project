import spacy
from .utils import process_arithmetic_query

nlp = spacy.load('en_core_web_sm')

class ChatBot:
    def __init__(self):
        self.arithmetic_keywords = [
            'calculate', 'sum', 'add', 'plus', 'minus', 'subtract',
            'multiply', 'divide', 'difference', 'times'
        ]

    def detect_intent(self, message):
        """Detect the intent of the user's message."""
        message = message.lower()
        doc = nlp(message)

        # Check for arithmetic intent
        if any(keyword in message for keyword in self.arithmetic_keywords):
            return 'arithmetic'

        # Check for greetings
        greetings = ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
        if any(greeting in message for greeting in greetings):
            return 'greeting'

        # Check for farewells
        farewells = ['bye', 'goodbye', 'see you', 'farewell', 'good night']
        if any(farewell in message for farewell in farewells):
            return 'farewell'

        # Check for bot capabilities question
        if 'what can you do' in message or 'help' in message:
            return 'capabilities'

        return 'general_chat'

    def generate_response(self, message):
        """Generate a response based on the user's message."""
        intent = self.detect_intent(message)

        if intent == 'arithmetic':
            try:
                result = process_arithmetic_query(message)
                if 'error' in result:
                    return {
                        'type': 'error',
                        'message': f"I encountered an error while calculating: {result['error']}"
                    }
                return {
                    'type': 'calculation',
                    'message': f"I calculated that for you! The result is {result['result']}",
                    'details': result
                }
            except Exception as e:
                return {
                    'type': 'error',
                    'message': "I'm having trouble with that calculation. Could you rephrase it?"
                }

        elif intent == 'greeting':
            return {
                'type': 'chat',
                'message': "Hello! I'm your friendly chat assistant. I can help you with calculations and chat about various topics. What's on your mind?"
            }

        elif intent == 'farewell':
            return {
                'type': 'chat',
                'message': "Goodbye! Feel free to come back if you need any help with calculations or just want to chat!"
            }

        elif intent == 'capabilities':
            return {
                'type': 'chat',
                'message': "I'm a chatbot that can help you with basic arithmetic calculations and general conversation. "
                          "For calculations, you can ask things like 'what is the sum of 5 and 3?' or 'multiply six and four'. "
                          "For other topics, I'm still learning, but I'm happy to chat!"
            }

        else:
            return {
                'type': 'chat',
                'message': "I'm still learning about different topics, but I'm great at arithmetic! "
                          "Feel free to ask me any calculation questions or just chat with me."
            }
