import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
def main():
    parent = tk.Tk() #new tk object
    parent.overrideredirect(1) #keep it around
    parent.withdraw() #withdraw it from the screen
    path = filedialog.askdirectory(title='Select a directory to sort the files inside by type\nFiles in folders and folders will', parent=parent) #prompt user to select a directory
    filesort(path) #call filesort function
def filesort(path): #function to sort files
    file_names = os.listdir(path) #get all files in the directory
    destination_folders = {} #dictionary to store destination folders

    now = datetime.now() #get the current date and time
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    #iterate over all files in the directory
    for file_name in file_names:
        file_path = os.path.join(path, file_name) #get the path of the file

        #check type
        if os.path.isfile(file_path): #if it is a file
            #retrieve file extension
            file_extension = os.path.splitext(file_name)[1]

            #Create a folder for the extension if it doesn't exist
            if file_extension not in destination_folders:
                folder_path = os.path.join(path, file_extension[1:]) 
                os.makedirs(folder_path, exist_ok=True) #create the folder
                destination_folders[file_extension] = folder_path
                destination_folder = folder_path
            else: 
                destination_folder = destination_folders[file_extension]  #get the folder path from the dictionary

            #Move the file to its destination folder
            destination_path = os.path.join(destination_folder, file_name) #get the destination path
            shutil.move(file_path, destination_path) #move the file to the destination path
    messagebox.showinfo('Filesorter', 'Completed at: ' + dt_string) #show a message box with the date and time
  
if __name__ == '__main__':
    main()

#Note: This will sort files OUTSIDE of folders while ignoring folders. If you want to sort files inside of folders
#Call the program on each folder individually.
#Written by: Sam Parson
