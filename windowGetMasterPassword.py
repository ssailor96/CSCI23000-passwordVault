#get master password ui window

from tkinter import * #imports tkinter

class WindowGetMasterPassword(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.wm_title("Get Master Password") #creates title for window
        Label(self, text = "Master Password").grid(row = 0, column = 0)
            #Need to change self.showVals
        self.btnSubmit = Button(self, text = "Submit", command = self.showVals) #creates a button and when clicked makes it invoke showVals function
        self.btnSubmit.grid(row = 1, column = 0) #assign to grid position 1,0
        
        self.mainloop()

def main():
    wmMain = WindowGetMasterPassword()   # Have the main function call your class App to start the GUI

if __name__ == "__main__": #check if the system variable name is equal to main
    main() #call main function