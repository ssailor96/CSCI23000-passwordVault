#main ui window

#creates GUI for changeMaker assignment

from tkinter import * #imports tkinter

class WindowMain(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.wm_title("Main Window") #creates title for window - "Change Maker"

        Label(self, text = "Password Vault").grid(row = 0, column = 0) #creates a label for Change Needed and places at 5,2


        #creates a button called calculate
        self.btnCalculate = Button(self, text = "Create Vault", command = self.showVals) #creates a button and when clicked makes it invoke showVals function
        self.btnCalculate.grid(row = 1, column = 0) #assign to grid position 14,0

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

        #function to clear all text boxes of values
    def clearTextBoxes(self):
        self.txtPrice.delete(0,END) #deletes contents of txtbox by going to the beginning of it and clearing till the end
        self.txtTendered.delete(0,END) #deletes contents of txtbox by going to the beginning of it and clearing till the end
        
        self.twenties.delete(0,END) #deletes contents of txtbox by going to the beginning of it and clearing till the end
        self.tens.delete(0,END) #deletes contents of txtbox by going to the beginning of it and clearing till the end
        self.fives.delete(0,END) #deletes contents of txtbox by going to the beginning of it and clearing till the end
        self.ones.delete(0,END) #deletes contents of txtbox by going to the beginning of it and clearing till the end
        self.quarters.delete(0,END) #deletes contents of txtbox by going to the beginning of it and clearing till the end
        self.dimes.delete(0,END) #deletes contents of txtbox by going to the beginning of it and clearing till the end
        self.nickels.delete(0,END) #deletes contents of txtbox by going to the beginning of it and clearing till the end
        self.pennies.delete(0,END) #deletes contents of txtbox by going to the beginning of it and clearing till the end

            
        #function to display to the screen the values calculated by the rectangle func
    def showVals(self):
        price = float(self.txtPrice.get()) #get the value of Price from txtPrice and cast as an int
        tendered = float(self.txtTendered.get()) #get value of Tendered and cast as an int
        change = ChangeCalulator(price,tendered) #creates instance of rectangle and using the constructor pass the Price and Tendered

        self.twenties.insert(1,str(change.getTwenties())) #inserts the amount of twenties needed into GUI for user to see
        self.tens.insert(1,str(change.getTens())) #inserts the amount of tens needed into GUI for user to see
        self.fives.insert(1,str(change.getFives())) #inserts the amount of fives needed into GUI for user to see
        self.ones.insert(1,str(change.getOnes())) #inserts the amount of ones needed into GUI for user to see
        self.quarters.insert(1,str(change.getQuarters())) #inserts the amount of quarters needed into GUI for user to see
        self.dimes.insert(1,str(change.getDimes())) #inserts the amount of dimes needed into GUI for user to see
        self.nickels.insert(1,str(change.getNickels())) #inserts the amount of nickels needed into GUI for user to see
        self.pennies.insert(1,str(change.getPennies())) #inserts the amount of pennies needed into GUI for user to see

class ChangeCalulator(object): #ChangeCalulator class inheriting from object
    def __init__(self,price = 0,tendered = 0): #constructor for ChangeCalculator taking values for Price and Tendered and providing a value of 0 as default
        object.__init__(self) #invoke the constructor from object
        self.setPrice(price) #using the Price provided, assign it to the Price variable of the instance using setPrice function
        self.setTendered(tendered) #using the Tendered provided, assign it to the Tendered variable of the instance using setTendered function
        self.calculateChange() #instance for calculateChange
    
    def getPrice(self): #create a getter for the Price function which returns the value of Price
        return self.price 

    def getTendered(self): #create a getter for the Tendered function which returns the value of Tendered
        return self.tendered

    def setPrice(self, Price): #create a setter for the Price, which sets the value of Price to the value provided by the user
        self.price = Price

    def setTendered(self, Tendered): #create a setter for the Tendered, which sets the value of Tendered to the value provided by the user
        self.tendered = Tendered

    def getTwenties(self): #create a getter for the Twenties function which returns the value of Twenties
        return self.twenties

    def getTens(self): #create a getter for the Tens function which returns the value of Tens
        return self.tens

    def getFives(self): #create a getter for the Fives function which returns the value of Fives
        return self.fives

    def getOnes(self): #create a getter for the Ones function which returns the value of Ones
        return self.ones

    def getQuarters(self): #create a getter for the Quarters function which returns the value of Quarters
        return self.quarters

    def getDimes(self): #create a getter for the Dimes function which returns the value of Dimes
        return self.dimes

    def getNickels(self): #create a getter for the Nickels function which returns the value of Nickels
        return self.nickels

    def getPennies(self): #create a getter for the Pennies function which returns the value of Pennies
        return self.pennies

    def calculateChange(self):

        #creates variables for different amounts of change and assigns 0 to them
        twenties = 0
        tens = 0
        fives = 0
        ones = 0
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
        
        amtTendered = self.getTendered() #get value of Tendered and assign it to variable amtTendered
        price = self.getPrice() #get value of Price and assign it to variable price

        changeNeeded = amtTendered - price #calculates the amount of change needed by subtracting price from the amount tendered

        #if statements ensure proper modulus by avoiding modulus operations with less than values
        if changeNeeded >= 20:
            #this finds remainder for needed change in twenties
            remainder = changeNeeded % 20
            #this subtracts the remainder from change needed in order to find divisible amount to find number of denominations
            total = changeNeeded - remainder
            #determine number of twenties required
            twenties = total / 20
            #reset running total of change needed
            changeNeeded = remainder

        if changeNeeded >= 10:
            #this finds remainder for needed change in tens
            remainder = changeNeeded % 10
            #this subtracts the remainder from change needed in order to find divisible amount to find number of denominations
            total = changeNeeded - remainder
            #determine number of tens required
            tens = total / 10
            #reset running total of change needed
            changeNeeded = remainder

        if changeNeeded >= 5:
            #this finds remainder for needed change in fives
            remainder = changeNeeded % 5
            #this subtracts the remainder from change needed in order to find divisible amount to find number of denominations
            total = changeNeeded - remainder
            #determine number of fives required
            fives = total / 5
            #reset running total of change needed
            changeNeeded = remainder

        if changeNeeded >= 1:
            #this finds remainder for needed change in ones
            remainder = changeNeeded % 1
            #this subtracts the remainder from change needed in order to find divisible amount to find number of denominations
            total = changeNeeded - remainder
            #determine number of ones required
            ones = total / 1
            #reset running total of change needed
            changeNeeded = remainder

        if changeNeeded >= .25:
            #this finds remainder for needed change in quarters
            remainder = changeNeeded % .25
            #this subtracts the remainder from change needed in order to find divisible amount to find number of denominations
            total = changeNeeded - remainder
            #determine number of quarters required
            quarters = total / .25
            #reset running total of change needed
            changeNeeded = remainder

        if changeNeeded >= .1:
            #this finds remainder for needed change in dimes
            remainder = changeNeeded % .1
            #this subtracts the remainder from change needed in order to find divisible amount to find number of denominations
            total = changeNeeded - remainder
            #determine number of dimes required
            dimes = total / .1
            #reset running total of change needed
            changeNeeded = remainder

        if changeNeeded >= .05:
            #this finds remainder for needed change in nickels
            remainder = changeNeeded % .05
            #this subtracts the remainder from change needed in order to find divisible amount to find number of denominations
            total = changeNeeded - remainder
            #determine number of nickels required
            nickels = total / .05
            #reset running total of change needed
            changeNeeded = remainder

        if changeNeeded >= .01:
            #this finds remainder for needed change in pennies
            remainder = changeNeeded % .01
            #this subtracts the remainder from change needed in order to find divisible amount to find number of denominations
            total = changeNeeded - remainder
            #determine number of pennies required
            pennies = total / .01
            #reset running total of change needed
            changeNeeded = remainder

        self.twenties = twenties #assigns value twenties to property self.twenties
        self.tens = tens #assigns value tens to property self.tens
        self.fives = fives #assigns value fives to property self.fives 
        self.ones = ones #assigns value ones to property self.ones
        self.quarters = quarters #assigns value quarters to property self.quarters
        self.dimes = dimes #assigns value dimes to property self.dimes
        self.nickels = nickels #assigns value nickels to property self.nickels
        self.pennies = pennies #assigns value pennies to property self.pennies

def main():
    wmMain = WindowMain()   # Have the main function call your class App to start the GUI


if __name__ == "__main__": #check if the system variable name is equal to main
    main() #call main function