# Sample found at http://stackoverflow.com/questions/22456445/how-to-imitate-this-table-using-tkinter

#import tkinter
from tkinter import *
#import tkinter.ttk
from tkinter.ttk import *


class Vault(Frame): #create class for vault

    def __init__(self, parent):
        Frame.__init__(self, parent) #constructor for vault class
        self.CreateWindow() #calling create window function
        self.LoadTable() #calling load table function
        #creates a grid and enables it to expand when window expands
        self.grid(sticky = (N+S+W+E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)


    def CreateWindow(self): #make function for create window
        Label(self, text = "Vault").grid(row = 0, column = 0) #create lable for vault and place at 0,0

        #create button for 'add account' and place at 1,0
        self.btnAddAccount = Button(self, text = "Add Account", command = self.PlaceHolder)
        self.btnAddAccount.grid(row = 1, column = 0)

        #create button for 'edit account' and place at 2,0
        self.btnEditAccount = Button(self, text = "Edit Account", command = self.PlaceHolder)
        self.btnEditAccount.grid(row = 2, column = 0)

        #call create table function
        self.CreateTable()

        return

    #make create table function
    def CreateTable(self):
        
        tv = Treeview(self)
        #create columns and headings for grid
        tv['columns'] = ('password', 'accounturl')
        tv.heading("#0", text='Username', anchor='w')
        tv.column("#0", anchor='w')
        tv.heading('password', text='Password')
        tv.column('password', anchor='w', width=200)
        tv.heading('accounturl', text='Account URL')
        tv.column('accounturl', anchor='w', width=250)
        #make grid able to expand with window
        tv.grid(sticky = (N+S+W+E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self): #creates function for loading table
        self.treeview.insert('', 'end', text=" ", values=(' ',' ',' '))
        
    def PlaceHolder(self):
        
        return

def main():
    root = Tk()
    Vault(root)
    root.mainloop()

if __name__ == '__main__':
    main()