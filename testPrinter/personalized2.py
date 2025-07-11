import win32api
def print_file(file_to_print):   
    if file_to_print:
        
        # Print Hard Copy of File
        win32api.ShellExecute(0,              # NULL since it's not associated with a window
             "print",        # execute the "print" verb defined for the file type
             file_to_print,  # path to the document file to print
             None,           #no parameters, since the target is a document file
             ".",            #current directory, same as NULL here
             0)              # SW_HIDE passed to app associated with the file type                   
print_file('C:/Users/gon/Desktop/Ticketera/img/logo.jpeg')