import pytchat
import json
import re
from win32com.client import Dispatch
import sys




if __name__ == "__main__":
    link=sys.argv[1]
    id=re.search("(?<=watch\\?v=).*",link).group()
    print("Connecting to "+link+"with id: "+id)
    speak = Dispatch("SAPI.SpVoice").Speak
    chat = pytchat.create(video_id=id)
    while chat.is_alive():
        messageFeed=json.loads(chat.get().json())
        if len(messageFeed)>0:
            authorName=re.search("(?<=@).*",(messageFeed[0]["author"]["name"])).group()
            message=messageFeed[0]["message"]
            print(authorName + " - " + message)
            speak(authorName + " .-. " + message)