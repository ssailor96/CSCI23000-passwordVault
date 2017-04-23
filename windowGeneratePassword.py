#generate password ui window


from tkinter import * #imports tkinter

import random #import random for generating password

specialChars = "!@#$%^&*" #creates variable for special characters and gives value of special characters

upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #creates variable for uppercase letters and gives value of upper case letters

lowerCase = "abcdefghijklmnopqrstuvwxyx" #creates variable for lowercase letters and gives value of lower case letters

numbers = "0123456789" #creates variable for numbers and gives value of numbers

class Password(object):
    def __init__(self, length, useSpecialChars, useUpperCase, useLowerCase, useNumbers):
        object.__init__(self)
        self.setLength(length)
        self.setSpecialChars(bool(useSpecialChars))
        self.setUpperCase(bool(useUpperCase))
        self.setLowerCase(bool(useLowerCase))
        self.setNumbers(bool(useNumbers))
        
    def getLength(self):
        return self.length

    def getSpecialChars(self):
        return self.useSpecialChars

    def getUpperCase(self):
        return self.useUpperCase

    def getLowerCase(self):
        return self.useLowerCase

    def getNumbers(self):
        return self.useNumbers

    def setLength(self, length):
        self.length = length

    def setSpecialChars(self, useSpecialChars):
        self.useSpecialChars = useSpecialChars

    def setUpperCase(self, useUpperCase):
        self.useUpperCase = useUpperCase

    def setLowerCase(self, useLowerCase):
        self.useLowerCase = useLowerCase

    def setNumbers(self, useNumbers):
        self.useNumbers = useNumbers

    def createPassword(self):
        password = ""
        dictCategories = {}

        hasSpecialChars = True
        hasUpperCase = True
        hasLowerCase = True 
        hasNumbers = True

        if self.getSpecialChars() == True:
            hasSpecialChars = False
            dictCategories["SpecialChars"] = specialChars

        if self.getUpperCase() == True:
            hasUpperCase = False
            dictCategories["UpperCase"] = upperCase

        if self.getLowerCase() == True:
            hasLowerCase = False
            dictCategories["LowerCase"] = lowerCase

        if self.getNumbers() == True:
            hasNumbers = False
            dictCategories["Numbers"]= numbers

        for val in range(0,self.getLength()):
            selection = random.randint(0,len(dictCategories)-1)

            selectionKey = list(dictCategories)[selection]

            blah = list(dictCategories[selectionKey])

            charIndex = random.randint(0,len(blah)-1)

            charSelection = blah[charIndex]

            password += str(charSelection)

            if selectionKey == "SpecialChars":
                hasSpecialChars = True
            elif selectionKey =="UpperCase":
                hasUpperCase = True
            elif selectionKey == "LowerCase":
                hasLowerCase = True
            elif selectionKey  =="Numbers":
                hasNumbers=True

        if hasSpecialChars ==True and hasUpperCase ==True and hasLowerCase == True and hasNumbers ==True :
            return password
        else:
            self.createPassword()


class WindowGeneratePassword(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.wm_title("Generate Password") #creates title for window - " "

        Label(self, text = "Generate Password").grid(row = 0, columnspan = 2) #creates a label for Change Needed and places at 5,2
        
        Label(self, text = "Password").grid(row = 1, column = 0)
        self.txtGeneratedPassword = Entry(self)
        self.txtGeneratedPassword.grid(row = 1, column = 1)

        Label(self, text = "Length").grid(row = 2, column = 0)
        self.txtLength = Entry(self)
        self.txtLength.grid(row = 2, column = 1)

        self.cbSpecialCharsVal = IntVar()
        self.cbSpecialChars = Checkbutton(self, text = "Special Characters", variable = self.cbSpecialCharsVal)
        self.cbSpecialChars.grid(row = 2, column = 2)

        self.cbUpperCaseVal = IntVar()
        self.cbUpperCase = Checkbutton(self, text = "Upper Case", variable = self.cbUpperCaseVal)
        self.cbUpperCase.grid(row = 3, column = 0)

        self.cbLowerCaseVal = IntVar()
        self.cbLowerCase = Checkbutton(self, text = "Lower Case", variable = self.cbLowerCaseVal)
        self.cbLowerCase.grid(row = 3, column = 1)

        self.cbNumbersVal = IntVar()
        self.cbNumbers = Checkbutton(self, text = "Numbers", variable = self.cbNumbersVal)
        self.cbNumbers.grid(row = 3, column = 2)

        self.btnGenerate = Button(self, text = "Generate", command = self.CreateNewPassword)
        self.btnGenerate.grid(row = 4, column = 0)

        self.btnClose = Button(self, text = "Close", command = self.PlaceHolder)
        self.btnClose.grid(row = 4, column = 1)

        self.mainloop() #loop window until you push close button on the top window bar

    def PlaceHolder(self):
        
        return
    
    def CreateNewPassword(self):
        length = int(self.txtLength.get())
        useSpecialChars = self.cbSpecialCharsVal.get()
        useUpperCase = self.cbUpperCaseVal.get()
        useLowerCase = self.cbLowerCaseVal.get()
        useNumbers = self.cbNumbersVal.get()
        password = Password(length,useSpecialChars,useUpperCase,useLowerCase,useNumbers)
        p = password.createPassword()
        self.txtGeneratedPassword.delete(0,END)
        self.txtGeneratedPassword.insert(0,p) 

        return


def main():
    wdoGeneratePassword = WindowGeneratePassword()   # Have the main function call your class App to start the GUI


if __name__ == "__main__": #check if the system variable name is equal to main
    main() #call main function