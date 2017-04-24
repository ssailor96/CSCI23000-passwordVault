#sources:

# http://stackoverflow.com/questions/8009176/function-to-close-the-window-in-tkinter
# http://stackoverflow.com/questions/22456445/how-to-imitate-this-table-using-tkinter

#import json for storing data
import json
#import tkinter for gui
from tkinter import *
#import tkinter.ttk
from tkinter.ttk import *

class Account(object): #create class for account
    def __init__(self,accountName,username,password,url):
        object.__init__(self) #constructor for account class
        self.AccountName = accountName #TODO: create getters and setters
        self.Username = username
        self.Password = password
        self.Url = url

class App(Frame): #creates class for App
    def __init__(self, parent): #constructor for App class
        Frame.__init__(self, parent) 
        self.CreateUI() #calls function CreateUI
        #function call to read and create a list of accounts from a json file
        #note user needs to paste their path to the json file in order for this to work
        accounts = self.CreateRecords("FILE PATH NEEDS TO BE ENTERED HERE")
        #function call to load table by passing in the list of accounts
        self.LoadTable(accounts)
        #giving table ability to expand with window
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
    
    def selectItem(self,event): #function for getting an item in the treeview that the user has double-clicked on
        curItem = self.treeview.focus()
        value = (self.treeview.item(curItem)['values'])
        self.showTop(value)
        print(value)

    #make create ui function
    def CreateUI(self):
        #creating a treeview on the gui
        tree = Treeview(self)
        #create columns and headings for grid
        tree['columns'] = ('username', 'password','url')
        tree.heading("#0", text='accountName', anchor='w')
        tree.column("#0", anchor="w")
        tree.heading('username', text='Username')
        tree.column('username', anchor='center', width=200)
        tree.heading('password', text='Password')
        tree.column('password', anchor='center', width=200)
        tree.heading('url', text='Url')
        tree.column('url', anchor='center', width=200)
        #gets the item in the treeview that the user selected
        tree.bind('<Double-1>', self.selectItem)
        tree.grid(sticky = (N,S,W,E))
        #gives table ability to expand with window
        self.treeview = tree
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def CreateRecords(self,jsonPath): #create records function reads a json file and creates a list of accounts from the data in the json file
        accounts = []
        jsonContent = GetJsonFromFile(jsonPath)

        for idx,i in enumerate(jsonContent): #loop through each json object and create an instance of account with that data
            #account objects are added to a list of accounts
            accounts.append(Account(jsonContent[idx]["AccountName"],jsonContent[idx]["Username"],jsonContent[idx]["Password"],jsonContent[idx]["Url"]))    
        #return list of accounts
        return accounts

    def LoadTable(self,lstAccounts): #function for loading data into treeview from the accounts list
        for account in lstAccounts:
            self.treeview.insert('','end',text=account.AccountName,values=(account.Username,account.Password,account.Url))

    def showTop(self,txt): #function to launch a new window
        Toplevel(App2(txt))

def main(): 
    #create an instance of tk
    root = Tk()
    #launch app window
    app = App(root)
    #initiate main loop 
    root.mainloop()

def GetJsonFromFile(filePath): #function for reading the json file and returning the data
    with open(filePath,'r') as json_data:
        return json.load(json_data)

class App2(Tk): #creates class for App2, an extra window
    def __init__(self,txt):
        Tk.__init__(self)
        
        #prints out value user selected in treeview window
        Label(self, text = txt).grid(row = 2, column = 0) #creates label and places at 2,0
        # self.txtEntry = Entry(self)
        # self.txtEntry.grid(row = 2, column = 1)
        self.mainloop() #repeats until user closes gui
        
if __name__ == '__main__': #launches into the main function
    main()