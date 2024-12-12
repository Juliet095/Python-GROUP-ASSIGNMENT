# #A python function named calculate_area takes the radius of a circle as a parameter
# #  returns the area of the circle
def calculate_area (the_radius_of_a_circle):
    if(the_radius_of_a_circle > 0):
         pie = 3.14
         result = pie * (the_radius_of_a_circle)**2
         print(result)
    else:
         result = 0
         return result
         print('The area is')
         calculate_area (5)

# #Define a python class named "Book" with attributes title author and pages 
# # Provide a method in class to display information about the book. Create an instance of the class to display the info.
# # create a derieved class EBook that inherits from Book class.
class Book(): #class
     def _init_(self, author, pages):
         self.author = author#Attributes
         self.pages = pages #Attributes
     def about_the_book(self): #nethod
         print(f"The author is{self.author} and the pages are {self.pages}")
Book1 = Book(author="Daniela", pages=33)#Instance or object
print(Book1.about_the_book())
class Ebook(Book): 
     def _init_(self, author, pages):
         super()._init_(author, pages)
x=Ebook("Micheal", 44)
x.about_the_book()

# #Define a python class named "Car" with attributes brand and year .
# # Provide a method in class to display info about the car.
# # Create an instance of the class and display the information.
class Car():
     def _init_(self, brand, year):
         self.brand = brand
         self.year = year
     def car_details(self):
         print(f"The car is {self.brand} made in {self.year}")
Car1 = Car(brand="Lexus", year=2021)
Car2 = Car(brand="Harrier", year=2020)
print(Car1.car_details())
print(Car2.car_details())

# #Write a python program function that taks parameters a and b and returns their sum. test the 
# #function the values a = 3, b=4
def sum_of_two_numbers(a, b):
     return a + b
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

sum_of_two_numbers(a=3, b=4)
print("Sum is {0}".format(sum_of_two_numbers(a , b)))

# #Write a python program that prints the folowing pattern
# #1, 1,2,,,1,2,3,,,1,2,3,4,,,1,2,3,4,5
numbers = int(input("Enter number of rows:"))
for i in range (1, numbers+1):
    for j in range (1,i+1):
        print(j,end="")

    print()
# For repeated numbers change print(j,end="") change j to i

#Write a recursive function to calculate the factorial of a given number n test the function with n= 5.
def fact_of(n):
     if n==0:
         return 1
     elif n==1:
         return 1
     else:
         return n*fact_of(n-1)
print(fact_of(5))

# #Write a python code snippet that asks the user for their age and prints "yoe are eligible" if the age is greater
# #if age is greater tahn equal to 18 otherwise prints "You arenot eligible"
age = int(input("Enter age:"))
if age < 18:
     print("You are eligible")

else:
     print("You arenot eligible")

#Write python function named grade students that takes a student's mark as input and returns their corresponding
#grade based on the following criteria:
#90 and above A
#80-89 B
#70-79 C
#60-69 D
#Below 60 F
# Test the function with 85
def grade_students(marks):
     marks = int(input("Enter the marks please:"))
     if marks >=90:
         print('Thats grade A' )
     elif marks >=80 and marks < 89:
         print("Thats grade B")
     elif marks >=70 and marks < 79:
         print("Thats grade C")
     elif marks >= 60 and marks< 69:
         print('The grade is D' )
     else:
         print('The Grade is F')
grade_students(marks=85)
# # Test the function with 85
def grade_students():
#     marks = 85
#     if marks >=90:
#         print('Thats grade A' )
#     elif marks >=80 and marks < 89:
#         print("Thats grade B")
#     elif marks >=70 and marks < 79:
#         print("Thats grade C")
#     elif marks >= 60 and marks< 69:
#         print('The grade is D' )
#     else:
#         print('The Grade is F')
# grade_students()

#Modify the grade students function to handle the case where the input mark is not a valid number. If the input 
# isnot a number the function shuold return inavlid input test the function with both a avlid mark and an invalid input
 def grade_students(marks):
     marks = int(input("Enter the marks please:"))
     if marks >=90:
         print('Thats grade A' )
     elif marks >=80 and marks < 89:
         print("Thats grade B")
     elif marks >=70 and marks < 79:
         print("Thats grade C")
     elif marks >= 60 and marks< 69:
         print('The grade is D' )
     elif marks <= 60:
         print('The Grade is F')
     else:
         return "Invalid Input"
#except ValueError:
    
    
# grade_students(marks=85)


# def grade_students(marks=None):
#     try:
#         # If marks is passed as a string, convert it to an integer
#         if marks is None:
#             marks = input("Enter the marks please: ")
#             marks = int(marks)  # Try converting to an integer
            
#         # Check if marks is a valid number
#         if isinstance(marks, int):
#             # Check the grade based on the marks
#             if marks >= 90:
#                 print('That\'s grade A')
#             elif marks >= 80 and marks < 89:
#                 print("That's grade B")
#             elif marks >= 70 and marks < 79:
#                 print("That's grade C")
#             elif marks >= 60 and marks < 69:
#                 print('The grade is D')
#             else:
#                 print('The Grade is F')
#         else:
#             return "Invalid input"
    
#     except ValueError:
#         return "Invalid input"  # Handle non-integer input gracefully

# # Test with a valid mark
# print(grade_students(marks=85))  # This should print "That's grade B"

# # Test with an invalid input (string)
# print(grade_students(marks="abc"))  # This should return "Invalid input"

# # Test with user input (when marks is not passed)
# Uncomment the following line to test with a user input
# print(grade_students())
