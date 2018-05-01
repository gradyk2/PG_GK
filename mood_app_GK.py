# Mood changer

import pyautogui as pg
import webbrowser

#Question goes here
answer = pg.prompt(
"""
How are you feeling today?
a) Happy
b) Sad
c) Angry
d) Sick

"""


    )

if answer == "a":
    #Ali-a
    webbrowser.open("https://www.youtube.com/watch?v=q41-2-b0dz8")
if answer == "b":
    #Wii remix 
    webbrowser.open("https://www.youtube.com/watch?v=hPS6bl9QOHw")
if answer == "c":
    #Spageht Footlettuce
    webbrowser.open("https://www.youtube.com/watch?v=6nr_pSsz02o")
if answer == "d":
    #Walmart Kid
    webbrowser.open("https://www.youtube.com/watch?v=IQe7rB2sn88")
    
