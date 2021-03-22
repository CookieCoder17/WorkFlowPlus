import os # For reading and writing files
import tkinter as tk # Tkinter module
from tkinter import filedialog, Label, simpledialog # for selecting files and prompting to user

class App:
    # Constructor: Calls the methods in the class
    def __init__(self, color1, color2):
        self.root = tk.Tk() 
        self.root.resizable(False, False) # disable resizing the canvas 
        self.root.title("WorkFlow++") # the title for the canvas
        self.files = [] # List used to store the file names 
        self.color1 = color1 # bg
        self.color2 = color2 # fg
        self.setCanvas() # Calls the setCanvas method
        self.setFrame() # Calls the setFrame method
        self.activateButtons() # Calls the activateButtons method
        self.root.mainloop() #mainloop in order to keep the program running
    
    # setCanvas: Sets the canvas for the program
    def setCanvas(self):
        self.canvas = tk.Canvas(self.root, height = 600, width = 480, bg=self.color1)
        self.canvas.pack()
    
    # setFrame: Sets the frame used in the canvas
    def setFrame(self):
        self.frame = tk.Frame(self.root, bg=self.color2)
        self.frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.05)

    # activateButtons: creates the buttons in the canvas to execute the operations
    def activateButtons(self):
        # addFile: adds a file to the list, when clicked calls the add method
        addFile = tk.Button(self.root, text="Add File", fg=self.color1, bg=self.color2, width=10, command = self.add).place(x=150, y=520)

        # runApps: runs the files in the list, when clicked calls the run method
        runApps = tk.Button(self.root, text="Run Apps", fg=self.color1, bg=self.color2, width=10, command = self.run).place(x=250, y=560)

        # saveStack: saves the list into a txt file for future usage, when clicked calls the save method
        saveStack = tk.Button(self.root, text="Save List", fg=self.color1, bg=self.color2, width=10, command = self.save).place(x=150, y=560)

        # openStack: opens a txt file and reads in the list into the program, when clicked calls the open method
        openStack = tk.Button(self.root, text="Open List", fg=self.color1, bg=self.color2, width=10, command = self.open).place(x=250, y=520)
    
    # add: prompts the user to select a file, and appends it to the list and into a label to be displayed in the frame
    def add(self):
        self.filename = filedialog.askopenfilename(title="Select File", initialdir = "/", filetypes = (("All File", "*.*"), ("Executables", "*.exe"))) 
        if self.filename == "": return # incase the user click cancel
        else:
            self.files.append(self.filename)
            self.text = Label(self.frame, text=self.filename, bg = "light grey", width=90, height = 1)
            self.text.pack(pady=1)

    # run: runs the file in the list
    def run(self):
        for file in self.files: os.startfile(file) # uses os.startfile
    
    # save: saves the list into a new txt file
    def save(self):
        filename = simpledialog.askstring("Save File", "Input the name of your txt file") # prompts the user to enter the file's name
        if filename == None: return # incase the user clicks cancel
        with open(filename + ".txt", 'w') as editor:
            for file in self.files:
                editor.write(file + "\n") #write in the file name and go to the next line

    # open: opens a txt file, appends the files into the list and displays the files in the frame
    def open(self):
       self.opefile = filedialog.askopenfilename(title = "Select File", initialdir = "/", filetypes = (("txt files", "*.txt"),("All File", "*.*")))
       with open(self.opefile, 'r') as reader:
           for file in reader.readlines():
                self.files.append(file.strip()) # to remove the empty space, strip was used
                label = Label(self.frame, text=file.strip(), bg="grey", width=90, height = 1)
                label.pack(pady=1)

# main
if __name__ == "__main__":
    myapp = App('midnight blue', 'snow') # you may change the colors to whatever fits you
    