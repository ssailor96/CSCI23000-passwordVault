#change master password ui window

#importing tkinter
from tkinter import *


class WindowChangeMasterPassword(Tk): #creating a class for the UI window
    def __init__(self): #constructor for change master password window class
        Tk.__init__(self)

        self.wm_title("Change Master Password") #title for window - "Change Master Password"

        Label(self, text = "Change Master Password").grid(row = 0, columnspan = 2) #create label for change master password and place at 0,2

        Label(self, text = "Current Password").grid(row = 1, column = 0) #create label for "Current Password" and place at 1,0
        self.currentPassword = Entry(self) #create entry box for current password
        self.currentPassword.grid(row = 1, column = 1) #place entry box at 1,1

        Label(self, text = "New Password").grid(row = 2, column = 0) #create label for "New Password" and place at 2,0
        self.newPassword = Entry(self) #create entry box for new password
        self.newPassword.grid(row = 2, column = 1) #place entry box at 2,1

        self.btnSaveChanges = Button(self, text = "Save Changes", command = self.PlaceHolder) #create button for saving changes and place at 3,0
        self.btnSaveChanges.grid(row = 3, column = 0)

        self.btnCancel = Button(self, text = "Cancel", command = self.PlaceHolder) #create button for canceling window and place at 3,1
        self.btnCancel.grid(row = 3, column = 1)

        self.mainloop() #loop until user closes program

    def PlaceHolder(self): #temporary placeholder function 

        return

def main():
    wdoChangeMasterPassword = WindowChangeMasterPassword() # Have the main function call your class WindowChangeMasterPassword to start the GUI

if __name__ == "__main__":
    main() #call main function