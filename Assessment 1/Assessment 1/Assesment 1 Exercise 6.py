## Exercise 6: Brute Force Attack - 30 Marks

#Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
# 1. Define the correct password.
# 2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
# 3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

# Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.

print("Exercise 6")
# This is the part where it defines the correct password.
password = "12345" # The password that needs to be entered to grant access. 
num_attempts = 5 # The maximum number of allowed attempts 

# This tracks the number of attempts by the user. 
attempts = 0

while attempts < num_attempts:
    # Ask the user to enter the password.
    user = input("Enter the password: ")
    
    # This checks if the entered password is the correct one. 
    if user == password:
        print("Access granted! Welcome.")
        break  # THis exits the loop if the password is correct.
    else:
        attempts += 1  # Increment the attempts counter. 
        remaining_attempts = num_attempts - attempts # This line calculates the remaining attempts. 
        print(f"Incorrect password. You have {remaining_attempts} attempt(s) left.")
        
# This checks if the maximum attempts is reached, after exiting the loop.
if attempts == num_attempts:
    print("The Maximum attempts has been reached. \nAuthorities have been alerted.")
