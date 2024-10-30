## Exercise 4: Primitive Quiz - 30 Marks

# In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
# 1. Write a program that asks the user "What is the capital of France?" and waits for their response.
# 2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
# 3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
# Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
# Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.


print("Exercise 4")
print("Welcome to Guess the European capital Quiz")
score = 0  # This initializes the score.

question = input("What is the capital of France? ") # A variable that ask the user a Wuestion and let's yhe user enter a answer.
if question.lower() == "paris": # .lower allows it so that even if I use capital letter it allows the answer to proceed.
    print("Answer is Correct!") 
else:
    print("Answer is Wrong.") # Prints when the answer is wrong. 

question = input("1.What is the capital of Norway? ")
if question.lower() == "oslo":
    print("Answer is Correct!")
    score += 1 #This adds 1 point if the user get the question right. If not it proceeds and does not count a score resulting in no point for this question.
else:
    print("Answer is Wrong.")

question = input("2.What is the capital of Austria? ")
if question.lower() == "vienna":
    print("Answer is Correct!")
    score += 1
else:
    print("Answer is Wrong.")

    
question = input("3.What is the capital of Belgium? ")
if question.lower() == "brussels":
    print("Answer is Correct!")
    score += 1
else:
    print("Answer is Wrong.")

    
question = input("4.What is the capital of Sweden? ")
if question.lower() == "stockholm":
    print("Answer is Correct!")
    score += 1
else:
    print("Answer is Wrong.")

    
question = input("5.What is the capital of Spain? ")
if question.lower() == "madrid":
    print("Answer is Correct!")
    score += 1
else:
    print("Answer is Wrong.")

    
question = input("6.What is the capital of Italy? ")
if question.lower() == "rome":
    print("Answer is Correct!")
    score += 1
else:
    print("Answer is Wrong.")

    
question = input("7.What is the capital of Germany? ")
if question.lower() == "berlin":
    print("Answer is Correct!")
    score += 1
else:
    print("Answer is Wrong.")

    
question = input("8.What is the capital of United Kingdom? ")
if question.lower() == "London":
    print("Answer is Correct!")
    score += 1
else:
    print("Answer is Wrong.")

    
question = input("9.What is the capital of Netherlands? ")
if question.lower() == "amsterdam":
    print("Answer is Correct!")
    score += 1
else:
    print("Answer is Wrong.")

    
question = input("10.What is the capital of Portugal? ")
if question.lower() == "lisbon":
    print("Answer is Correct!")
    score += 1
else:
    print("Answer is Wrong.")

print(f"You got {score} questions correct!") # This shows the total amount of score accumulated per question. 

