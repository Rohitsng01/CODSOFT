
import datetime
import random

print("Welcome! Type something to chat with the bot. Type 'exit' to stop.")
while True:
    user = input("You: ").lower()
    if user == "exit":
        print("ChatBot: Bye!")
        break
    elif user == "hello":
        print("ChatBot: Hello! Sir How can I help you")
    elif user == "how are you?":
        print("ChatBot: I'm fine, What About you  Sir")
    elif user == "what is your name?":
        print("ChatBot: My name is ChatBot, Developed By Mr.Rohit.")
    elif user == "time":
        now = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"ChatBot: The  time is {now}")
    elif user == "date":
        today = datetime.date.today().strftime('%Y-%m-%d')
        print(f"ChatBot: Today's date is {today}")
    elif user == "joke":
        jokes = [
            "Why did Rohit take a ruler to bed? To see how long he could sleep.",
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "Rohit walked into the exam hall with sunglasses… because his future was too bright.",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the math book sad? It had too many problems.",
            "Rohit doesn’t get stuck in traffic… traffic waits for Rohit.",
            "Why did the computer go to therapy? It had too many bytes of sadness.",
            "Rohit once clicked 'I agree' without reading the terms… and nothing bad happened."
        ]
        print(f"ChatBot: {random.choice(jokes)}")
    elif user == "help":
        print("ChatBot: You can try these commands: hello, how are you?, what is your name?, time, date, joke, exit.")
    else:
        print("ChatBot: I don't understand. Try 'help' to see what I can do.")
