import os
from dotenv import load_dotenv  # Import the dotenv package
from openai import OpenAI
import colorama
from colorama import Fore, Style

# Load environment variables from the .env file
load_dotenv()

def main():
    colorama.init(autoreset=True)
    
    # Fetch domain and API key from environment variables
    domain = os.getenv('DOMAIN')
    api_key = 'na'
    
    # Initialize the OpenAI client with the base URL of your hosted model and the API key
    client = OpenAI(base_url=f'{domain}:3000/v1', api_key=api_key)

    # Define a system message that sets the role of the AI
    system_message = {
        "role": "system",
        "content": "You are a virtual AI agent that assists users with their questions. Provide helpful, concise, and friendly answers."
    }

    # Initialize conversation history with the system message
    conversation_history = [system_message]

    while True:
        print(Fore.CYAN + "-" * 50)
        user_input = input(Fore.GREEN + "You: ")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(Fore.YELLOW + "Goodbye!")
            break

        # Append the user's message to the conversation history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Create a chat completion request with the conversation history
        response = client.chat.completions.create(
            model="hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",
            messages=conversation_history,
        )

        # Extract and print the response from the model
        answer = response.choices[0].message.content
        print(Fore.CYAN + "-" * 50)
        print(Fore.MAGENTA + "Model: " + Style.RESET_ALL + answer)
        print(Fore.CYAN + "-" * 50)

        # Append the model's response to the conversation history
        conversation_history.append({
            "role": "assistant",
            "content": answer
        })

if __name__ == "__main__":
    main()
