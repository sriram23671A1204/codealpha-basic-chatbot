import nltk
from nltk.chat.util import Chat, reflections

# Define a list of pattern-response pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi, how can I assist you?"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created to assist you."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No worries!", "It's okay, don't worry."]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear!", "Awesome! How can I help you?"]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you. Please tell me more."]
    ],
    [
        r"quit",
        ["Bye! Have a great day.", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase that?", "Tell me more..."]
    ],
]

# Create and start the chatbot
def start_chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    start_chatbot()
