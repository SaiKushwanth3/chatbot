import string
import random
def greet(sentence):
    for word in sentence.split():
        if word.lower() in Greeting_input:
            return (random.choice(Greeting_response))
def chatbot_response(element):
    for word in element.split():
      for x,y in train_data.items():
          if(word.lower()== x):  
             return y
Greeting_input=("hello", "hii" , "greetings", "whatsup", "hey")
Greeting_response=["hello", "hii" , "hithere", "nod's", "hey", "i'm glad!"]

train_data={"bye": "good bye, Take care"}
chatbot_response("bye")
            
