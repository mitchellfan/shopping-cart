#-------------------------------------------------------------------------------
# Final Project GUI
# Student Name: Mitchell Fan
# Submission Date: 12/4/20222
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: Line 145, changed "Add To Cart" to "Update Cart" because function is updating rather than just adding to the cart.
#-------------------------------------------------------------------------------
# Your source code below
#-------------------------------------------------------------------------------

#import tkinter
from tkinter import *
#import Item and SmartCart class from CLASS file
from Mitchell_Fan_final_project_CLASS import Item
from Mitchell_Fan_final_project_CLASS import SmartCart
from functools import partial
import random, string #used in random receipt no function

class MyFrame(Frame):
    current_subtotal = 0
    def __init__(self, root):
        '''Constructor method'''
        Frame.__init__(self, root) #Frame class initialization
        self.init_container() #initialize all widget containers
        self.cart = SmartCart() #initialize SmartCart dict object - key = Item object item selected, value = quantity
        self.welcome() #start the application
        self.data = StringVar(self, "Subtotal: 0.0") #Associated with subtotal label

        
    def init_container(self):
        '''Initialize widget containers'''
        self.states = [] #holds state if selected/not i-th list item holds selection for i-th item
 
    def clear_frame(self): 
        '''Clears the previous frame'''
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        '''Exits the program'''
        root.destroy()

 
    def welcome(self):
        '''Welcome window - refer spec file for details'''
        self.clear_frame()
        Label(self, text = '****Welcome to AppsCart!****', background="gray80").pack(side = TOP)
        #your code here
        #Select by category: Button – start ordering, command = shop_by_apps_category
        Button (self, text = "Select by Category", command = self.shop_by_apps_category).pack()
        #Select by rating: Button - start ordering, command = shop_by_apps_ratings
        Button (self, text = "Select by Ratings", command = self.shop_by_apps_ratings).pack()
        #Exit Application: Button – exit the program, command = exit_application
        Button (self, text = "Exit Application", command = self.exit_application).pack()

    def shop_by_apps_ratings(self):
        self.clear_frame()
        self.init_container()
        ratings = [1, 2, 3, 4, 5]  

    def shop_by_apps_category(self):
        '''2. Widget to display different category of apps - refer spec file for details'''
        self.clear_frame()
        self.init_container()
        categories = ["Games", "Productivity", "Weather", "Shopping", "Utilities", "Finance", \
                      "Travel", "Music", "Health & Fitness"]
        #your code here
        #Choose Apps Category: label
        #Iterate over each category in categories list
        #create a button for each category, set text = category and
        #command= partial(self.start,Item.category_dict[category])
        #partial is a special method to pass an argument during button command
        #layout button
        Label (self, text = "Choose Apps Category").pack(side = TOP)
        for category in categories:
            Button (self, text = category,  command = partial(self.start, Item.category_dict[category])).pack()
    
    def shop_by_apps_ratings(self):
        self.clear_frame()
        self.init_container()
        ratings = [1, 2, 3, 4, 5]

        Label (self, text = "Choose Apps Rating").pack(side = TOP)
        for rating in ratings:
            Button (self, text = rating,  command = partial(self.start, Item.rating_dict[rating])).pack()

        #Go Back: Button – command = welcome
        #layout manager for all the widgets
        Button(self, text = "Go Back", command = self.welcome).pack()


    def start(self, current_items):
        ''''3. Start ordering from selected category,
        list passed by command will be used as current_items'''
        self.clear_frame()
        self.init_container()
        
        #creating widgets for items using a for loop
        #iterative over each item of current apps and
        #create that many checkbutton, price, ID, rating and category label
        row = 0#########
        for item in current_items:
            self.states.append(IntVar()) #keeps track if an item is selected
            checkbutton = Checkbutton(self, text=item.get_name(), variable=self.states[row])#create check buttons
            checkbutton.grid(row = row, column = 0)

            #your code here
            #create and layout a price label, set text to item.get_price()
            #create and layout id label and set text to item.get_id() method
            #similary create and layout rating and category label 
            price_label = Label(self, text = "$" + item.get_price())
            price_label.grid(row = row, column = 1)
        
            id_label = Label(self, text = item.get_id())
            id_label.grid(row = row, column = 2)

            rating_label = Label(self, text = item.get_rating())
            rating_label.grid(row = row, column = 3)
            
            category_label = Label(self, text = item.get_category())
            category_label.grid(row = row, column = 4)

            row +=1

        
        #create and layout subtotal lable, set textvaribale = self.data so it changes
        self.subtotal_label = Label(self, textvariable = self.data, background="gray80")
        self.subtotal_label.grid(row = row + 1, column = 0)

        #create and layout select by categories: button, command = shop_by_apps_category
        self.select_by_categories_label = Button(self, text = "Categories", command = self.shop_by_apps_category)
        self.select_by_categories_label.grid(row = row + 1, column = 1)

        #create and layout select by ratings: button, command = shop_by_apps_ratings
        self.select_by_ratings_label = Button(self, text = "Ratings", command = self.shop_by_apps_ratings)
        self.select_by_ratings_label.grid(row = row + 1, column = 2)

        #create and layout add_to_cart_button, command = partial(self.add_to_cart, current_items)
        self.add_to_cart_button = Button(self, text = "Update Cart", command = partial(self.add_to_cart, current_items))
        self.add_to_cart_button.grid(row = row + 1, column = 3)

        #create and layout button: checkout, command = self.checkout
        self.checkout_button = Button(self, text = "Checkout", command= self.checkout)
        self.checkout_button.grid(row = row + 1, column = 4)


    def add_to_cart(self, current_items): #####
        '''3. Added to cart, displays subtotal - see spec file for details layout'''
    
        for i in range(len(current_items)):
            #your code here
            #get() the value of i-th item of self.states -> returns 1 if selected otherwise 0
            #if item is selected:
                #add app item object to self.cart list 
            if (self.states[i].get() == 1): 
                if not (current_items[i] in self.cart):
                    self.cart.append(current_items[i])
                    self.current_subtotal = self.cart.subtotal()
                    self.data.set ("Subtotal: ${:.2f}".format(float(self.current_subtotal)))
            
            else:
                if (current_items[i] in self.cart):
                    self.cart.remove(current_items[i])
                    self.current_subtotal = self.cart.subtotal()
                    self.data.set ("Subtotal: ${:.2f}".format(float(self.current_subtotal)))
            
        
        #your code here
        #set the StringVar to be the current subtotal (SmartCart object self.cart has subtotal method)
        #refer to class file
        
    def get_receipt_number(self):
        '''Generate random receipt number'''
        return  ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))

    def checkout(self):
        '''4. Check out window '''
        self.clear_frame()
        #your code here to create and layout following widgets:
        #refer to receipt frame
        #   Your e-order: Label
        eorder_label = Label (self, text = "Your e-order:", background = "gray80")
        eorder_label.grid(columnspan = 5)

        #   e-Order Number: Label - Randomly generated by program - text = get_receipt_number()
        eorder_number_label = Label (self, text = ("e-order Number:" + self.get_receipt_number()))
        eorder_number_label.grid(columnspan = 5)

        #	Name Price Rating Category: Header Label
        header_label = Label(self, text = "****************************************")
        header_label.grid(columnspan = 5, sticky = E + W)  
        
        #   Iterate over apps items from cart list
        name_label = Label(self, text = ("Name"))
        name_label.grid(row = 5, column = 0)

        price_label = Label(self, text = ("Price"))
        price_label.grid(row = 5, column = 1)

        rating_label = Label(self, text = ("Rating"))
        rating_label.grid(row = 5, column = 2)

        genre_label = Label(self, text = ("Genre"))
        genre_label.grid(row = 5, column = 3)

        #	Generate labels of name, price, rating, category and layout
        row = 6
        for item in self.cart:
            get_name_label = Label(self, text = (item.get_name()))
            get_name_label.grid(row = row, column = 0, sticky = E + W)
            
            get_price_label = Label(self, text = (item.get_price()))
            get_price_label.grid(row = row, column = 1)
            
            get_rating_label = Label(self, text = (item.get_rating()))
            get_rating_label.grid(row = row, column = 2)
            
            get_category_label = Label(self, text = (item.get_category()))
            get_category_label.grid(row = row, column = 3)
            row += 1

        #	Subtotal: Label - get self.cart subtotal - new label 
        subtotal_label = Label(self, text = ("Subtotal: ${:.2f}".format(float(self.cart.subtotal()))))
        subtotal_label.grid(columnspan = 5, sticky = E + W)

        #	Tax: Label - 4.3%
        tax_label = Label(self, text = "Tax: 4.30%")
        tax_label.grid(columnspan = 5, sticky = E + W)

        #	Total: Label - subtotal + tax
        total_label = Label(self, text = "Total: ${:.2f}".format(float(self.cart.subtotal())*0.043 + self.cart.subtotal()))
        total_label.grid(columnspan = 5, sticky = E + W)

        #	‘Thank you’ message: Label
        thank_you_label = Label(self, text = ("Thank You For Using AppsCart"))
        thank_you_label.grid(columnspan = 5, sticky = E + W)

        #	Exit application: Button – exit the program- command = exit_application
        footer_label = Label(self, text = "****************************************")
        footer_label.grid(columnspan = 5, sticky = E + W)
        
        exit_label = Button(self, text = "Exit Application", command = self.exit_application)
        exit_label.grid(columnspan = 5)

#main driver code
#your code here
#create root window
root = Tk()
root.geometry("600x400")
root.title("Apps Cart") #set window title

#your code here
#create a myframe object and layout
frame = MyFrame(root)
frame.grid()

#call mainloop
root.mainloop()
