###############################################################################################
# Python Tkinter Dybamically Resize Buttons 
#############################################################################################

from tkinter import *

root = Tk()
root.title('Dybamically Resize Buttons')
root.iconbitmap('icons/theapplication.ico')
root.geometry("500x500") 

# Config our column rows and cols
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

# Config row 2
Grid.rowconfigure(root, 1, weight=1)


# Create two Buttons
button_1 = Button(root, text="Button 1")
button_2 = Button(root, text="Button 2")

# Grid thm to the screen
button_1.grid(row=0, column=0, sticky="nsew")
button_2.grid(row=1, column=0, sticky="nsew")




root.mainloop()
