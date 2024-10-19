from tkinter import *

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")

def draw_grid():
    pass

root = Tk()         # Blank window, with title className = ""
root.title("AI FRUIT CLASSIFIER APP")
root.maxsize(width = 1000, height = 500)
center_window(root)

# We create a frame inside our root window.
# This can force the window to expand to size 'width =' and 'height ='
frame1 = Frame(root, width=500, height=500, bg = "grey", border = 5)
frame1.grid(row = 0, column = 0, )
frame2 = Frame(root, width=500, height=500, bg = "green", border = 5)
frame2.grid(row = 0, column = 1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# We can import *.png files as photos, then insert them as a label.
#   They then need to be packed.
"""photo = PhotoImage(file="banana.png")
label = Label(root, image=photo)
label.pack()"""

"""# A canvas is like a frame that allows drawing.
canvas = Canvas(frame1, width=300, height=300)
canvas.grid(row = 0, column = 0)

# We can create items on that drawing, such as lines:
blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")

# Or shapes.
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

# We can then delete only pieces, or clear the whole canvas.
# canvas.delete()
"""

root.mainloop()         # Calls the mainloop method on the root window. (Keeps window open.)