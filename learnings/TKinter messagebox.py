from tkinter import *
# Requires an extra import.
import tkinter.messagebox

root = Tk()

# We can add a system message box that requires an "okay" button click by creating.
# showinfo is a predefined class of "information" box.
tkinter.messagebox.showinfo('Window Title', 'Monkeys can live up to 300 years.')


# We can add a system message box that requires an "okay" button click by creating.
# askquestion is a predefined class that gives a yes or no button information box,
#   and returns a string "yes", or "no".
answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
    print(' 8==D~~ ')

elif answer == 'no':
    print("You are no fun!")

root.mainloop()