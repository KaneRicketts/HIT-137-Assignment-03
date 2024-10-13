from tkinter import *

# We can create a new BuckysButtons class.
class BuckysButtons:

    # In the class, we can call a master frame.
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        # Then we can add an instance of the Button class() 
        #   anchor it to the frame, and pack it into the frame in 'side = '.
        # Instead of .bind(), we can call a 'command =' inside the button class, 
        #   and call a method from our BuckysButton class().
        self.printButton = Button(frame, text = "Print Message", command = self.printMessage)
        self.printButton.pack(side = LEFT)

        # Or we can call a 'command =' inside the button class, 
        #   and use a method directly, instead of button.bind().
        self.quitButton = Button(frame, text="Quit", command = frame.quit)
        self.quitButton.pack(side = LEFT)

    def printMessage(self):
        print("Wow, this actually worked!")

# Then we can just create our window and call our class.
root = Tk()
b_button = BuckysButtons(root)
root.mainloop()