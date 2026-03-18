import random
import time

# Krishna quotes
quotes = [
    "You have the right to perform your duty, but not to the fruits of your actions.",
    "Set your heart upon your work but never on its reward.",
    "A person can rise through the efforts of their own mind.",
    "Calmness, gentleness, silence, self-restraint are qualities of a wise person.",
    "Change is the law of the universe.",
]

# Mood keywords
moods = {
    "sad": ["sad", "depressed", "upset", "cry", "tired"],
    "stress": ["stress", "pressure", "worried", "exam"],
    "happy": ["happy", "good", "great", "excited"]
}

# Funny Krishna-style lines
fun_lines = [
    "Even Arjuna had doubts 😄 but he still fought!",
    "Maybe it's time for some chai ☕ and then back to work!",
    "Krishna believes in you 💙 do you?",
]

def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def get_mood(user):
    for mood, words in moods.items():
        if any(word in user for word in words):
            return mood
    return "neutral"

def krishna_reply(user, name):
    mood = get_mood(user)

    if mood == "sad":
        return f"{name}, why sadness? 🌸 " + random.choice(quotes)

    elif mood == "stress":
        return f"{name}, focus on your karma, not results 🌿 " + random.choice(quotes)

    elif mood == "happy":
        return f"That’s wonderful, {name}! 😊 Keep shining!"

    elif "bored" in user:
        return random.choice(fun_lines)

    elif "who are you" in user:
        return "I am Krishna AI, your friend and guide 💙"

    elif "hello" in user or "hi" in user:
        return f"Radhe Radhe {name} 💙 What’s on your mind?"

    else:
        return random.choice(quotes)


# Start chatbot
print("🌟 Krishna AI Chatbot 🌟")
name = input("Krishna AI: What is your name? ")

typing_effect(f"Radhe Radhe {name} 💙 I am here for you.")

while True:
    user = input(f"{name}: ").lower()

    if user == "exit":
        typing_effect("Krishna AI: Goodbye 🌸 Stay blessed!")
        break

    response = krishna_reply(user, name)
    typing_effect("Krishna AI: " + response)
