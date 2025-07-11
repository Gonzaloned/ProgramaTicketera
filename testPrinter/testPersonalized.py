import os
def print_any_file(file=None):
    if os.path.exists(file):
        try:
            os.startfile(file, "print")
        except Exception as e:
            print(e)

print_any_file('C:/Users/gon/Desktop/Ticketera/RCC.txt')