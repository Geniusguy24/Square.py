import tkinter as tk
import ttkbootstrap as tb
from tkinter import messagebox

def shutdown():
    question = input("Are you sure you want to shut down?")
    if question == "yes" or question == "Yes":
        print("System Shutting Down!")
        print("Goodbye!")
    elif question == ("no" or "No"):
        print("Abort Shut Down!")
    else:
        print("Sorry!")

def GUI_Shutdown():
    quit = messagebox.askyesno(title = "Shutdown", message = "Do you really want to shut down!")
    if quit:
        root.destroy()

shutdown()

GUI = input("Would you like GUI?")

if GUI == ("yes" or "Yes"):
    root = tb.Window(themename = "darkly")

    root.title("Project Shutdown!")
    root.geometry("500x350")

    my_button = tb.Button(root, text = "Shutdown!", command = GUI_Shutdown)
    my_button.pack(pady = 40)

    root.mainloop()

elif GUI == ("no" or "No"):
    print("Ok!")
else:
    print("Sorry Invalid Input!")