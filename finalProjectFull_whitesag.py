#main ui window

from tkinter import *

class GUIWindows():
    def __init__(self,main):
        
        self.main=main
        self.btnCreateVault = Button(self, text = "Create Vault", command = self.goToGetMasterPassword)
        self.btnCreateVault.grid(row = 0, column = 0)
        self.btnCloseProgram = Button(self, text = "Close", command = self.finish)
        self.btnCloseProgram.grid(row = 0, column = 1)


    def goToGetMasterPassword(self):
        root2=TopLevel(self.main)
        myGUI=GetMasterPassword(root2)

    def finish(self):
        self.main.destroy()


class GetMasterPassword(Tk): #create class for get master password window of ui
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
    guiWindows = GUIWindows()  #Have the main function call class WindowMain to start the GUI
    getMasterPassword = GetMasterPassword()


if __name__ == "__main__": #check if the system variable name is equal to main
    main() #call main function

# from tkinter import * #imports tkinter
# import random

# class WindowMain(Tk): #create class for main window of UI
#     def __init__(self): #constructor for main window
#         Tk.__init__(self) 

#         self.wm_title("Main Window") #creates title for window - "Main Window"

#         Label(self, text = "Password Vault").grid(row = 0, column = 0) #creates a label for Password Vault and places at (0,0)

#         self.btnCreateVault = Button(self, text = "Create Vault", command = self.PlaceHolder) #creates a button for creating vault
#         self.btnCreateVault.grid(row = 1, column = 0) #assign to grid position 1,0

#         self.btnLoadVault = Button(self, text = "Load Vault", command = self.PlaceHolder) #creates a button for loading vault
#         self.btnLoadVault.grid(row = 2, column = 0) #assign to grid position 2,0

#         self.btnGeneratePassword = Button(self, text = "Generate Password", command = self.PlaceHolder) #creates a button for generate password
#         self.btnGeneratePassword.grid(row = 3, column = 0) #assign to grid position 3,0

#         self.btnChangeMasterPassword = Button(self, text = "Change Master Password", command = self.PlaceHolder) #creates a button for change master password
#         self.btnChangeMasterPassword.grid(row = 4, column = 0) #assign to grid position 4,0

#         self.btnCloseProgram = Button(self, text = "Close Program", command = self.closeWindow) #creates a button for close program
#         self.btnCloseProgram.grid(row = 5, column = 0) #assign to grid position 5,0

#         self.mainloop() #loop window until you push close button on the top window bar



#     def PlaceHolder(self):
#     #      #### TODO: PLACEHOLDER TO ALLOW TO RUN GUI  --  NEED TO CREATE FUNCTIONS TO CALL THE PROPER WINDOWS AND REFERENCE THEM FROM THE BUTTONS ###
#         return

# def main():
#     wdoMain = WindowMain()  #Have the main function call class WindowMain to start the GUI


# if __name__ == "__main__": #check if the system variable name is equal to main
#     main() #call main function