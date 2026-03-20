import random
import time

# ===============================
# Krishna AI Chatbot 💙
# ===============================

# Quotes
quotes = [
    "You have the right to perform your duty, but not to the fruits of your actions.",
    "Set your heart upon your work but never on its reward.",
    "A person can rise through the efforts of their own mind.",
    "Calmness, gentleness, silence, self-restraint are qualities of a wise person.",
    "Change is the law of the universe."
]

# Mood keywords
moods = {
    "sad": ["sad", "depressed", "upset", "cry", "tired"],
    "stress": ["stress", "pressure", "worried", "exam"],
    "happy": ["happy", "good", "great", "excited"]
}

# Fun lines
fun_lines = [
    "Even Arjuna had doubts, but he still moved forward!",
    "Take a short break and come back stronger.",
    "Krishna believes in you. Keep going!"
]

# Typing effect
def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print()

# Detect mood
def get_mood(user):
    for mood, words in moods.items():
        for word in words:
            if word in user:
                return mood
    return "neutral"

# Generate reply
def krishna_reply(user, name):
    mood = get_mood(user)

    if mood == "sad":
        return name + ", do not be disheartened. " + random.choice(quotes)

    elif mood == "stress":
        return name + ", focus on your duty, not the results. " + random.choice(quotes)

    elif mood == "happy":
        return "That's great to hear, " + name + "! Keep smiling."

    elif "bored" in user:
        return random.choice(fun_lines)

    elif "exam" in user:
        return name + ", do your best without fear. Results will follow."

    elif "failure" in user:
        return name + ", failure is a step towards success. Learn and move forward."

    elif "motivate" in user:
        return name + ", believe in yourself. You are stronger than you think."

    elif "help" in user:
        return "You can talk about stress, sadness, exams, motivation, or just say hello!"

    elif "who are you" in user:
        return "I am Krishna AI, your guide and friend."

    elif "hello" in user or "hi" in user:
        return "Radhe Radhe " + name + "! How can I help you today?"

    else:
        return random.choice(quotes)

# ===============================
# Main Program
# ===============================

print("🌟 Welcome to Krishna AI Chatbot 🌟")
print("Type 'exit' anytime to stop")

name = input("Enter your name: ")
typing_effect("Radhe Radhe " + name + ". I am here to guide you.")

while True:
    user = input(name + ": ").lower()

    if user == "exit":
        typing_effect("Goodbye " + name + ". Stay positive and keep learning!")
        break

    response = krishna_reply(user, name)
    typing_effect("Krishna AI: " + response)
