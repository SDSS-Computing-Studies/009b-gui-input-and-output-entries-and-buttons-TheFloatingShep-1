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

answer = StringVar()
answer.set("ANSWER")

def doTheThingThatPutsNumbersTogetherAndGetsAnOutput():
    output = 1 + 1
    output.delete(0,END)
    output.insert(0,output)

# Create everything
main = tk.Tk()
main.title("METH")

instruction = tk.Label(text = "INSTRUCTIONS: Figure it out yourself")

frameA = tk.Frame()
frameB = tk.Frame()
frameC = tk.Frame()
frameX = tk.Frame()

inputA = tk.Entry(master = frameA)
inputB = tk.Entry(master = frameB)
inputC = tk.Entry(master = frameC)

labelA = tk.Label(master = frameA, text = "A = 1")
labelB = tk.Label(master = frameB, text = "B")
labelC = tk.Label(master = frameC, text = "C")

button = tk.Button(master = frameX, text = "Factor", command = lambda: doTheThingThatPutsNumbersTogetherAndGetsAnOutput)

output = tk.Entry(master = frameX, textvariable = answer)

# PACKING EVERYTIHINGSNGSNDG
instruction.pack()

frameA.pack()
frameB.pack()
frameC.pack()
frameX.pack()

labelA.pack(side = LEFT)
labelB.pack(side = LEFT)
labelC.pack(side = LEFT)

#inputA.pack(side = LEFT)
inputB.pack(side = LEFT)
inputC.pack(side = LEFT)

button.pack(side = LEFT)
output.pack(side = LEFT)

main.mainloop()