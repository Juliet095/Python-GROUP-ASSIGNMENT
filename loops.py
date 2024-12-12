#1) Write a Python program that prints all even numbers between 1 and 20 using a for loop.
def even_numbers():
    for even in range(1,21):
        if even % 2 ==0:
            print(even)
        else:
            pass
even_numbers()

#2) Use a while loop to ask the user to input a number until they provide a number greater than 10.
def number_greater_than_10():
    num = 0
    
    while num < 0:
        num = int(input('Please input a number: '))
            
        if num <=10:
            print(f'Please input a number greater than 10')
            
        else:
            print(f'The number is greater than 10, Exiting')
number_greater_than_10()    

#3) Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.
def multiplication_table():
    for j in range(1,11):
        for k in range(1,6):
            print(j*k, end=' \t ')
        print('\n\n')
multiplication_table()

#4)  Given a list of integers, [4, 7, 2, 9, 12, 15], 
# write a program using a for loop to find the sum of all odd numbers and print the result.
def sum_of_odd():
    x=[4, 7, 2, 9, 12, 15]
    sum = 0
    for i in x:
        
        if i % 2 != 0:
            sum += i
        print(sum)
sum_of_odd()