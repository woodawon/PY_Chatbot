from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatbot") # 챗봇 객체
trainer = ListTrainer(chatbot) # 챗봇 트레이너

trainer.train([
    "Hi",
    "Welcome, friend🤗",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])

exit_conditions = (":q", "quit", "exit") # tuple
while True:
    query = input("> ")
    if query in exit_conditions: # 3개중에 하나라도 해당되면
        break
    else:
        print(f"{chatbot.get_response(query)}")

