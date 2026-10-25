import re

def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    
    if re.search(r'\b(hi|hello|hey|नमस्कार)\b', user_input):
        return "Hello! How can I help you today?"
    elif re.search(r'\b(how are you)\b', user_input):
        return "I'm doing great! How about you?"
    elif re.search(r'\b(name|who are you)\b', user_input):
        return "I am a simple Rule-Based AI Chatbot for your internship task."
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return "Goodbye! Have a wonderful day!"
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

def start_chat():
    print("--- Rule-Based Chatbot ---")
    print("Type 'exit' to stop.\n")
    
    while True:
        user_message = input("You: ")
        if user_message.lower() in ['exit', 'quit']:
            print("Bot: Goodbye!")
            break
        
        response = get_bot_response(user_message)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    start_chat()