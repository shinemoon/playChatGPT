from story import StoryTeller
from blog import BlogWriter
from chatGPT import NormalTeller
from config import config
from rich import print

import sys

ctype = 'normal'
if(len(sys.argv)>1):
    ctype = sys.argv[1]

story_background = ""

if __name__ == "__main__":
        story_teller = None
        if(ctype=='blog'):
            print("现在我们的文章开始了：")
            story_teller = BlogWriter(config,story_background)
        if(ctype=='story'):
            print("现在我们的故事开始了：")
            story_teller = StoryTeller(config,story_background)
        else:
            print("现在开始提问吧：")
            story_teller = NormalTeller(config,story_background)
        story_teller.interactive()
