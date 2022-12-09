from revChatGPT.revChatGPT import Chatbot
import textwrap
from rich import print

def print_warp(instr):
    for i in textwrap.wrap(instr,width=50):
        print(i)

class NormalTeller():
    def __init__(self,config,blog):
        self.chatbot = Chatbot(config, conversation_id=None)
        self.chatbot.reset_chat()  # Forgets conversation
        self.chatbot.refresh_session()  # Uses the session_token to get a new bearer token
        self.first_interact = True
        self.blog = blog

    def reset(self):
        self.chatbot.reset_chat()
        self.first_interact = True

    def action(self,user_action):
        prompt = user_action
        resp = self.chatbot.get_chat_response(prompt)  # Sends a request to the API and returns the response by OpenAI
        self.response = resp["message"]

    def interactive(self):
        while True:
            action = input(">  ")
            self.action(action)
            print_warp(self.response)
