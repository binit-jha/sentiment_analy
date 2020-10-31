# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:38:40 2020

@author: BINIT KUMAR
"""

import speech_recognition as sr
import pyttsx3
import tkinter as tk
from textblob import TextBlob

engine = pyttsx3.init()


def check():
    
    global order
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        order=r.recognizer_google(audio,language="en-in")
        
    sen_analy()
    
def sen_analy():
    obj=TextBlob(order)
    sentiment=obj.sentiment.polarity
    
    if sentiment>0:
        
        engine.say("Your sentence is positive")
        engine.runAndWait()
        l2.configure(text="Positive\nSentence\n:)")
        
    elif sentiment==0:
        engine.say("Your sentence is Neutral")
        engine.runAndWait()
        l2.configure(text="Neutral\nSentence\n(-_-)")
        
    else:
        engine.say("Your sentence is Negative")
        engine.runAndWait()
        l2.configure(text="Negative\nSentence\n:(")
        
        
        
root=tk.Tk()
root.geometry("500x300")
root.title("BINIT")
root.configure(bg="black")
font=('verdana',15,'bold')
font2=('verdana',30,'bold')
l1=tk.Label(root,text="Click on the Button to speak", bg="black", fg="white", font=font)
l1.place(x=100,y=10)

l2=tk.Label(root,text=":)" , bg="black", fg="white", font=font2)
l2.place(x=120,y=50)
b1=tk.Button(root, text="Speak", bg="red", fg="white", command=check)
b1.place(x=50,y=220,height=50,width=400)

root.mainloop()