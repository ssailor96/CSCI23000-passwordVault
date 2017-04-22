#add account ui window

from tkinter import * 

class WindowAddAccount(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.wm_title("Add Account")

        Label(self, text = "Account Name").grid(row = 0, column = 0) #create a label called "Master Password" and places at 0,0
        self.accountName = Entry(self)
        self.accountName.grid(row = 0, column = 1)

        Label(self, text = "Username").grid(row = 1, column = 0) #create a label called "Master Password" and places at 0,0
        self.username = Entry(self)
        self.username.grid(row = 1, column = 1)

        Label(self, text = "Password").grid(row = 2, column = 0) #create a label called "Master Password" and places at 0,0
        self.password = Entry(self)
        self.password.grid(row = 2, column = 1)

        Label(self, text = "URL").grid(row = 3, column = 0) #create a label called "Master Password" and places at 0,0
        self.url = Entry(self)
        self.url.grid(row = 3, column = 1)
        
        self.btnSave = Button(self, text = "Save", command = self.PlaceHolder)
        self.btnSave.grid(row = 4, column = 0)

        self.btnCancel = Button(self, text = "Cancel", command = self.PlaceHolder)
        self.btnCancel.grid(row = 4, column = 1)

        self.mainloop()

    def PlaceHolder(self):

        return

def main():
    wdoAddAccount = WindowAddAccount()

if __name__ == "__main__":
    main()