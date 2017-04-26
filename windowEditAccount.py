#edit account ui window

from tkinter import * 

class WindowEditAccount(Tk): #create class for edit account window
    def __init__(self): #create constructor for edit account window class
        Tk.__init__(self) 

        self.wm_title("Edit Account") #add title for window - 'Edit account'

        Label(self, text = "Current Account Name").grid(row = 0, column = 0) #create a label called "Account Name" and place at 0,0
        self.currentAccountName = Entry(self) #create entry box for account name and place at 0,1
        self.currentAccountName.grid(row = 0, column = 1)

        Label(self, text = "New Account Name").grid(row = 1, column = 0) #create a label called "Account Name" and place at 0,0
        self.newAccountName = Entry(self) #create entry box for account name and place at 0,1
        self.newAccountName.grid(row = 1, column = 1)

        Label(self, text = "Current Username").grid(row = 2, column = 0) #create a label called "Username" and place at 1,0
        self.currentUsername = Entry(self) #create entry box for username and place at 1,1
        self.currentUsername.grid(row = 2, column = 1)

        Label(self, text = "New Username").grid(row = 3, column = 0) #create a label called "Username" and place at 1,0
        self.newUsername = Entry(self) #create entry box for username and place at 1,1
        self.newUsername.grid(row = 3, column = 1)

        Label(self, text = "Current Password").grid(row = 4, column = 0) #create a label called " Password" and place at 2,0
        self.currentPassword = Entry(self) #create entry box for password and place at 2,1
        self.currentPassword.grid(row = 4, column = 1)

        Label(self, text = "New Password").grid(row = 5, column = 0) #create a label called " Password" and place at 2,0
        self.newPassword = Entry(self) #create entry box for password and place at 2,1
        self.newPassword.grid(row = 5, column = 1)

        Label(self, text = "Current URL").grid(row = 6, column = 0) #create a label called "URL " and places at 3,0
        self.currentUrl = Entry(self) #create entry box for url and place at 3,1
        self.currentUrl.grid(row = 6, column = 1)

        Label(self, text = "New URL").grid(row = 7, column = 0) #create a label called "URL " and places at 3,0
        self.newUrl = Entry(self) #create entry box for url and place at 3,1
        self.newUrl.grid(row = 7, column = 1)

        self.btnSave = Button(self, text = "Save", command = self.PlaceHolder) #create button for saving changes and place at 4,0
        self.btnSave.grid(row = 8, column = 0)

        self.btnCancel = Button(self, text = "Cancel", command = self.PlaceHolder) #create cancel button and place at 4,1
        self.btnCancel.grid(row = 8, column = 1)

        self.mainloop() #loop until user closes UI

    def PlaceHolder(self):

        return

def main(): #launches edit account window
    wdoEditAccount = WindowEditAccount()

if __name__ == "__main__": #launches main function
    main()