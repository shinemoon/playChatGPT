from revChatGPT.revChatGPT import Chatbot
import textwrap
from rich import print

def print_warp(instr):
    for i in textwrap.wrap(instr,width=50):
        print(i)

class BlogWriter():
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
        #if user_action[-1] != "。":
        #   user_action = user_action + "。"
        if self.first_interact:
            prompt = """现在来续写一篇散文，请尽量模仿沈从文的文风。一次只需要续写六句话。
            开头是，""" + self.blog + """ """ + user_action
            self.first_interact = False
        else:
            prompt = """继续续写，续写的时候注意节奏，续写的时候注意节奏，不要太快，一次只需要续写四到六句话，请尽量模仿沈从文的文风。
            """ + user_action
        resp = self.chatbot.get_chat_response(prompt)  # Sends a request to the API and returns the response by OpenAI
        self.response = resp["message"]

    def interactive(self):
        while True:
            action = input(">  ")
            self.action(action)
            print_warp(self.response)
