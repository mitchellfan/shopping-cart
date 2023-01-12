#-------------------------------------------------------------------------------
# Final Project CLASS
# Student Name: Mitchell Fan 
# Submission Date: 12/4/20222
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: For the file reading, I had to use an absolute path for my script to work. Originally it was 'AppleStoreApps.csv' in line 79 and 80.
#-------------------------------------------------------------------------------
# Your source code below
#-------------------------------------------------------------------------------

import csv

#your code here
#define a class SmartCart - a subclass of list class
#define a subtotal function
#Returns subtotal from a SmartCart list object
class SmartCart(list):

    def subtotal(self):
        total = 0
        for item in self:
            total += float(item.get_price())
        return total

    
class Item(object):
    '''Item class defines an app item
    available in store. App object saved in
    category_dict per category
    and rating_dict per rating'''
    category_dict = {}
    rating_dict = {1:[], 2:[],3:[],4:[],5:[]} #rating from 1 to 5
    

    def __init__(self, ID, track_name, price, rating, category):
        '''Initialization method'''
        self.__id = ID
        #your code here
        #initialize name, price, rating and category as private method
        self.__name = name
        self.__price = price
        self.__rating =  rating
        self.__category = category
        
        #populate dict by category - key = category and values = list of app objects
        if self.__category in Item.category_dict.keys():
            #your code here
            #append object to current category
            Item.category_dict[self.__category].append(self)
        else:
            #your code here
            Item.category_dict[self.__category] = [self]
        
        if float(self.__rating) <2:
            Item.rating_dict[1].append(self)
        elif float(self.__rating) <3:
            Item.rating_dict[2].append(self)
        elif float(self.__rating) <4:
            Item.rating_dict[3].append(self) 
        elif float(self.__rating) <5:
            Item.rating_dict[4].append(self)
        elif float(self.__rating) == 5:
            Item.rating_dict[5].append(self)

    #your code here
    #define get methods
    #to return all private attributes
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_rating(self):
        return self.__rating
    
    def get_category(self):
        return self.__category

#process file - creating Item app object
absolute_path = r"C:\Users\Mitchell\Documents\GMU\IT 209\AppleStoreApps.csv"
with open(absolute_path) as fin:
    apps = csv.reader(fin, delimiter = ',')
    for row in apps:
        ID, name, price, rating, category = row
        i = Item(ID, name, price, rating, category)
        


'Testing code to check object creating Items Comment out when done'

#prints all the app's name and rating from
#category dict

for k,v in Item.category_dict.items(): #v is a list of all objects
    print(k, [(obj.get_name(), obj.get_rating()) for obj in v ])
print('++++++++++')

#print all apps name from rating dict
for k,v in Item.rating_dict.items(): #v is a list of all objects
    print(k, [obj.get_name() for obj in v ])
print('++++++++++')





          

