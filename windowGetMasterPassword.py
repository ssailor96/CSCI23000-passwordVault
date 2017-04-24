#get master password ui window

from tkinter import * #imports tkinter

class WindowGetMasterPassword(Tk): #create class for get master password window of ui
    def __init__(self): #constructor for get master password window
        Tk.__init__(self) 

        self.wm_title("Get Master Password") #creates title for window - "Get Master Password"

        Label(self, text = "Master Password").grid(row = 0, column = 0) #create a label called "Master Password" and places at 0,0
        self.getMasterPassword = Entry(self) #create entry box for get master password and place at 0,1
        self.getMasterPassword.grid(row = 0, column = 1)

        self.btnSubmit = Button(self, text = "Submit", command = self.PlaceHolder) #creates a submit button
        self.btnSubmit.grid(row = 1, column = 0) #assign button to grid position 1,0

        self.btnClear = Button(self, text = "Clear", command = self.PlaceHolder) #creates a clear button
        self.btnClear.grid(row = 1, column = 1) #assign button to grid position 1,1
        
        self.mainloop() #loop window until you push close button on the top window bar



    def PlaceHolder(self):

        return

def main():
    wdoGetMasterPassword = WindowGetMasterPassword()   #Main function calls class WindowGetMasterPassword to start the GUI

if __name__ == "__main__": #check if the system variable name is equal to main
    main() #call main function