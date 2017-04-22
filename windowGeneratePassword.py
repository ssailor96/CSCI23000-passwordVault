#generate password ui window


from tkinter import * #imports tkinter

class GeneratePassword(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.wm_title("Generate Password") #creates title for window - "Change Maker"

        Label(self, text = "Generate Password").grid(row = 0, columnspan = 2) #creates a label for Change Needed and places at 5,2
        
        Label(self, text = "Password").grid(row = 1, column = 0)
        self.generatedPassword = Entry(self)
        self.generatedPassword.grid(row = 1, column = 1)

        Label(self, text = "Length").grid(row = 2, column = 0)
        self.length = Entry(self)
        self.length.grid(row = 2, column = 1)

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

        self.btnGenerate = Button(self, text = "Generate", command = self.PlaceHolder)
        self.btnGenerate.grid(row = 4, column = 0)

        self.btnClose = Button(self, text = "Close", command = self.PlaceHolder)
        self.btnClose.grid(row = 4, column = 1)

        self.mainloop() #loop window until you push close button on the top window bar

    def PlaceHolder(self):
        
        return


def main():
    wdoGeneratePassword = GeneratePassword()   # Have the main function call your class App to start the GUI


if __name__ == "__main__": #check if the system variable name is equal to main
    main() #call main function