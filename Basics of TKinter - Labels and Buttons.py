from tkinter import *

root = Tk()         # Create a blank window.

label_1 = Label(root, text = "Assessment 3 - Q1 Tk Interface Application", bg = "red", fg = "white")
label_1.pack(side = TOP)            # pack the Label widget into the root window.

# Instead of a side = , we can use fill = X to make the widget as wide as the parent area.
label_2 = Label(root, text="Two", bg="green", fg="black")
label_2.pack(side = BOTTOM, fill = X)

label_3 = Label(root, text="Three", bg="blue", fg="white")
label_3.pack(side = LEFT, fill = Y)

label_4 = Label(root, text="Four", bg="blue", fg="white")
label_4.pack(side = RIGHT, fill = Y)

# Once we have created a root(window), we can add a frame to it 
#   to help split up the next features.
top_frame = Frame(root)
top_frame.pack(side = TOP)

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

# Initialising Button class objects.
        # Button(anchor=, text=, fg= (font colour))

button_1 = Button(top_frame, text="Button 1", fg="red")
button_2 = Button(top_frame, text="Button 2", fg="blue")
button_3 = Button(top_frame, text="Button 3", fg="green")
button_4 = Button(bottom_frame, text="Button 4", fg="purple")

# Pack the buttons into the frame.
button_1.pack(side = LEFT)
button_2.pack(side = LEFT)
button_3.pack(side = LEFT)

button_4.pack(side = BOTTOM)

root.mainloop()         # Calls the mainloop method on the root window. (Keeps window open.)