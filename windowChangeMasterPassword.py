#change master password ui window

#importing tkinter
from tkinter import *


class WindowChangeMasterPassword(Tk): #creating a class for the UI window
    def __init__(self): #
        Tk.__init__(self)

        self.wm_title("Change Master Password")

        Label(self, text = "Change Master Password").grid(row = 0, columnspan = 2)

        Label(self, text = "Current Password").grid(row = 1, column = 0) 
        self.currentPassword = Entry(self)
        self.currentPassword.grid(row = 1, column = 1)

        Label(self, text = "New Password").grid(row = 2, column = 0) 
        self.newPassword = Entry(self)
        self.newPassword.grid(row = 2, column = 1)

        self.btnSaveChanges = Button(self, text = "Save Changes", command = self.PlaceHolder)
        self.btnSaveChanges.grid(row = 3, column = 0)

        self.btnCancel = Button(self, text = "Cancel", command = self.PlaceHolder)
        self.btnCancel.grid(row = 3, column = 1)

        self.mainloop()

    def PlaceHolder(self):

        return

def main():
    wdoChangeMasterPassword = WindowChangeMasterPassword()

if __name__ == "__main__":
    main()