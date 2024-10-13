from tkinter import *

root = Tk()

# Defining a function to "do-something" at an event.
# The name of the function is misleading, it means nothing.
def leftClick(event):
    print("Left")

def middleClick(event):
    print("Middle")

def rightClick(event):
    print("Right")

# We create a frame inside our root window.
# This can force the window to expand to size 'width =' and 'height ='
frame = Frame(root, width=300, height=200)


# We can bind the event to the frame itself:
# i.e. if you click anywhere inside this frame, we assess that click event.
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)

# We then pack the frame to the window.
frame.pack()

root.mainloop()