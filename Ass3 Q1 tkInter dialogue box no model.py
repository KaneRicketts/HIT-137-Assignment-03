import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import PIL.Image, PIL.ImageTk
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
from sklearn.preprocessing import LabelEncoder
import sys
import numpy as np

# Variables
# Use list instead of global variable to ensure the image is not "garbage collected", 
#   and the canvas is accessible outside of the funtions(methods).
global_image_list: list[PIL.ImageTk.PhotoImage] = []
global_canvas_list: list[Canvas] = []
file_name: list[str] = []
img_predicted_label: list[str] = []
img_confidence: list[float] = []

########################## PRE-TRAINED MODEL ##########################
# Load the trained model and label encoder
model = load_model("fruit_detector_model.h5")
label_encoder = np.load("label_encoder.npy", allow_pickle=True)

def load_and_prepare_image(image_path):
    try:
        image = load_img(image_path, target_size=(100, 100))
        image = img_to_array(image) / 255.0
        return np.expand_dims(image, axis=0)
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

def predict_fruit(image_path) -> tuple[str, float]:
    image = load_and_prepare_image(image_path)
    if image is None:
        print("Error loading image.")
    
    prediction = model.predict(image)
    predicted_label_index = np.argmax(prediction)
    confidence = prediction[0][predicted_label_index]

    if confidence < 0.5:
        predicted_label = "Not a fruit"
        return (predicted_label, confidence)
    else:
        predicted_label = label_encoder[predicted_label_index]
        #return f"{predicted_label} with {confidence * 100:.2f}% confidence"
        return (predicted_label, confidence)

########################## PRE-TRAINED MODEL ##########################

# Functions to be called.
def print_result() -> None:
    """Display the result to the Entry boxes. Append results to list for access."""
    image_path = file_name[0]
    predicted_label, confidence = predict_fruit(image_path)
    print(predicted_label)
    img_predicted_label.append(predicted_label)
    print(confidence)
    img_confidence.append(confidence)

    disp_type.delete(0, END)
    disp_confidence.delete(0, END)

    fruit = prediction_str()
    disp_type.insert(0, fruit)

    string_confid = prediction_confidence()
    disp_confidence.insert(0, string_confid)

def prediction_str():
    if not img_predicted_label:
        return "Prediction."
    else:
        fruit = img_predicted_label[0]
        return fruit

def prediction_confidence():
    if not img_confidence:
        return "Confidence."
    else:
        value = img_confidence[0]
        confidence = f"{value*100:.2f}%"
        return confidence

# A system message box that requires an "okay" button click by creating a
#   showinfo messagebox, a pre-defined class of "information" box.
def intro() -> None:
    """Generate a messagebox to give a brief introduction to the UI."""
    tkinter.messagebox.showinfo("Instructions", """Select the image filetype, then open the image from a 
    file to determine the type of fruit or vegetable 
    using a pretrained AI image recognition model.""")

# Uses user generated extension input to open an image of *.extension
def set_filetype(filetype) -> None:
    """Change the filetype extension"""
    print(f"The selected filteype is {selected_filetype.get()}")

def open_file() -> None:
    """Open the file using a file selection dialogue to return a filepath based 
        upon limited file extensions that are user defined."""
    reset()
    while True:
        extension = selected_filetype.get()
        print(extension)
        if not extension:
            tkinter.messagebox.showerror("Error", "You must first select a filetype to import an image.")
            break
        elif global_canvas_list:
            tkinter.messagebox.showerror("Error", "You can not select another image without pressing finished.")
            break
        else:
            filename = filedialog.askopenfilename(title = "Select an Image.", filetypes = [("Image Files", f"*.{extension}")])
            
            if not filename:
                break
            elif filename is not None:
                file_name.append(filename)
                print("Loading file...\nDone.")
                break
    scale_image()

def scale_image() -> None:
    """Open the image to determine its size, then adjust to suit the canvas window.
        Also add the image to a list so that it is available once the function is called."""
    filename = file_name[0]
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
    if answer == "yes":
        print(" YAAAYYYY ")
        reset()
    elif answer == "no":
        print("You are no fun!")
        root.destroy()

def reset():
    """Clear the image from its list, then destroys the instance of the canvas, 
        and removes it from its list. Also clear all other lists to prevent issues."""
    global_image_list.clear()
    for canvas in global_canvas_list:
        canvas.destroy()
    global_canvas_list.clear()
    file_name.clear()
    img_predicted_label.clear()
    img_confidence.clear()

    disp_type.delete(0, END)
    disp_confidence.delete(0, END)

    fruit = prediction_str()
    disp_type.insert(0, fruit)

    string_confid = prediction_confidence()
    disp_confidence.insert(0, string_confid)


# Here we create the window UI.
root = Tk()      # This is a class that creates a window.
root.title("🍉🍌🥝  AI Fruit Classifier  🥝🍌🍉")
root.geometry("1200x800")       # Window size.

# Remove minimise and maximise function from the window.
try:
    root.attributes("-toolwindow", True)
except TclError:
    print("This feature is not supported")

# Small delay before calling the introductory messagebox.
root.after(500, intro)

# Create the Frames to arrange and store widgets.
# Master frame.
frame_all = Frame(root, 
                  background = "light gray", 
                  relief = "ridge", 
                  padx = 10, 
                  pady = 10)

frame_all.columnconfigure(0, weight = 1)
frame_all.columnconfigure(1, weight = 3)
frame_all.columnconfigure(2, weight = 1)
frame_all.rowconfigure(0, weight = 1)
frame_all.rowconfigure(1, weight = 10)

frame_all.pack(fill = BOTH, expand = True)

# Top Frame
frame_top = Frame(frame_all, 
                  background = "lightblue", 
                  borderwidth = 2, 
                  padx = 10, 
                  pady = 10)

frame_top.columnconfigure(0, weight =1)
frame_top.columnconfigure(1, weight =3)
frame_top.columnconfigure(2, weight =1)
frame_top.rowconfigure(0, weight = 1)
frame_top.rowconfigure(1, weight = 1)
frame_top.rowconfigure(2, weight = 1)

frame_top.grid(column = 0, row = 0, columnspan = 3, sticky = N+E+S+W)

# Left Frame
frame_left = Frame(frame_all, 
                   background = "lightgray", 
                   borderwidth = 2, 
                   relief = "ridge", 
                   cursor = "pirate", 
                   padx = 10, 
                   pady = 10, )
frame_left.config(width = 750, height = 650)
frame_left.columnconfigure(0, weight = 1)
frame_left.rowconfigure(0, weight = 1)

frame_left.grid(column = 0, columnspan = 2, row = 1, sticky = N+E+S+W)
frame_left.grid_propagate(0)        # We dont want this frame to adjust in size and squish the buttons or text. 

# Right Frame
frame_right = Frame(frame_all, 
                    background = "white", 
                    borderwidth = 2, 
                    padx = 10, 
                    pady = 10, )
frame_left.config(width = 450, height = 650)

frame_right.columnconfigure(0, weight = 1)
frame_right.columnconfigure(1, weight = 1)
frame_right.rowconfigure(0, weight = 1)
frame_right.rowconfigure(1, weight = 1)
frame_right.rowconfigure(2, weight = 1)
frame_right.rowconfigure(3, weight = 1)
frame_right.rowconfigure(4, weight = 1)
frame_right.rowconfigure(5, weight = 1)
frame_right.rowconfigure(6, weight = 1)
frame_right.rowconfigure(7, weight = 2)
frame_right.rowconfigure(8, weight = 1)
frame_right.rowconfigure(9, weight = 2)

frame_right.grid(column = 2,  row = 1, sticky = N+E+S+W) 

# Creating a Title for the window.
heading_label = Label(frame_top, 
                      background = "lightblue", 
                      text = "🍋🍈🍉🍌🥝🍇🍊🥥🍉🍍  AI Fruit Classifier from Trained Model  🍌🍇🍈🍋🍉🍊🍇🥥🍍🥝", 
                      font = ("Arial", 18, "bold"))
heading_label.grid(column = 1, row = 1)

# A label telling the user to select image format from selection box.
type_label = Label(frame_right, 
                   background = "white", 
                   text = "Choose the file format of your image.", 
                   font = ("Arial", 12))
type_label.grid(column = 0, columnspan = 2, row = 1, sticky = W)

#Creating a selection (combobox) box to determine filetype.
selected_filetype = tk.StringVar()

filetype_combobox = ttk.Combobox(frame_right, textvariable = selected_filetype)
filetype_combobox["state"] = "readonly"
filetype_combobox["values"] = ["jpg", "jpeg", "png"]

filetype_combobox.grid(column = 0, row = 2, sticky = NW)

filetype_combobox.bind("<<ComboboxSelected>>", set_filetype)

#Creating a button to open an image.
open_label = Label(frame_right, 
                   background = "white", 
                   text = "Click 'Open' to import an image file.", 
                   font = ("Arial", 12))
open_label.grid(column = 0, columnspan = 2, row = 3, sticky = NW)

open_btn = Button(frame_right, text = "Open", 
                  command = open_file)
open_btn.grid(column = 2, row = 3, sticky = NW)

# Creating a button to check.
open_label = Label(frame_right, 
                   background = "white", 
                   text = "Click 'Check Fruit' to see the type of fruit.", 
                   font = ("Arial", 12))
open_label.grid(column = 0, columnspan = 2, row = 4, sticky = NW)

open_btn = Button(frame_right, 
                  text ="Check Fruit", 
                  command = print_result)
open_btn.grid(column = 2, row = 4, sticky = NW)

# Creating a display for the model output.
# Display type of food.
disp_type = Entry(frame_right, 
                  background = "lightblue", 
                  width = 38, 
                  font=("Arial", 14), 
                  justify = "center")
disp_type.grid(column = 0, columnspan = 3, row = 5, sticky = W)
fruit = prediction_str()
disp_type.insert(0, fruit)

# Display type of fruit.
disp_confidence = Entry(frame_right, 
                        background = "lightblue", 
                        width = 38, 
                        font =("Arial", 14), 
                        justify = "center")
disp_confidence.grid(column = 0, columnspan = 3, row = 6, sticky = W)
confidence = prediction_confidence()
disp_confidence.insert(0, confidence)

# Creating a button to finish or restart.
open_label = Label(frame_right, 
                   background = "white", 
                   text= "Click 'Finish' to Finish.", 
                   font = ("Arial", 12))
open_label.grid(column = 0, columnspan = 2, row = 8, sticky = NW)

open_btn = Button(frame_right, 
                  text = "Finish", 
                  command = try_again)
open_btn.grid(column = 1, row = 8, sticky = NW)

# Mainloop method.
root.mainloop()
