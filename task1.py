"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
import tkinter as tk
from tkinter import *

entry = []
x = []

def doinYourMomYesYoursFirstSawHerAtTheWalmartPickingOutYourDrawers():
    for i in range(19):
        x.append(entry[i].get())
        entry[i].pack_forget()
    button.pack_forget()

    if x[2][0] == "a" or x[2][0] == "e" or x[2][0] == "i" or x[2][0] == "o" or x[2][0] == "u":
        a1 = "an"
    else:
        a1 = "a"
    if x[3][0] == "a" or x[3][0] == "e" or x[3][0] == "i" or x[3][0] == "o" or x[3][0] == "u":
        a2 = "an"
    else:
        a2 = "a"
    if x[11][0] == "a" or x[11][0] == "e" or x[11][0] == "i" or x[11][0] == "o" or x[11][0] == "u":
        a3 = "an"
    else:
        a3 = "a"

    label1["text"] = "A vacation is when you take a trip to some " + x[0]
    label2["text"] = "place with your " + x[1]
    label3["text"] = "family. Usually you go to some place that is near " + a1 + " " + x[2]
    label4["text"] = "or up on " + a2 + " " + x[3] + "."
    label5["text"] = "A good vacation place is one where you can ride " + x[4]
    label6["text"] = "or play " + x[5]
    label7["text"] = "or go hunting for " + x[6] + "."
    label8["text"] = "I like to spend my time " + x[7]
    label9["text"] = "or " + x[8] + "."
    label10["text"] = "When parents go on a vacation, they spend their time eating three " + x[9]
    label11["text"] = "a day, and fathers play golf, and mothers sit around " + x[10] + "."
    label12["text"] = "Last summer, my little brother fell in " + a3 + " " + x[11]
    label13["text"] = "and got poison " + x[12]
    label14["text"] = "all over his " + x[13] + "."
    label15["text"] = "My family is going to go to (the) " + x[14] + ","
    label16["text"] = "and I will practice " + x[15] + "."
    label17["text"] = "Parents need vacations more than kids because parents are always very " + x[16]
    label18["text"] = "and because they have to work " + x[17]
    label19["text"] = "hours every day all year making enough " + x[18]
    label20 = tk.Label(text = "to pay for the vacation.", font = ("Comic Sans MS", 10))
    label20.pack()

main = tk.Tk()
main.geometry("500x850")
main.title("Madlib!")

for i in range(19):
    entry.append(tk.Entry())


label1 = tk.Label(text = "Adjective", font = ("Comic Sans MS", 10))
label2 = tk.Label(text = "Adjective", font = ("Comic Sans MS", 10))
label3 = tk.Label(text = "Noun", font = ("Comic Sans MS", 10))
label4 = tk.Label(text = "Noun", font = ("Comic Sans MS", 10))
label5 = tk.Label(text = "Plural Noun", font = ("Comic Sans MS", 10))
label6 = tk.Label(text = "Game", font = ("Comic Sans MS", 10))
label7 = tk.Label(text = "Plural Noun", font = ("Comic Sans MS", 10))
label8 = tk.Label(text = "Verb ending in 'ing'", font = ("Comic Sans MS", 10))
label9 = tk.Label(text = "Verb ending in 'ing'", font = ("Comic Sans MS", 10))
label10 = tk.Label(text = "Plural Noun", font = ("Comic Sans MS", 10))
label11 = tk.Label(text = "Verb ending in 'ing'", font = ("Comic Sans MS", 10))
label12 = tk.Label(text = "Noun", font = ("Comic Sans MS", 10))
label13 = tk.Label(text = "Plant", font = ("Comic Sans MS", 10))
label14 = tk.Label(text = "Part of the body", font = ("Comic Sans MS", 10))
label15 = tk.Label(text = "A Place", font = ("Comic Sans MS", 10))
label16 = tk.Label(text = "Verb ending in 'ing'", font = ("Comic Sans MS", 10))
label17 = tk.Label(text = "Adjective", font = ("Comic Sans MS", 10))
label18 = tk.Label(text = "Number", font = ("Comic Sans MS", 10))
label19 = tk.Label(text = "Plural Noun", font = ("Comic Sans MS", 10))

button = tk.Button(text = "Go!", command = doinYourMomYesYoursFirstSawHerAtTheWalmartPickingOutYourDrawers, font = ("Comic Sans MS", 10))

label1.pack()
entry[0].pack()

label2.pack()
entry[1].pack()

label3.pack()
entry[2].pack()

label4.pack()
entry[3].pack()

label5.pack()
entry[4].pack()

label6.pack()
entry[5].pack()

label7.pack()
entry[6].pack()

label8.pack()
entry[7].pack()

label9.pack()
entry[8].pack()

label10.pack()
entry[9].pack()

label11.pack()
entry[10].pack()

label12.pack()
entry[11].pack()

label13.pack()
entry[12].pack()

label14.pack()
entry[13].pack()

label15.pack()
entry[14].pack()

label16.pack()
entry[15].pack()

label17.pack()
entry[16].pack()

label18.pack()
entry[17].pack()

label19.pack()
entry[18].pack()

button.pack()
main.mainloop()