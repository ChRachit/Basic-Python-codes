def book_description(author, book_type = 'fiction'):
    print("\n This book is " + book_type.title() + '.')
    print(" The Author of " + book_type.title() + ' is ' + author.title() + '.')

#1Return value
def formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name+ ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

def get_email(username):
	email = username.strip()
	return email
    
#2Returning dictionary
def build_book(name, author, publisher):
	book_info = {'name' : name, 'author' : author, 'publisher' : publisher}
	return book_info

#3 While loop
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\nHello, Please Enter your name ')
    print(" ( Press 'q' to stop. ) ") 
    first_name = input('\n First Name: ')
    if first_name == 'q':
    	break
    last_name = input(' Last Name: ')
    if last_name == 'q':
    	break
    formatted = get_formatted_name(first_name, last_name)
    print('\n Hello! ' + formatted + '.')

#Modifying list within a function
#passengers Function
"""transfering list of passengers from not checked in to checked in then displaying the names"""
"""uses two lists checked in and not checked in as parameters"""
def passengers(not_checked_in, checked_in):
	while not_checked_in:
		current_passenger = not_checked_in.pop()
		print("Checking in passenger: " + current_passenger.title())
		checked_in.append(current_passenger)



def checked_in_passengers(checked_in):
    print('\nThe following have been checked in:- ')
    for passengers in checked_in:
        print(passengers.title())
"""sample input		 
not_checked_in = ['rachit tiwari', 'md saif', 'tushar pandey']
checked_in = []"""

#Making a copy of list and keeping the original
"""using slice function to send the copy of the list and not modifying the original"""
#list_name[:]
#passengers(not_checked_in[:], checked_in)

#aribtrary/multiple parameters in a function
#Note :- arbitrary arguments must be last in order to non-arbitrary
"""Put an astriek '*' in the parameter"""
def passenger(*request):
    print(requests)
#with more functionality with for loop
def passenger_requests(*requests):
     print('The passenger has requested:- ')
     for request in requests:
         print('\n' + request)
"""to import a module save only the functions and use import module
   like import temp"""
#Note :- to import a particular function/multiple function from a module
#use from module import function1,function2,...

#giving an alias to a function/module
"""from temp import passenger_requests as pr
>>> pr(holy, shit)"""
#for module
#import temp as t
#to import all the functions use *
#from temp import *

#object oriented programming
#creating a book information class

class book():
	def __init__(self, name, price, publisher):#for self refrencing use init
		self.name = name
		self.price = price
		self.publisher = publisher
		
	def hardcopy(self):
		print(self.name.title() + " is in Hardcopy")
		
	def ebook(self):
		print(self.name.title() + " is an Ebook")
		
	def price(self):
		print(self.name.title() + " has a price " + self.price)

#creating an instance of class book
my_book = book('elon musk', 300, 'virgin books')

#ereader class
class Ereader():
	"""Making an ereader class"""
	def __init__(self, make, model, backlight, battery_life):
		#initialize attributes to describe an ereader
		self.make = make
		self.model = model
		self.backlight = backlight
		self.battery_life = battery_life

	def get_ereader_name(self):
		#Return a formatted decsription of the ereader
		name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery_life + '.'
		return name.title()

#sample input
"""my_ereader = Ereader('amazon kindle', 'paperwhite', 'white', '10 hours')
    print(my_ereader.get_ereader_name())"""
#output
#Amazon Kindle - Paperwhite - White - 10 Hours.
class Ereader():
	"""Making an ereader class"""
	def __init__(self, make, model, backlight, battery_life):
		#initialize attributes to describe an ereader
		self.make = make
		self.model = model
		self.backlight = backlight
		self.battery_life = battery_life
		self.library_count = 0 #default attribute value doesnt need to be initialized in function(init) parameter!

	def get_ereader_name(self):
		#Return a formatted decsription of the ereader
		name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery_life + '.'
		return name.title()

	def get_library_count(self):
		#Display the number of books in a library
		print('You have ' + str(self.library_count) + ' books in your library.')
		
	def update_lib_count(self,new_count):
	    #changing default attributes through a method
	    self.library_count = new_count
	    return self.library_count
	    
	def increment_lib_count(self,increment):
	    #adding new books to our library
	    self.library_count += increment

#sample input	    
"""my_ereader = Ereader('amazon kindle', 'paperwhite', 'white', '10 hours')
print(my_ereader.get_ereader_name())
my_ereader.update_lib_count(3)#updating attributes via a method call by passing the updated value
my_ereader.increment_lib_count(9)#adding new books purchased
my_ereader.get_library_count()"""

#inheritance
class Kindle_fire(Ereader):#inheriting from parent Ereader class
    def __init__(self, make, model, backlight, battery, screen_res = "1280 * 1080"): 
        #child attributes specific to kindle Kindle_fire
        self.screen_res = screen_res
        super().__init__(make, model, backlight, battery)#for superclass ie parent
    
    def describe_screen(self):
        #For printing out marketing text
        print("\nThis Kindle Fire features a " + self.screen_res + " Full HD display.")
        
#sample input       
"""my_fire = Kindle_fire("Amazon", "Kindle fire", "White backlight", "3000 mAh")
print(my_fire.get_ereader_name())
my_fire.describe_screen()"""
	   
#overriding a method
"""to override a method in child class use the same method name with properties
specific to the child class and py overrides the method"""
#eg to override describe_screen in another child class of kindle_class
# def describe_screen(self):
#    ......code.....

#ereader class with separate screen function
class Ereader():
	"""Making an ereader class"""
	def __init__(self, make, model, backlight, battery_life):
		#initialize attributes to describe an ereader
		self.make = make
		self.model = model
		self.backlight = backlight
		self.battery_life = battery_life
		self.library_count = 0 #default attribute value doesnt need to be initialized in function(init) parameter!

	def get_ereader_name(self):
		#Return a formatted decsription of the ereader
		name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery_life + '.'
		return name.title()

	def get_library_count(self):
		#Display the number of books in a library
		print('You have ' + str(self.library_count) + ' books in your library.')
		
	def update_lib_count(self,new_count):
	    #changing default attributes through a method
	    self.library_count = new_count
	    return self.library_count
	    
	def increment_lib_count(self,increment):
	    #adding new books to our library
	    self.library_count += increment
	    
	    
class Screen():
    #class to describe Screen description and functionality
    def __init__(self , screen_res = "1280 * 1080"):    
        #initialize screen attributes
        self.screen_res = screen_res
        
    def describe_screen(self):
        #For printing out marketing text
        print("\nThis Kindle Fire features a " + self.screen_res + " Full HD display.")
            

	   
#inheritance
class Kindle_fire(Ereader):
    def __init__(self, make, model, backlight, battery): 
        #child attributes specific to kindle Kindle_fire
        
        super().__init__(make, model, backlight, battery)
        self.fire_screen = Screen()
        
"""my_fire = Kindle_fire("Amazon", "Kindle fire", "White backlight", "3000 mAh")
print(my_fire.get_ereader_name())
my_fire.fire_screen.describe_screen()"""
#import single class as- from file import class
#import multiple class as- from file import class1, class2
#import entire module as- import file
#import all classes from module as- from file import *
#Files in py
#Note- Couldn't cover file handling thoroughly so brush up when you get a chance, Peace!
#Reading an entire file 
#directries should be same
"""with open('file_name.txt') as file_object:
    variable = file_object.read() #Creating a variable that reads the content
    print(variable.strip()) #using strip() to clear all whitespaces
    
#code to count number of words in a boook with FileNotFound exception
def wordcount(file_name):
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:#use 'pass' in except block to not print any error/fail silently
        message = "Yo cant get no book like " + file_name + "!"
        print(message)
    
    else:
        words = contents.split()
        number_words = len(words)
        print("This Bitch got around " + str(number_words) + " in it.")
    
print("\n----------Nine Nine Nigga-----------")"""
#sample input
#wordcount('gibberjabber.txt')

#using json.dump
#using json to create a new file with phone numbers
"""import json

phone = [1234567890]

filename = 'Phone_Number.json'

with open(filename, 'w') as file_object:
    json.dump(phone, file_object)

#using json.load to display a file with phone numbers
import json

filename = 'Phone_Number.json'

with open(filename) as file_object:
   phone = json.load(file_object)
print(phone)"""
