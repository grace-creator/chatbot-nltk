import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello, my name is Bot, nite to meet you!", "Hey there, my name is Bot, nite to meet you!"]
    ],
    [
        r"I need to place a return",
        ["I'm sorry to hear that, please provide your order number and the reason for the return and we will process it as soon as possible."]
    ],
    [
        r"I need help troubleshooting a device",
        ["Please provide the device's model number and a description of the problem and we will assist you in troubleshooting the issue."]
    ],
    [
        r"I did not receive the what I order",
        ["I apologize for the inconvenience. Please provide your order number and we will look into it and resolve the issue as soon as possible."]
    ],
    [
        r"I received the wrong part",
        ["I apologize for the mistake. Please provide your order number and the correct part number and we will ship the correct part and return the incorrect one as soon as possible."]
    ],
    [
        r"Where is my order",
        ["Please provide your order number and we will look into the status of your order and get back to you as soon as possible."]
    ],
    [
        r"quit",
        ["Bye bye take care. It was nice talking to you :) "]
    ],
    [
        r".*",
        ["Sorry, I don't understand what you're asking. Please choose from one of the following options: I need to place a return, I need help troubleshooting a device, I did not receive the what I order, I received the wrong part, Where is my order, quit"]
    ],
]

chatbot = Chat(pairs, reflections)

def converse():
    print("Welcome to our customer service chatbot, How can I help you today?")
    while True:
        input_text = input()
        response = chatbot.respond(input_text,1)
        if not response:
            response = "I do not understand, please choose from one of the following options."
        print(response[0])
        if input_text.strip() == "quit":
            break

chatbot.converse()
