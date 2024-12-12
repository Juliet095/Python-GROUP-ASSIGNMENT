# 1. Create a dictionary with three key-value pairs representing a 
#  student's information: name, age, and grade. Print each key-value pair on a new line.
# #Creating the dictionary
student_info = {
    "name": "Juliet",  
     "age": "21",
     "grade": "A"
 }
for key, value in student_info.items():
     print(f"{key}: {value} \n")

    
# 2. Write a function that takes a dictionary of people's
#   names and their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and 
#  returns a list of names of people who are 21 or older.
def get_adults(peoples_dictionary):
    adults = []
    for name, age in peoples_dictionary.items():
        if age >= 21:
            adults.append(name)
    return adults
people= {'Alice': 24, 'Bob': 19, 'Charlie': 30} 
result = get_adults(people)
print(result)  


#  3.  Given a dictionary representing items in a store with their prices, 
#  {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items 
#  bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
 
def store_items_with_prices():
    dictionary = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
    items_bought = ["apple","oranges","banana"]
    total_cost = sum(dictionary[items_bought] for item in items_bought)
    print (f"The total cost of the item bought is:${total_cost}")
store_items_with_prices() 



# 4.    Challenge: Write a program that counts the occurrences of each word in a given sentence. 
# Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.

sentence = "hello hello world"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word,0) + 1
    print("Word occurances:")
for word, count in word_count.items():
    print(f"{word}:{count}")
