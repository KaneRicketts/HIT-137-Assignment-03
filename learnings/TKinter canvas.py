from tkinter import *

root = Tk()

# We can import *.png files as photos, then insert them as a label.
#   They then need to be packed.
photo = PhotoImage(file="banana.png")
label = Label(root, image=photo)
label.pack()

# A canvas is like a frame that allows drawing.
canvas = Canvas(root, width=200, height=100)
canvas.pack()

# We can create items on that drawing, such as lines:
blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")

# Or shapes.
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

# We can then delete only pieces, or clear the whole canvas.
"""canvas.delete(redLine)
canvas.delete(ALL)"""

root.mainloop()