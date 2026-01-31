import pytchat
import time
import json
import re
from win32com.client import Dispatch
import sys


class Message ():
    def __init__(self, authorName, text):
        self.authorName=authorName
        self.text=text



def makeMessage (authorName, text):
        
    return Message(authorName,text)

def checkMessage (Message):
    #read Json

    #check Names

    if True: return
    elif False: 
        changedMessage=changeMessage(Message)
        checkMessage(changedMessage)

def changeMessage (Message, jsonObject):

    return Message




if __name__ == "__main__":
    
    if len(sys.argv)<1:
        sys.exit("Invalid Argument")
    link=sys.argv[1]
    id=re.search("(?<=watch\\?v=).*",link).group()
    print("Connecting to "+link+"with id: "+id)
    voice = Dispatch("SAPI.SpVoice")
    try:
        chat = pytchat.create(video_id=id)
    except:
        sys.exit("Invalid youtube-link")
    while chat.is_alive():
        messageFeed=json.loads(chat.get().json())
        if len(messageFeed)>0:
            authorName=re.search("(?<=@).*",(messageFeed[0]["author"]["name"])).group()
            message=messageFeed[0]["message"]
            print(authorName + " - " + message)
            voice.Speak(authorName + " .-. " + message)
            voice.speakWaitUntilDone(-1)
        else: time.sleep(5)

