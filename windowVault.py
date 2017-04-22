# Sample found at http://stackoverflow.com/questions/22456445/how-to-imitate-this-table-using-tkinter

from tkinter import *
from tkinter.ttk import *


class Vault(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateWindow()
        self.LoadTable()
        self.grid(sticky = (N+S+W+E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)


    def CreateWindow(self):
        Label(self, text = "Vault").grid(row = 0, column = 0)

        self.btnAddAccount = Button(self, text = "Add Account", command = self.PlaceHolder)
        self.btnAddAccount.grid(row = 1, column = 0)

        self.btnEditAccount = Button(self, text = "Edit Account", command = self.PlaceHolder)
        self.btnEditAccount.grid(row = 2, column = 0)

        self.CreateTable()

        return

    def CreateTable(self):
        tv = Treeview(self)
        tv['columns'] = ('password', 'accounturl')
        tv.heading("#0", text='Username', anchor='w')
        tv.column("#0", anchor='w')
        tv.heading('password', text='Password')
        tv.column('password', anchor='w', width=200)
        tv.heading('accounturl', text='Account URL')
        tv.column('accounturl', anchor='w', width=250)
        tv.grid(sticky = (N+S+W+E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text=" ", values=(' ',' ',' '))
        self.treeview.insert('', 'end', text=" ", values=(' ',' ',' '))
        
    def PlaceHolder(self):
        
        return

def main():
    root = Tk()
    Vault(root)
    root.mainloop()

if __name__ == '__main__':
    main()