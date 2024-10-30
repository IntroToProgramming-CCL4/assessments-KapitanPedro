## Exercise 10: Is it even? - 35 Marks

#Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
# * The program should ask the user for a number from within the main function.
# * The entered number should be passed to a function that determines if the value is even or odd.
# * The function should return a message indicating whether the number is even or odd.
# * The message returned by the function should be printed from within the main function.

print("Exercise 10")

def oddneven (num):  
    if num % 2 == 0:
        return f"The number {num} is even." # This part of the code determines 
    else:                                   # Whether the given number by the user is odd or even. 
        return f"The number {num} is odd."  # The return is a message indicates whether the number is even or odd.
def main():                            
    num = int(input("Enter a number: "))    # The main function being used here to prompt the user for input, which determine if the number is
    result = oddneven(num)                  # Even or odd, and print the result.
    print(result)                           # The num varibale ask the user to enter a integer number.
main()                                      # Result then calls my oddneven function with the number prompt by the user. Then prints the result by the oddneven function.
                                            # As it says in the last part of the intrucions says to run the message is printed from within the main function, to explain further the returned message from oddneven is now printed in the main function.
    
