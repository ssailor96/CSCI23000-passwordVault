#add account ui window

#import tkinter
from tkinter import * 

class WindowAddAccount(Tk): #create class for add account window
    def __init__(self): #create constructor for add account window class
        Tk.__init__(self) 

        self.wm_title("Add Account") #add title for window - 'Add account'

        Label(self, text = "Account Name").grid(row = 0, column = 0) #create a label called "Account Name" and place at 0,0
        self.accountName = Entry(self) #create entry box for account name and place at 0,1
        self.accountName.grid(row = 0, column = 1)

        Label(self, text = "Username").grid(row = 1, column = 0) #create a label called "Username" and place at 1,0
        self.username = Entry(self) #create entry box for username and place at 1,1
        self.username.grid(row = 1, column = 1)

        Label(self, text = "Password").grid(row = 2, column = 0) #create a label called " Password" and place at 2,0
        self.password = Entry(self) #create entry box for password and place at 2,1
        self.password.grid(row = 2, column = 1)

        Label(self, text = "URL").grid(row = 3, column = 0) #create a label called "URL " and places at 3,0
        self.url = Entry(self) #create entry box for url and place at 3,1
        self.url.grid(row = 3, column = 1)
        
        self.btnSave = Button(self, text = "Save", command = self.PlaceHolder) #create button for saving changes and place at 4,0
        self.btnSave.grid(row = 4, column = 0)

        self.btnCancel = Button(self, text = "Cancel", command = self.PlaceHolder) #create cancel button and place at 4,1
        self.btnCancel.grid(row = 4, column = 1)

        self.mainloop() #loop until user closes UI

    def PlaceHolder(self):

        return

def main(): #launches add account window
    wdoAddAccount = WindowAddAccount()

if __name__ == "__main__": #launches main function
    main()