import os
from tkinter.messagebox import showerror
file_to_print = ''
def print_any_file(file="C:/Users/gon/Desktop/Ticketera/q.txt"):
    if os.path.exists(file):
        try:
            os.startfile(file, "print")
        except Exception as e:
            showerror('Error',message='printing Error',detail=e)
    else:
        showerror('Printing Error',message='Please Select a file to print.')
        