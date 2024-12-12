# 1.  Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.

def fruit_list ():
    fruits = ['Apples','orange','Mangoes','Water melon','Paw paw']
    for fruit in fruits:
        print (f'{fruit}\n')
fruit_list ()

# # 2.  Intermediate: Write a function that takes a list of numbers and returns a new list 
# # with each number squared. Example: [1, 2, 3] should become [1, 4, 9].

def square_numbers():
    squared_list = []
    numbers = [1, 2, 3]
    for num in numbers:
        squared_list.append(num ** 2)
    return squared_list
result = square_numbers() 
print(result)  
square_numbers()

 
# # 3.  Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and 
# # list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].

def combination_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = []
    for i in range(len(list1)):
        combined.append(list1[i])  
        combined.append(list2[i])  
    print(combined)
combination_lists()
 

# 4.    Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2],
#  write a program to find and print the two largest numbers in the list without using the max() function.

numbers = [3, 1, 4, 1, 5, 9, 2]
largest = float('-inf') #negative infinity
second_largest = float('-inf')
for num in numbers :
    if num> largest: # if the currentnumber is greater than the largest then there is need to update both
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:       
        second_largest = num
        print("largest number is:", largest)
    else:
            print ("second largets number is:" ,second_largest)
 
