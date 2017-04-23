import random
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

        # self.mainloop() #loop window until you push close button on the top window bar

    def PlaceHolder(self):
         #### TODO: PLACEHOLDER TO ALLOW TO RUN GUI  --  NEED TO CREATE FUNCTIONS TO CALL THE PROPER WINDOWS AND REFERENCE THEM FROM THE BUTTONS ###
        return

class Password(object): #create class for password
    def __init__(self, length, useSpecialChars, useUpperCase, useLowerCase, useNumbers):
        object.__init__(self) #constructor for password class
        self.setLength(length) #setting value for length
        self.setSpecialChars(bool(useSpecialChars)) #setting value for special characters and casting as boolean
        self.setUpperCase(bool(useUpperCase)) #setting value for uppercase and casting as boolean
        self.setLowerCase(bool(useLowerCase)) #setting value for lowercase and casting as boolean
        self.setNumbers(bool(useNumbers)) #setting value for numbers and casting as boolean
        
    def getLength(self): #create a getter for the length function which returns the value of length
        return self.length

    def getSpecialChars(self): #create a getter for the useSpecialChars function which returns the value of useSpecialChars
        return self.useSpecialChars

    def getUpperCase(self): #create a getter for the useUpperCase function which returns the value of useUpperCase
        return self.useUpperCase

    def getLowerCase(self): #create a getter for the useLowerCase function which returns the value of useLowerCase
        return self.useLowerCase

    def getNumbers(self): #create a getter for the useNumbers function which returns the value of useNumbers
        return self.useNumbers

    def setLength(self, length): #create a setter for the length, which sets the value of length to the value provided by user
        self.length = length

    def setSpecialChars(self, useSpecialChars): #create a setter for special characters
        self.useSpecialChars = useSpecialChars

    def setUpperCase(self, useUpperCase): #create a setter for upper case
        self.useUpperCase = useUpperCase

    def setLowerCase(self, useLowerCase): #create a setter for lower case
        self.useLowerCase = useLowerCase

    def setNumbers(self, useNumbers): #create a setter for numbers
        self.useNumbers = useNumbers

    def createPassword(self): #function for creating password
        password = "" #create password variable and give it an empty value
        dictCategories = {} #creates an empty dictionary

        hasSpecialChars = True #creates variable for hasSpecialChars and give it value True
        hasUpperCase = True #creates variable for hasUpperCase and give it value True
        hasLowerCase = True #creates variable for hasLowerCase and give it value True
        hasNumbers = True #creates variable for hasNumbers and give it value True

        #checking if user had selected the specified checkbox, and setting the flag to false
        #it also adds to the dictionary the category and string value
        if self.getSpecialChars() == True: 
            hasSpecialChars = False
            dictCategories["SpecialChars"] = "!@#$%^&*"

        #checking if user had selected the specified checkbox, and setting the flag to false
        #it also adds to the dictionary the category and string value
        if self.getUpperCase() == True:
            hasUpperCase = False
            dictCategories["UpperCase"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        #checking if user had selected the specified checkbox, and setting the flag to false
        #it also adds to the dictionary the category and string value
        if self.getLowerCase() == True:
            hasLowerCase = False
            dictCategories["LowerCase"] = "abcdefghijklmnopqrstuvwxyx"

        #checking if user had selected the specified checkbox, and setting the flag to false
        #it also adds to the dictionary the category and string value
        if self.getNumbers() == True:
            hasNumbers = False
            dictCategories["Numbers"]= "0123456789"

        #gets the length the user specifies and loops through that many times
        for val in range(0,self.getLength()):
            #randomly grabs a category index
            selection = random.randint(0,len(dictCategories)-1)

            #gets the key for the randomly chosen category
            selectionKey = list(dictCategories)[selection]

            #gets a list of all the values for the specified category
            lstCategoryValues = list(dictCategories[selectionKey])

            #gets a random index from the specified cateogry value list
            charIndex = random.randint(0,len(lstCategoryValues)-1)

            #retrieves the randomly chosen character 
            charSelection = lstCategoryValues[charIndex]

            #appends new character to password and casts it as a string
            password += str(charSelection)

            #checks which category key was selected and sets the flag for that category to true
            if selectionKey == "SpecialChars":
                hasSpecialChars = True
            elif selectionKey =="UpperCase":
                hasUpperCase = True
            elif selectionKey == "LowerCase":
                hasLowerCase = True
            elif selectionKey  =="Numbers":
                hasNumbers=True

        #if all flags are true, return password
        #otherwise, use recursion to run function again
        if hasSpecialChars ==True and hasUpperCase ==True and hasLowerCase == True and hasNumbers ==True :
            return password
        else:
            self.createPassword()


class WindowGeneratePassword(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.wm_title("Generate Password") #creates title for window - " "

        Label(self, text = "Generate Password").grid(row = 0, columnspan = 2) #creates a label for Generate password and puts at 0,2
        
        Label(self, text = "Password").grid(row = 1, column = 0) #creates label for Password and places at 1,0
        self.txtGeneratedPassword = Entry(self) #creates textbox for generated password and places at 1,1
        self.txtGeneratedPassword.grid(row = 1, column = 1)

        Label(self, text = "Length").grid(row = 2, column = 0) #creates label for Length and places at 2,0
        self.txtLength = Entry(self) #creates textbox for length and places at 2,1
        self.txtLength.grid(row = 2, column = 1)

        #create checkbox for special characters
        self.cbSpecialCharsVal = IntVar()
        self.cbSpecialChars = Checkbutton(self, text = "Special Characters", variable = self.cbSpecialCharsVal)
        self.cbSpecialChars.grid(row = 2, column = 2) #places checkbox at 2,2

        #create checkbox for uppercase
        self.cbUpperCaseVal = IntVar()
        self.cbUpperCase = Checkbutton(self, text = "Upper Case", variable = self.cbUpperCaseVal)
        self.cbUpperCase.grid(row = 3, column = 0) #places checkbox at 3,0

        #create checkbox for lowercase
        self.cbLowerCaseVal = IntVar()
        self.cbLowerCase = Checkbutton(self, text = "Lower Case", variable = self.cbLowerCaseVal)
        self.cbLowerCase.grid(row = 3, column = 1) #places checkbox at 3,1

        #create checkbox for numbers
        self.cbNumbersVal = IntVar()
        self.cbNumbers = Checkbutton(self, text = "Numbers", variable = self.cbNumbersVal)
        self.cbNumbers.grid(row = 3, column = 2) #places checkbox at 3,2

        #creates button for generating password and places at 4,0
        self.btnGenerate = Button(self, text = "Generate", command = self.CreateNewPassword)
        self.btnGenerate.grid(row = 4, column = 0)

        #creates button for closing window and places at 4,1
        self.btnClose = Button(self, text = "Close", command = self.closeWindow)
        self.btnClose.grid(row = 4, column = 1)

        self.mainloop() #loop window until you push close button on the top window bar

    def closeWindow(self):
        
        return
    
    def CreateNewPassword(self):
        #gets user input for length and stores it in variable length
        length = int(self.txtLength.get())
        #gets user selection for specified textbox 
        useSpecialChars = self.cbSpecialCharsVal.get()
        #gets user selection for specified textbox 
        useUpperCase = self.cbUpperCaseVal.get()
        #gets user selection for specified textbox 
        useLowerCase = self.cbLowerCaseVal.get()
        #gets user selection for specified textbox 
        useNumbers = self.cbNumbersVal.get()
        #creating an instance of password and putting in values provided by user
        password = Password(length,useSpecialChars,useUpperCase,useLowerCase,useNumbers)
        #for instance of password, calling create password function
        p = password.createPassword()
        #clears textbox for generated password
        self.txtGeneratedPassword.delete(0,END)
        #enters generated password into textbox
        self.txtGeneratedPassword.insert(0,p) 

        return

def showTop(self):
    TopLevel()


def main():
    wdoMain = WindowMain()  #Have the main function call class WindowMain to start the GUI


if __name__ == "__main__": #check if the system variable name is equal to main
    main() #call main function