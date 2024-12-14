
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


class IceCreamGuiMainPage:

    def __init__(self, master):

        self.iceCreamMainPage= Frame(master)

        self.iceCreamMainPage.grid(row=0, column=0, sticky= "NSEW")

        global welcomeIMG       #Allows welcome image to be used.

        self.totalPrice = 0.0

        self.orderList = []     #Creates a list for items purchased 

        self.order = ()

        self.priceList = []      #Creates a list of prices of combos sold

        self.reciptList = {}     #Creates a dictionary of order tuples with the price as a value.

        global thankYouPhotoIMG  #Allows for thank you photo to be used

        thankYouPhotoIMG = ImageTk.PhotoImage(Image.open("Desktop\\Ice Cream Shop\\thankYou.jpg")) 

        self.thankyouPhotoImg = thankYouPhotoIMG

        self.x = 0


        #Creating a introductory label.

        welcomeLabel = Label(self.iceCreamMainPage, text= "Home of the world's best ice cream")

        self.nameOutputLabel = Label(self.iceCreamMainPage, text= '')

        self.nameOutputMarket = Label(self.iceCreamMainPage, text= "Order Name: ")

        self.orderOutPut = Label(self.iceCreamMainPage, text= ' ')

        self.currenOrderLabel = Label(self.iceCreamMainPage, text= "Latest order: ")

        self.orderLabel = Label(self.iceCreamMainPage, text= "Price: ")

        self.priceOutput = Label(self.iceCreamMainPage, text= self.totalPrice)

    

       

        #Creates main page buttons

        startOrderButton = Button(self.iceCreamMainPage, text= "Start Order", width= 8, command= self.openMenu)

        startOrderButton.config(bg= 'red', width= 10)

        enterNameButton = Button(self.iceCreamMainPage, text= "Enter Name", width= 8, command= self.openEnterName)

        enterNameButton.config(bg= "Green", width= 10)

        exitButton = Button(self.iceCreamMainPage, text= "Exit", command= root.destroy)

        exitButton.config(bg= "black", fg= "white", width= 10)

        resetOrderButton = Button(self.iceCreamMainPage, text= "Reset Order", command= self.resetOrder)

        resetOrderButton.config(width= 10)

        confirmOrderButton = Button(self.iceCreamMainPage, text= "Confirm Order")

        confirmOrderButton.config(width= 10, command= self.confirmOrder)




        #Gives the file location to the welcome impage and opens it.

    

        welcomeIMG = ImageTk.PhotoImage(Image.open("Desktop\\Ice Cream Shop\\ice1.jpg"))

        welcomeIMGLabel = Label(self.iceCreamMainPage,image= welcomeIMG)

        welcomeIMGAltText = Label(self.iceCreamMainPage, text= "(This in an image of ice cream  with a welcome to the shop program text above it)")

        welcomeIMGAltText.configure(font= "algerian")





        #Placing widgets in front page


        welcomeLabel.grid(row=0, column=0, columnspan= 5, sticky= "NSEW")

        welcomeIMGLabel.grid (row=1, column= 0, columnspan= 5)

        welcomeIMGAltText.grid(row=2, column=0, columnspan= 5)

        startOrderButton.grid(row= 3, column= 1)

        enterNameButton.grid(row= 3, column= 0)

        exitButton.grid(row= 3, column= 4)

        resetOrderButton.grid(row= 3, column= 2)

        confirmOrderButton.grid(row= 3, column= 3)

        self.nameOutputLabel.grid(row=4, column=1)

        self.nameOutputMarket.grid(row= 4, column= 0)

        self.priceOutput.grid(row=5, column= 1)

        self.orderLabel.grid(row= 5, column= 0)

        self.orderOutPut.grid(row= 6, column= 1, columnspan= 4)

        self.currenOrderLabel.grid(row=6, column= 0)

        



    #Creates the function for buttons 

    def openEnterName(self):

        #Creates function that opens name entry window when button is pressed.

        self.enterNameWindow = nameEntryWindow(self.getOrderName)  #Passes getOrderName function to nameEntryWindow class

        
    def getOrderName(self,orderName):

        #This receives an order name from the nameEntry class and outputs the name to the main menu
        
        self.nameOutputLabel.configure(text= orderName)


    def openMenu(self):

        #Creates function that opens the Ice Cream Menu window
        
        self.enterOrderMenu = IceCreamMenu(self.getOrderInfo)  #Opens ice cream menu and passed the get order info function to it.


    def getOrderInfo(self, orderInfo, r, f, T):

        #This function recieves the price, flavor, container, and topping and places them in a list and dictionary. This calcuates the total price with each incoming order
        #It then outs puts the latest order and the current total price to the main menu.
        
        self.order = (r, f, T)  #Creates a tupple for an order.

        self.x = int(self.x)
                               #This generates an order number that is used to differentiate orders that ordered the same thing.
        self.x = self.x + 1

        self.reciptList.update({(r,f,T,self.x): orderInfo})

        self.priceList.append(self.order)

        self.orderList.append(self.order)

        self.totalPrice = float(self.totalPrice)

        self.totalPrice += orderInfo                    #Adds price of an ice cream combo to the total bill

        self.orderOutPut.configure(text= "Your current item is a " + f + ' in a ' + r + ' with ' + T)

        self.priceOutput.configure(text="$%.2f" % self.totalPrice)

    def resetOrder(self):

        #Creates function for a button that resets the price and items


        self.orderList.clear

        self.totalPrice = 0

        self.priceOutput.configure(text= "%.2f" % self.totalPrice)     #Adjusts the main menu page

        self.orderOutPut.config(text= ' ')                             #Removes the last item ordered from menu.

    def confirmOrder(self):

        #Creates a function that brings up a page that asks the uesr if they would like to confirm their order and will either close the page or bring up a thank you message based on the answer
        
        finalPage = Toplevel()

        self.confirmationPage = Frame(finalPage)
    
        self.confirmationPage.grid(row=0, column=0)

        self.confimationLabel = Label(self.confirmationPage, text= ' ')    
                                                                        #Creates a place holder for confirmation message.
        self.confimationLabel.grid(row=1, column= 0, columnspan= 5)  

        self.custOrder = Label(self.confirmationPage, text= self.orderList)
        
        oC = messagebox.askquestion(self.confirmationPage, "Would you like to place your order?")   #Prommpts the user to confirm or deny the ordre placed
        
        if oC == 'yes':        #Geneates a thank you message if yes

            self.confimationLabel.configure(text= "Thank you for your order.  \n Your total is: " + str(self.totalPrice) + " Your wait will be about 15 minutes.")

            thankYouIMGSpace = Label(self.confirmationPage, image= self.thankyouPhotoImg)

            thankYouIMGSpace.grid(row=2, column=0, columnspan= 5)

            thankYouIMGSpaceAltText = Label(self.confirmationPage, text= "(This picture is on an ice cream cone with thank you over the ice cream)")

            thankYouIMGSpaceAltText.grid(row= 4, column= 0, columnspan= 5)

            thankYouIMGSpaceAltText.configure(font= "algerian")
                                            
    
            self.iceCreamMainPage.destroy()       #Closes main page

            



        if oC == 'no':
            self.confirmationPage.destroy()       #Closes confirmation page

        


        

            



        
        

        
class nameEntryWindow():

    #Creates the class for the name entry window

    def __init__(self, orderName):

        #Creates the framework for the name entry widow

        page1 = Toplevel()

        self.nameEntry = Frame(page1)

        self.nameEntry.grid(row=0, column= 0) 

        self.getorderName = orderName 

        #Create lables and entry box for user to enter their name

        nameEntryPromptLabel = Label(page1, text= "Please enter the name for your order. ")

        self.orderName = StringVar()                 #Formats the variable so that it is able to be received from get()

        nameEntryBox = Entry(page1, bg= "white", textvariable= self.orderName)            #Creates an entry box for user to input their name

        nameEntryBox.insert(0, "Name Here")        #Adds name here to highlight box for user.


        #Creates buttons for name entry page

        submitButton = Button(page1, text= "Submit", command= self.myclick)

        backButton = Button(page1, text= "Back", command= page1.destroy)



        #Placing widgets

        nameEntryPromptLabel.grid(row= 0, column= 0)

        nameEntryBox.grid(row=0, column= 1)

        submitButton.grid(row=1, column=1)

        backButton.grid(row= 1, column= 0)

    #Creating functions for entry box and buttons

    def myclick(self):
            
            #Creates function for submit button to submit name.

            self.getorderName(self.orderName.get())


        

class IceCreamMenu():

    #Creates a class for the Ice Cream Menu

    def __init__(self,orderInfo):

        #Creates framework for ice crea menu window
        
        page2 = Toplevel()

        self.page2 = page2

        self.IceCreamMenu = Frame(page2)

        self.IceCreamMenu.grid(row= 0, column= 0)

        self.getorderInfo = orderInfo

        self.orderInfo = 0.0

        self.container = StringVar()    #Formats variable so it can be used in a get().

        self.containerPrice = 0.0

        self.flavorPrice = 0.0

        self.toppingPrice = 0.0

     

        self.r= StringVar()               #Value for containers
        self.r.set("Regular Cone")

        self.f = StringVar()              #Value for flavors
        self.f.set("Vanilla")

        self.T = StringVar()              #Value for toppings
        self.T.set("No Toppings")

        

        def pickedContainer(value):

            #This creates a function for the radio buttons to give a value back and outputs the highligted one

            containerLabel = Label(page2, text=value)
            containerLabel.grid(row=7, column= 0)
            
        def pickedFlavor(value):

            #This creates a function for the radio buttons to give a value back and outputs the highligted on

            flavorLabel = Label(page2, text=value)
            flavorLabel.grid(row=7, column= 1)


        def pickedTopping(value):

            #This creates a function for the radio buttons to give a value back and outputs the highligted one


            toppingLabel = Label(page2, text= value)
            toppingLabel.grid(row=7, column= 2)


        #Sets up the headers for the radio buttons and general header

        header = Label(page2, text= "Menu")

        containerHeader = Label(page2, text= "Choose a container")

        flavorHeader = Label(page2, text= "Choose a Flavor")

        toppingsHeader = Label(page2, text= "Choose your topping")

        #Creates the radio buttons for each columns


        firstContainerBTN = Radiobutton(page2, text="Regular Cone: $0.99" , variable= self.r, value= "Regular Cone", command= lambda: pickedContainer(self.r.get()))

        secondContainerBTN = Radiobutton(page2, text= "Waffle Cone: $2.99", variable= self.r, value= "Waffle Cone", command= lambda: pickedContainer(self.r.get()))

        thirdContainerBTN = Radiobutton(page2, text= "Regular Bowl: $1.50", variable= self.r, value= "Regular Bowl", command= lambda: pickedContainer(self.r.get()))

        firstFlavorBTN = Radiobutton(page2, text= "Vanilla: $1.00", variable= self.f, value= "Vanilla", command= lambda: pickedFlavor(self.f.get()))

        secondFlavorBTN = Radiobutton(page2, text= "Chocolate: $1.00", variable= self.f, value= "Chocolate", command= lambda: pickedFlavor(self.f.get()))

        thirdFlavorBTN = Radiobutton(page2, text= "C:S Swirl: $1.00", variable= self.f, value= "C:S Swirl", command= lambda: pickedFlavor(self.f.get()))

        firstToppingsBTN = Radiobutton(page2, text= "No Toppings: $0.00", variable= self.T, value= "No Toppings", command= lambda: pickedTopping(self.T.get()))

        secondToppingsBTN = Radiobutton(page2, text= "Choc Syrup: $0.99", variable= self.T, value= "Choc Syrup", command= lambda: pickedTopping(self.T.get()))

        thirdToppingsBTN = Radiobutton(page2, text= "Sprinkles: $0.50", variable= self.T, value= "Sprinkles", command= lambda: pickedTopping(self.T.get()))

        fourthToppingsBTN = Radiobutton(page2, text = "Cookie Crumble: $2.00", variable= self.T, value= "Cookie Crumble", command= lambda: pickedTopping(self.T.get()))



        #Adds butons for back and place order


        addtoOrderBTN = Button(page2, text= "Add to Order",command= self.addToOrder)

        backBTN = Button(page2, text= "Back", command= page2.destroy)

        backBTN.configure(width= 10, bg= "Red", fg= "black")

        addtoOrderBTN.configure(width= 10, bg= "Green")



        #Places Widgets onto the grid

        header.grid(row= 0, column= 0, columnspan= 4)

        containerHeader.grid(row=1, column= 0)

        flavorHeader.grid(row=1, column= 1)

        toppingsHeader.grid(row=1, column= 2)

        firstContainerBTN.grid(row=2, column= 0)

        secondContainerBTN.grid(row=3, column=0)

        thirdContainerBTN.grid(row=4, column= 0)

        firstFlavorBTN.grid(row= 2, column= 1)

        secondFlavorBTN.grid(row= 3, column= 1)

        thirdFlavorBTN.grid(row= 4, column= 1)

        firstToppingsBTN.grid(row=2, column= 2)

        secondToppingsBTN.grid(row=3, column= 2)

        thirdToppingsBTN.grid(row= 4, column= 2)

        fourthToppingsBTN.grid(row=5, column= 2)

        backBTN.grid(row=9, column= 0)

        addtoOrderBTN.grid(row=9, column=2)



    def addToOrder(self):
            
        #This generates the name of each item in the indidual item, calculates a price for the combo, and then sends the info to the mainpage.
            container = self.r.get()
            flavor = self.f.get()
            topping = self.T.get()

        #Obtains the prices of the items in a combo based on teh value selected in the radio button
        #  
            if container == "Regular Cone":
                self.containerPrice = 0.99
            if container == "Waffle Cone":
                self.containerPrice = 2.99
            if container == "Regular Bowl":
                self.containerPrice = 1.50

            if flavor == "Vanilla":
                self.flavorPrice = 1.00
            if flavor == "Chocolate":
                self.flavorPrice = 1.01
            if flavor == "C:S Swirl":
                self.flavorPrice = 1.02

            if topping == "No Topping":
                self.toppingPrice = 0.0
            if topping == "Choc Syrup":
                self.toppingPrice = 0.99
            if topping == "Sprinkles":
                self.toppingPrice = 0.50
            if topping == "Cookie Crumble":
                self.toppingPrice = 2.00

            self.containerPrice = float(self.containerPrice)
                                                              
                                                              #Formats values for total price calculation
            self.flavorPrice = float(self.flavorPrice)

            self.orderInfo = self.toppingPrice + self.containerPrice + self.flavorPrice

            orderLabel = Label(self.page2, text= "Your order will be " + str(self.orderInfo))    #Gives price of last added item.

            orderLabel.grid(row= 10, column= 0) 
    
            
            self.container.get()
            self.getorderInfo(self.orderInfo, self.r.get(), self.f.get(), self.T.get())
            



root = Tk()
IceCreamGuiMainPage(root)
root.mainloop()