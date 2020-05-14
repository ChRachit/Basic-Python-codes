""""#leap year
while True:
    year = int(input("Enter a year to check if its a leap year: "))
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a leap year!")
        else:
            print(str(year) + " is not a leap year!")
    elif year % 4 == 0:
        print(str(year) + " is a leap year!")
    elif year % 4 != 0:
        print(str(year) + " is not a leap year!")"""

"""#program to calculate number of average squats in a week :)
days = 1
total = 0
while days <= 7:
    squats = float(input("Squats on Day " + str(days) + ': '))
    total = total + squats
    days = days + 1
    
average = total/7
print('You did ' + str(average) + ' squats on average everyday!')"""

"""#table program
i=1
table = int(input("Enter the number to get its table: "))
upper_limit = int(input("Enter the upper limit for table: "))
while i <= upper_limit : 
    print( str(table) + ' * ' + str(i) + ' = ' + str(table * i))
    i= i + 1"""

"""#factorial program
fact = 1
number = int(input("Enter a Number to find its factorial: "))
for i in range(1, number + 1):
    fact = fact * i
print(fact)"""

"""#prime number
number = int(input("Input a number to chech if its prime: "))
for num in range(2, number):
    if number % num == 0:
        print(str(number) + " is not prime!")
        break
else:
    print(str(number) + " is " + "PRIME!")"""

"""#prime factors
number = int(input("Input a number to chech if its prime factors: "))
div = 2
while number > 1:
    if number % div == 0:
        print(div)
        number = number/div
        continue
    div = div + 1"""

"""#getter and setter and classes
class car:
    counter = 0
    def __init__(self, speed = 0, colour = "White", power = '100 bhp'):
        self.speed = speed
        self.colour = colour
        self.power = power
        car.counter = car.counter + 1
    def get_info(self):
        print("This car has: \n")
        print("Speed: {}".format(self.speed))
        print("Colour: {}".format(self.colour))
        print("Power: {}".format(self.power))
        
        @classmethod
        def show_count(cls):
            print("The class car has been called {} times!".format(cls.counter))"""

#operator overloading with feet and inches calculatar class
"""
class distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        
    def __add__(self, other):
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches
        if total_inches >= 12:
            total_feet = total_feet + 1
            total_inches = total_inches - 12
            return distance(total_feet, total_inches)
        
    def __str__(self):
        return "Total is " + str(self.feet) + " feet and " + str(self.inches) + " inches."

#inhertance
    
class subtractor(distance):
        
    def __sub__(self, other):
        total_inches = (self.feet * 12 + self.inches) - (other.feet * 12 + other.inches)
        final_feet = total_inches / 12
        final_inches = total_inches % 12
        return subtractor(final_feet, final_inches)"""
"""#Exception handling

import sqlite3
MySchool=sqlite3.connect('schooltest.db')
        
mysid= int(input("Enter ID: "))
myname=input("Enter name: ")
myhouse=int(input("Enter house: "))
mymarks=float(input("Enter marks: "))
        
#try block to catch exceptions
try:
    curschool=MySchool.cursor()
    curschool.execute("INSERT INTO student (StudentID, name, house, marks) VALUES (?,?,?,?)", (mysid, myname, myhouse, mymarks))
    MySchool.commit()
    print ("One record added successfully.")
    
#except block to handle exceptions    
except:
    print ("Error in operation.")
    MySchool.rollback()
        
MySchool.close()"""

"""import sqlite3
MySchool = sqlite3.connect('schooltest.db')
curschool = MySchool.cursor()

curschool.execute(''' CREATE TABLE students( sid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT (20) NOT NULL, marks REAL);''')
MySchool.close()"""

#widget GUI
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        btn = QPushButton("Hello World!", self)
        btn.move(50,75)
        self.setGeometry(100, 100, 200,150)
        self.setWindowTitle('PyQt Window')
        self.show()
                
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    


    
