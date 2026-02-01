import json


#read Json
with open('bot-settings.json') as file:
    rules = json.load(file)["rules"]
    for rule in rules:
        regexName=rule["regex_name"]
        regexMessage=rule["regex_message"]
        botname=rule["name"]
    