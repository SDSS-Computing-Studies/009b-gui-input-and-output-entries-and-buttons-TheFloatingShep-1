"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients. For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
from tkinter import *
import math

main = tk.Tk()
main.title("METH")

answer = StringVar()
answer.set("ANSWER")

def toggleA():
    if buttonA["text"] == "+":
        buttonA["text"] = "-"
    else:
        buttonA["text"] = "+"

def toggleB():
    if buttonB["text"] == "+":
        buttonB["text"] = "-"
    else:
        buttonB["text"] = "+"

def do():
    b = float(inputB.get())
    c = float(inputC.get())
    if buttonA["text"] == "-":
        b = b * -1
    if buttonB["text"] == "-":
        c = c * -1
    thing = [((-b + (math.sqrt((b**2) - 4 * 1 * c))) / (2 * 1)),((-b - (math.sqrt((b**2) - 4 * 1 * c))) / (2 * 1))]
    output.delete(0,END)
    output.insert(0,thing)

# Create everything

instruction = tk.Label(text = "INSTRUCTIONS: Figure it out yourself")

frameA = tk.Frame()
frameX = tk.Frame()

inputB = tk.Entry(master = frameA, width = 5)
inputC = tk.Entry(master = frameA, width = 5)

labelA = tk.Label(master = frameA, text = "x^2")
labelB = tk.Label(master = frameA, text = "x")

button = tk.Button(master = frameX, text = "Factor", command = do)
buttonA = tk.Button(master = frameA, text = "+", command = toggleA)
buttonB = tk.Button(master = frameA, text = "+", command = toggleB)

output = Entry(master = frameX, textvariable = answer)

# PACKING EVERYTIHINGSNGSNDG
instruction.pack()

frameA.pack()
frameX.pack()

labelA.pack(side = LEFT)
buttonA.pack(side = LEFT)
inputB.pack(side = LEFT)
labelB.pack(side = LEFT)
buttonB.pack(side = LEFT)
inputC.pack(side = LEFT)

button.pack(side = LEFT)
output.pack(side = LEFT)

main.mainloop()