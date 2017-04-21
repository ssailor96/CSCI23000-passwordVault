#generate password ui window

#main ui window

#creates GUI for changeMaker assignment

from tkinter import * #imports tkinter

class WindowMain(Tk):
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

        Checkbutton(self,text ="Special Characters",variable = var2).grid(row = 3, sticky = W)




# Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
# Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
# Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
# mainloop()





        # self.btnCalculate = Button(self, text = "Generate Password", command = self.showVals) #creates a button and when clicked makes it invoke showVals function
        # self.btnCalculate.grid(row = 3, column = 0) #assign to grid position 14,0

        # #create a button called clear
        # self.btnClear = Button(self, text = "Change Master Password", command = self.clearTextBoxes) #creates a button and when clicked makes it invoke clearTextBoxes function
        # self.btnClear.grid(row = 4, column = 0) #assign to grid position 14,1

        #         #creates a button called calculate
        # self.btnCalculate = Button(self, text = "Close Program", command = self.showVals) #creates a button and when clicked makes it invoke showVals function
        # self.btnCalculate.grid(row = 5, column = 0) #assign to grid position 14,0

        self.mainloop() #loop window until you push close button on the top window bar
            
        #function to display to the screen the values calculated by the rectangle func


def main():
    wmMain = WindowMain()   # Have the main function call your class App to start the GUI


if __name__ == "__main__": #check if the system variable name is equal to main
    main() #call main function