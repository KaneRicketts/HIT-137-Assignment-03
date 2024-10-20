from tkinter import *

root = Tk(className = "Tk Interface")         # Blank window, with title className = ""

# The Label() class allows us to add text.
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

# The Entry() class allows us to recieve user input.
entry_1 = Entry(root)
entry_2 = Entry(root)

# Instead of calling a Frame() and packing(), we can use grid().

# When a widget is smaller than the cell it is inserted into, 
#   sticky can be used to push the widget in a direction (stick to side "").
# The direction is the compass directions: N, E, S, W, NE, NW, SE, and SW

label_1.grid(row = 0, sticky = E)
label_2.grid(row = 1, sticky = E)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

# We can add a checkbutton and label by using the Checkbutton() class.
# If the text is long, we can take up more than 1 column, or row, 
#   with columnspan = , or rowspan = .
check = Checkbutton(root, text="Keep me logged in")
check.grid(columnspan=2)

# We can add a function to "do-something", and bind the function to a Button().
# The bind(event, call-function())
# The we can place it in the grid()

def PrintName(event):
    """Docstring"""
    print("Chello my name is Bucky")

button_1 = Button(root, text="Print Message")
# <Button-1> is an event that means "clicked left mouse button"
button_1.bind("<Button-1>", PrintName)
button_1.grid(row = 4, columnspan= 2)

root.mainloop()
