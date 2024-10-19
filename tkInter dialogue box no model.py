import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import PIL.Image
import PIL.ImageTk

# Variables
# Use list instead of global variable to ensure the image is not "garbage collected", 
#   and the canvas is accessible outside of the funtions(methods).
global_image_list: list[PIL.ImageTk.PhotoImage] = []
global_canvas_list: list[Canvas] = []
type_food: list[str] = []
category_food: list[str] = []

# Functions to be called in window.
# A system message box that requires an "okay" button click by creating a
#   showinfo messagebox, a pre-defined class of "information" box.
def intro():
    """Generate a messagebox to give a brief introduction to the UI."""
    tkinter.messagebox.showinfo("Instructions", """Select the image filetype, then open the image from a 
    file to determine the type of fruit or vegetable 
    using a pretrained AI image recognition model.""")

# Uses user generated extension input to open an image of *.extension
def set_filetype(event) -> None:
    """Change the filetype extension"""
    print(f"The selected filteype is {selected_filetype.get()}")

def open_file(extension) -> None:
    """Open the file using a file selection dialogue to return a filepath based 
        upon limited file extensions that are user defined."""
    extension = selected_filetype.get()
    print(extension)
    while True:
        if not extension:
            tkinter.messagebox.showerror("Error", "You must first select a filetype to import an image.")
            break
        elif global_canvas_list:
            tkinter.messagebox.showerror("Error", "You can not select another image without pressing finished.")
            break
        else:
            filename = filedialog.askopenfilename(title = "Select an Image.", filetypes =[("Image Files", f"*.{extension}")])
            if not filename:
                break
            elif filename is not None:
                break
    scale_image(filename)

def scale_image(filename) -> None:
    """Open the image to determine its size, then adjust to suit the canvas window.
        Also add the image to a list so that it is available once the function is called."""
    img_load =  PIL.ImageTk.PhotoImage(PIL.Image.open(filename))
    img_width = img_load.width()
    img_height = img_load.height()
    new_width, new_height = (750, 640)
    if new_width * img_height < new_height * img_width:
        # reduce height to keep original aspect ratio
        new_height = max(1, img_height * new_width // img_width)
    else:
        # reduce width to keep original aspect ratio
        new_width = max(1, img_width * new_height // img_height)
    img = PIL.Image.open(filename)
    resize_image = img.resize((new_width, new_height))
    resized = PIL.ImageTk.PhotoImage(resize_image)
    global_image_list.append(resized)
    img_x, img_y = ((750-new_width)/2), ((640-new_height)/2)
    create_canvas(resized, img_x)

def create_canvas(resized, img_x) -> None:
    """A function to generate an image onto a canvas. The canvas object is then 
        added to a list to allow access outside of the function."""
    canvas = Canvas(frame_left, background = "white")
    canvas.create_image(img_x, 0, image = resized, anchor = NW)
    canvas.pack(anchor = "center", fill = BOTH, expand = True)
    global_canvas_list.append(canvas)

# Add an askquestion box, a predefined class that gives a yes or no button information box,
#   and returns a string "yes", or "no".
def try_again():
    """Call the askquestion messagebox when the user clicks the finish button."""
    answer = tkinter.messagebox.askquestion("AI Fruit and Vegetable Classifier.", "Would you like to try again?")
    if answer == 'yes':
        print(' YAAAYYYY ')
        reset()
    elif answer == 'no':
        print("You are no fun!")
        root.destroy()

def reset():
    """Clear the image from its list, then destroys the instance of the canvas, 
        and removes it from its list."""
    global_image_list.clear()
    for canvas in global_canvas_list:
        canvas.destroy()
    global_canvas_list.clear()

# Here we create the window UI.
root = Tk()      # This is a class that creates a window.
root.title("AI Fruit and Vegetable Classifier.")
root.geometry("1200x800")       # Window size.

# Remove minimise and maximise function from the window.
try:
    root.attributes("-toolwindow", True)
except TclError:
    print("This feature is not supported")

# Small delay before calling the introductory messagebox.
root.after(2000, intro)

# Create the Frames to arrange and store widgets.
# Master frame.
frame_all = Frame(root, background= "light gray", relief= "ridge", padx= 10, pady= 10)

frame_all.columnconfigure(0, weight=1)
frame_all.columnconfigure(1, weight=3)
frame_all.columnconfigure(2, weight=1)
frame_all.rowconfigure(0, weight=1)
frame_all.rowconfigure(1, weight=10)

frame_all.pack(fill= BOTH, expand= True)

# Top Frame
frame_top = Frame(frame_all, borderwidth= 2, padx= 10, pady= 10)

frame_top.columnconfigure(0, weight=1)
frame_top.columnconfigure(1, weight=3)
frame_top.columnconfigure(2, weight=1)
frame_top.rowconfigure(0, weight= 1)
frame_top.rowconfigure(1, weight= 1)
frame_top.rowconfigure(2, weight= 1)

frame_top.grid(column=0, row=0, columnspan= 3, sticky=N+E+S+W)

# Left Frame
frame_left = Frame(frame_all, background= "gray", borderwidth= 2, relief= "ridge", cursor= "pirate", padx= 10, pady= 10, )
frame_left.config(width= 750, height= 650)
frame_left.columnconfigure(0, weight= 1)
frame_left.rowconfigure(0, weight= 1)

frame_left.grid(column=0, columnspan=2, row=1, sticky=N+E+S+W)
frame_left.grid_propagate(0)        # We dont want this frame to adjust in size and squish the buttons or text. 

# Right Frame
frame_right= Frame(frame_all, background= "white", borderwidth= 2, padx= 10, pady= 10, )

frame_right.columnconfigure(0, weight= 1)
frame_right.columnconfigure(1, weight= 1)
frame_right.rowconfigure(0, weight= 2)
frame_right.rowconfigure(1, weight= 1)
frame_right.rowconfigure(2, weight= 1)
frame_right.rowconfigure(3, weight= 1)
frame_right.rowconfigure(4, weight= 1)
frame_right.rowconfigure(5, weight= 2)
frame_right.rowconfigure(6, weight= 2)
frame_right.rowconfigure(7, weight= 2)
frame_right.rowconfigure(8, weight= 2)
frame_right.rowconfigure(9, weight= 2)

frame_right.grid(column=2,  row=1, sticky=N+E+S+W)

# Creating a Title for the window.
heading_label = Label(frame_top, text="AI Fruit and Vegetable Classifier from Trained Model", font=("Arial", 18, "bold"))
heading_label.grid(column = 1, row = 1)

# Adding a little pzazz.
img_L = PIL.ImageTk.PhotoImage(PIL.Image.open(fruitbg.png))

img_R = PIL.ImageTk.PhotoImage(PIL.Image.open(fruitbgR.png))

heading_img_L = Label(frame_top, image = img_L, font=("Arial", 18, "bold"))
heading_label.grid(column = 0, row = 1)

heading_img_R = Label(frame_top, image = img_R, font=("Arial", 18, "bold"))
heading_label.grid(column = 3, row = 1)

# A label telling the user to select image format from selection box.
type_label = Label(frame_right, background= "white", text="Choose the image format of your image.", font=("Arial", 12))
type_label.grid(column= 0, columnspan= 2, row= 1, sticky=W)

#Creating a selection (combobox) box to determine filetype.
selected_filetype = tk.StringVar()

filetype_combobox = ttk.Combobox(frame_right, textvariable = selected_filetype)
filetype_combobox["state"] = "readonly"
filetype_combobox["values"] = ["jpg", "jpeg", "png"]

filetype_combobox.grid(column= 1, row= 2, sticky=W)

filetype_combobox.bind("<<ComboboxSelected>>", set_filetype)

#Creating a button to open an image.
open_label = Label(frame_right, background= "white", text="Click 'Open' to import an image file.", font=("Arial", 12))
open_label.grid(column= 0, columnspan= 2, row= 3, sticky=W)

open_btn = Button(frame_right, text ="Open", command = lambda:open_file(selected_filetype.get()))
open_btn.grid(column= 1, row= 4, sticky=W)

# Creating a display for the model output.
# Display category of food.
disp_category = Entry(frame_right,  width = 38, font=("Arial", 14))
disp_category.grid(column = 1, columnspan = 3, row = 6, sticky = W)
disp_category.insert(0, category_food)
# Display type of food.
disp_type = Entry(frame_right, width = 38, font=("Arial", 14))
disp_type.grid(column = 1, columnspan = 3, row = 7, sticky = W)
disp_type.insert(0, type_food)

# Creating a button to finish or restart.
open_label = Label(frame_right, text="Click 'Finished' to import annother file.", font=("Arial", 12))
open_label.grid(column= 0, columnspan= 2, row= 5, sticky=W)
open_btn = Button(frame_right, text ="Finish", command = try_again)
open_btn.grid(column= 1, row= 6, sticky=W)

# Mainloop method.
root.mainloop()
