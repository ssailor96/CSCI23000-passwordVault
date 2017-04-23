#main ui window


from tkinter import * #imports tkinter

class WindowMain(Tk): #create class for main window of UI
    def __init__(self):
        Tk.__init__(self) #constructor for main window

        self.wm_title("Main Window") #creates title for window - "Main Window"

        Label(self, text = "Password Vault").grid(row = 0, column = 0) #creates a label for Password Vault and places at (0,0)

        self.btnCreateVault = Button(self, text = "Create Vault", command = self.PlaceHolder) #creates a button for creating vault
        self.btnCreateVault.grid(row = 1, column = 0) #assign to grid position 1,0

        self.btnLoadVault = Button(self, text = "Load Vault", command = self.PlaceHolder) #creates a button for loading vault
        self.btnLoadVault.grid(row = 2, column = 0) #assign to grid position 2,0

        self.btnGeneratePassword = Button(self, text = "Generate Password", command = self.PlaceHolder) #creates a button for generate password
        self.btnGeneratePassword.grid(row = 3, column = 0) #assign to grid position 3,0

        self.btnChangeMasterPassword = Button(self, text = "Change Master Password", command = self.PlaceHolder) #creates a button for change master password
        self.btnChangeMasterPassword.grid(row = 4, column = 0) #assign to grid position 4,0

        self.btnCloseProgram = Button(self, text = "Close Program", command = self.PlaceHolder) #creates a button for close program
        self.btnCloseProgram.grid(row = 5, column = 0) #assign to grid position 5,0

        self.mainloop() #loop window until you push close button on the top window bar

    def PlaceHolder(self):
         #### TODO: PLACEHOLDER TO ALLOW TO RUN GUI  --  NEED TO CREATE FUNCTIONS TO CALL THE PROPER WINDOWS AND REFERENCE THEM FROM THE BUTTONS ###
        return

def main():
    wdoMain = WindowMain()  #Have the main function call class WindowMain to start the GUI


if __name__ == "__main__": #check if the system variable name is equal to main
    main() #call main function