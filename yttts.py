import pytchat
import time
import json
import re
from win32com.client import Dispatch
import sys




if __name__ == "__main__":
    
    if len(sys.argv)<1:
        sys.exit("missing link argument")
    link=sys.argv[1]
    id=re.search("(?<=watch\\?v=).*",link).group()
    print("Connecting to "+link+"with id: "+id)
    
    #todo add error handling maybe
    speak = Dispatch("SAPI.SpVoice").Speak
    
    #todo add error handling 
    chat = pytchat.create(video_id=id)
    while chat.is_alive():
        messageFeed=json.loads(chat.get().json())
        if len(messageFeed)>0:
            authorName=re.search("(?<=@).*",(messageFeed[0]["author"]["name"])).group()
            message=messageFeed[0]["message"]
            print(authorName + " - " + message)
            speak(authorName + " .-. " + message)