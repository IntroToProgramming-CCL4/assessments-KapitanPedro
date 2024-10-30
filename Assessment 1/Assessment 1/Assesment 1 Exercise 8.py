## Exercise 8: Simple Search - 30 Marks

# Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
# 1. Allow the user to input the search term instead of using a predefined value.
# 2. Implement the search functionality based on user input.

print("Exercise 8")
# This is a list with with all the name provided on the exercise. 
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# This is the optional Requirement which allows the user to input the search term. 
find_guy = input("Please enter the name to search for: ")

# This checks if the entered name is in the list. 
if find_guy in names:
    print(f"{find_guy} is found in the list!") # If the name is found in the list.
else:
    print(f"{find_guy} is not found in the list.") # This prints if the guy is not on the list.