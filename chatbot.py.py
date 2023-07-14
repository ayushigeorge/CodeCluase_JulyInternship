#!/usr/bin/env python
# coding: utf-8

# # GOLDEN TASK FOR CODECLAUSE INTERSHIP

# # CHAT BOT FOR CODECLAUSE

# In[1]:


# Import necessary libraries
import random


# In[2]:



# Define the chatbot's responses
greetings = ["Hello! Welcome to CodeClause. How can I assist you?", "Hi there! How can I help you with CodeClause today?"]

farewell = ["Thank you for reaching out to CodeClause. Have a great day!", "Goodbye! Feel free to contact us anytime."]
# Define the options and their corresponding answers as a dictionary
options = {
    "CodeClause": "CodeClause is a business startup that provides innovative solutions for companies.",
    "services": "CodeClause offers a wide range of services including software development, web design, and data analysis.",
    "contact": "You can get in touch with CodeClause by visiting our website at www.codeclause.com or emailing us at info@codeclause.com."
}

# Define the chatbot function
def chatbot():
    print("Chatbot: " + random.choice(greetings))
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: " + random.choice(farewell))
            break
        
        if user_input in options:
            print("Chatbot: " + options[user_input])
        else:
            print("Chatbot: I'm sorry, I don't have the information you're looking for. Can I help you with anything else?")

# Start the chatbot
print("!!! Welcome to CodeClause Chatbot !!!")
chatbot()


# In[ ]:




