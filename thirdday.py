#write a python code on book system 
#make the function and store the data in the dictionary atleast five books 
def book_system ():
    book_shop = {
        1: "The Great Gatsby by F. Scott Fitzgerald",
        2: "To Kill a Mockingbird by Harper Lee",
        3: "1984 by George Orwell",
        4: "Pride and Prejudice by Jane Austen",
        5: "The Catcher in the Rye by J.D. Salinger"
    }
    a = input("Enter the book number you want to pick  ")

    if a.isdigit():
        a = int(a)
        if a in book_shop:
            return f"You have selected: {book_shop[a]}"
        else:
            return "Book number not found. Please select a number between 1 and 5."
    else:
        return "Invalid input. Please enter a valid book number."
    
print(book_system())
# if number in books checks if ther match or not 
def books_system():
    dicti = {
        1: "atomic habits",
        2: "the lost boy",
        3: "GOT",
        4: "Black sails",
        5: "Art of war"
    }
    num = int(input("Enter the Book number you want to read "))
  
    if num in dicti:
          print(f"You have selected: {dicti[num]}")
    else:
         print(f"Book number not found enter a number between 1 and 5")
books_system()
#you can import a function from another file and use it using import keyword
import second_day
second_day.operations(12,2)

#random module its used to generate random numbers or select random items from a list 
import random
print("Random number between 1-10:",random.randint(1,10))
colors = ["red","blue","green","yellow","black"]
print("Random color:",random.choice(colors))

#import datetime module its used to work with date and time
import datetime
now = datetime.datetime.now()
print("Current date and time:",now)
print("Current year:",now.year)
print("Current month:",now.month)
print("Current day:",now.day)
print("Current hour:",now.hour)
print("Current minute:",now.minute)
print("Current second:",now.second)
#for current date use datetime.date.today()
today = datetime.date.today()
print("Today's date:",today)

#import sys module its used to work with system specific parameters and functions
import sys
print("Python version:",sys.version)
print("Platform:",sys.platform)

#import math
import math
print("Square root of 16:",math.sqrt(16))
print("Value of pi:",math.pi)
print("Value of e:",math.e)
print("Ceiling of 4.2:",math.ceil(4.2))
print("Floor of 4.7:",math.floor(4.7))
print("Factorial of 5:",math.factorial(5))
print("Logarithm of 1000 base 10:",math.log10(1000))
print("Sine of 90 degrees:",math.sin(math.radians(90)))
print("Cosine of 0 degrees:",math.cos(math.radians(0)))
print("Tangent of 45 degrees:",math.tan(math.radians(45)))
print("5 bitwise AND 3:",5 & 3)  # 0101 & 0011 = 0001 = 1
print("5 bitwise OR 3:",5 | 3)   # 0101 | 0011 = 0111 = 7
print("5 bitwise XOR 3:",5 ^ 3)  # 0101 ^ 0011 = 0110 = 6
print("Bitwise NOT of 5:",~5)     # ~0101 = 1010 (in 2's complement) = -6
print("5 left shifted by 1:",5 << 1) # 0101 << 1 = 1010 = 10
print("5 right shifted by 1:",5 >> 1) # 0101 >> 1 = 0010 = 2

#import os module its used to interact with operating system
import os
print("Current working directory:",os.getcwd())
print("List of files and directories in current directory:",os.listdir('.'))
#string methods and operators
str1 = " Hello, World! "
print("Original string:",str1)
print("Length of string:",len(str1))
print("Uppercase string:",str1.upper())
print("Lowercase string:",str1.lower())
print("Stripped string:",str1.strip())
print("Replaced string:",str1.replace("World","Python"))
print("Split string:",str1.split(","))
print("Substring 'World' found at index:",str1.find("World"))
print("Is alphanumeric:",str1.isalnum())
print("Is alphabetic:",str1.isalpha())
print("Is digit:",str1.isdigit())
print("Is lowercase:",str1.islower())
print("Is uppercase:",str1.isupper())

#task 
# create a function take random values using random module 
#check if the value is even or odd 
#check if the value is divisible with 5 or not 
import random
def rand():
    number = random.randint(-50,100)
    if number %2 == 0:
          print(f"Number {number} is Even")
    else:
         print(f"Number {number} is Odd")
    if number > 0 :
         print(f"Number {number} Is +ve")
    else:
         print(f"Number {number} Is -ve")
    if number %5 == 0:
         print(f"Number {number} is divisible by 5")
    else:
         print(f"Number {number} is Not divisible by 5")
rand()
#class and objects 
class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def get_info(self):
        return f"{self.title} by {self.author}, published in {self.year}, ISBN: {self.isbn}"
# Creating book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "9780743273565")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "9780061120084")
 
#create calss named as Rectangle with attributes length and width
#there is method named as area which returns area of rectangele 
#get input from the user for a and b 
class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
a = int(input("Enter the length of rectangle "))
b = int(input("Enter the width of rectangle "))
rect = rectangle(a,b)
print(f"The area of rectangle is {rect.area()}")
