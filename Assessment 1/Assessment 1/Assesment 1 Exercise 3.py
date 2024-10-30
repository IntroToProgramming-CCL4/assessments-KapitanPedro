## Exercise 3: Biography - 25 Marks
# In this exercise, you'll create a program that stores and prints your name, 
# hometown, and age to the console using a Python dictionary.
### Advanced Requirements:
#Have the user input their name, hometown, and age instead of hardcoding the values.
#Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
#Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?

# This variable gets the user's 1st and 2nd name and hometown.
print("Exercise 3")
name = input("Please enter your first and second name: ")
hometown = input("Please enter your hometown: ")

while True:  # This while loop is making sure it's a number.
    age = input("Please enter your age: ")
    if age.isdigit(): # we use the isdigit() funtion if the input is a number.
        a = int(age)  # this coverts it into a integer if valid.
        break
    else:
        print("Please enter a numeric value for age.\nplease try again. ")

# We now use the information above into a dictionary. 
user = { 
    "name": name,
    "hometown": hometown,
    "age": age
}

# This line of code prints all the different values on serparate lines on one single print statement.
print(f"Name: {user['name']}\nHometown: {user['hometown']}\nAge: {user['age']}")