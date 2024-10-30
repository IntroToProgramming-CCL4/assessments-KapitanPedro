## Exercise 5: Days of the Month - 30 Marks

# Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
# 1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
# 2. Input Handling: Ask the user to input the month number.
# 3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
# Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.


print("Exercise 5")

# here is a dictionary to map the month numbers to days in a normal year use # to show what month is who.
months = {
    1: 31,  # January
    2: 28,  # February (normal year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# This prompt the user to enter a month number.
num = int(input("Enter the month number (1-12): "))

# It checks if the entered month number exists in the months dictionary.
if num in months:
    # This check for February and whether the year is a leap year.
    if num == 2:
        year = int(input("Enter the year: "))
        # This checks for a Leap year because it is divisible by 4, but not by 100, or divisible by 400.
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("The month February has 29 days in a leap year.")
        else:
            print(f"The month February has {months[num]} days in a normal year.")
    else:
        print(f"The month has {months[num]} days.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.") # this prints if the number inputed by the user is not part of the dictionary above.
