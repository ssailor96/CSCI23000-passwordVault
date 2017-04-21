#main ui window


from tkinter import * #imports tkinter

class WindowMain(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.wm_title("Main Window") #creates title for window - "Main Window"

        Label(self, text = "Password Vault").grid(row = 0, column = 0) #creates a label for Password Vault and places at (0,0)


        #creates a button called calculate
        self.btnCalculate = Button(self, text = "Create Vault", command = self.showVals) #creates a button and when clicked makes it invoke showVals function
        self.btnCalculate.grid(row = 1, column = 0) #assign to grid position 1,0

        #create a button called clear
        self.btnClear = Button(self, text = "Load Vault", command = self.clearTextBoxes) #creates a button and when clicked makes it invoke clearTextBoxes function
        self.btnClear.grid(row = 2, column = 0) #assign to grid position 14,1        #creates a button called calculate

        self.btnCalculate = Button(self, text = "Generate Password", command = self.showVals) #creates a button and when clicked makes it invoke showVals function
        self.btnCalculate.grid(row = 3, column = 0) #assign to grid position 14,0

        #create a button called clear
        self.btnClear = Button(self, text = "Change Master Password", command = self.clearTextBoxes) #creates a button and when clicked makes it invoke clearTextBoxes function
        self.btnClear.grid(row = 4, column = 0) #assign to grid position 14,1

                #creates a button called calculate
        self.btnCalculate = Button(self, text = "Close Program", command = self.showVals) #creates a button and when clicked makes it invoke showVals function
        self.btnCalculate.grid(row = 5, column = 0) #assign to grid position 14,0

        self.mainloop() #loop window until you push close button on the top window bar

def main():
    wmMain = WindowMain() 


if __name__ == "__main__": #check if the system variable name is equal to main
    main() #call main function