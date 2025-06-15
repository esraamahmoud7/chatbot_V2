from dotenv import load_dotenv
from GeminiChatbot import GeminiChatbot
from TextFormatter import TextFormatter

load_dotenv()
API_KEY = "AIzaSyCK0vyobfULK1_qSztlu_uumk6xjCnJQow"  # OR hardcode the key here for testing


def run_chat():
    print("Bot: Hello! How can I help you today on the HireNy platform?\n")
    bot = GeminiChatbot(api_key=API_KEY)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! 👋")
            break

        try:
            reply = bot.get_response(user_input)
            formatted = TextFormatter.clean(reply)
            print("Bot:", formatted)
        except Exception as e:
            print(" Error:", e)


if __name__ == "__main__":
    run_chat()
