from tkinter import *
root = Tk()

input_text_area = Text(root)
input_text_area.grid(row=0, column=0, columnspan=4, sticky=N+S+W+E)
input_text_area.configure(background='#4D4D4D')
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()