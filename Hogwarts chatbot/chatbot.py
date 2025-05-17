import json
import threading

with open("hogwarts_data.json", "r") as f:
    data = json.load(f)

isRunning = False
persistance = False
prompt = ""
response = ""

promptEvent = threading.Event()
responseEvent = threading.Event()

def startConversation():
    global isRunning, prompt, response

    while isRunning:
        promptEvent.wait()
        promptEvent.clear()
        print("Working on prompt: " + prompt)
        response = generateResponse(prompt)
        print("Finished processing")
        responseEvent.set()
    print("Exited...")

def generateResponse(prompt):
    prompt_lower = prompt.lower()
    for entry in data:
        for keyword in entry["keywords"]:
            if keyword in prompt_lower:
                return entry["answer"]
    return "Sorry, I don't know that. Please check the official Hogwarts document."