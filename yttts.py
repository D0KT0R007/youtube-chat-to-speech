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

def changeMessage (Message, regexName, regexMessage):
    
    return Message

def checkMessage (Message):
    #read Json
    with open('bot-settings.json') as file:
        rules = json.load(file)["rules"]
        for rule in rules:
            regexName=rule["regex_name"]
            regexMessage=rule["regex_message"]
            botname=rule["name"]
            #check Names
            if Message.authorName.lower() in botname.lower():
                changedMessage=changeMessage(Message,regexName,regexMessage)
                checkMessage(changedMessage)
            else:
                return Message


def readMessage(Message):
    voice = Dispatch("SAPI.SpVoice")
    voice.Speak(authorName + " .-. " + message)
    voice.speakWaitUntilDone(-1)
    return


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
            messageObject=Message(authorName,message)
            checkMessage(messageObject)
        else: time.sleep(5)

