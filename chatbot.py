import random
class CustomerEnquiryChatbot:
    def __init__(self):
        self.responses = {
            "greeting": "Hello! How can I assist you today?",
            "order_status": "Your order is currently being processed.",
            "product_info": "Our products are of high quality. What specific information are you looking for?",
            "goodbye": "Thank you for chatting with us. Have a great day!"
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        if "hello" in user_input or "hi" in user_input:
            return self.responses["greeting"]
        elif "order" in user_input and "status" in user_input:
            return self.responses["order_status"]
        elif "product" in user_input and ("info" in user_input or "information" in user_input):
            return self.responses["product_info"]
        elif "goodbye" in user_input or "bye" in user_input:
            return self.responses["goodbye"]
        else:
            return "I'm sorry, I didn't understand. Could you please rephrase your question?"

# Example usage:
chatbot = CustomerEnquiryChatbot()

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = chatbot.get_response(user_input)
    print("Chatbot:", response)
