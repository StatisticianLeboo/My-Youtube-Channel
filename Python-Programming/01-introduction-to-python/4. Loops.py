# ==========================================
# LOOPS IN PYTHON
# ==========================================
# Loops allow us to repeat a block of code multiple times automatically.
# Instead of writing the same code 10 times, a loop handles it efficiently.
# There are two main types of loops in Python: 
# 1. while loops (repeat based on a condition)
# 2. for loops (repeat for a specific sequence or number of times)


# ==========================================
# PART 1: THE WHILE LOOP
# ==========================================
# A while loop executes a block of code repeatedly as long as its 
# given condition remains True. Once the condition becomes False, the loop stops.

print("--- WHILE LOOP EXAMPLES & EXERCISE ---")

# --- While Loop Example 1: Countdown Timer ---
# Useful when you don't know the exact number of iterations beforehand, 
# but you know the stopping condition.
countdown = 5
print("Countdown starting:")
while countdown > 0:
    print(countdown)
    countdown -= 1  # Crucial step: decreasing the variable so the loop eventually stops
print("Liftoff! 🚀\n")


# --- While Loop Example 2: Password Attempt Limiter ---
# Tracking security attempts until a condition (correct password or max tries) is met.
correct_password = "secret123"
attempts = 0
max_attempts = 3
access_granted = False

while attempts < max_attempts and not access_granted:
    entered_password = input("Enter your password: ")
    attempts += 1
    if entered_password == correct_password:
        print("Access granted! Welcome.")
        access_granted = True
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect. You have {remaining} attempt(s) left.")
        else:
            print("Account locked due to too many failed attempts.")
print()


# if bank balance is greater than 0, withdraw money until balance is 0
bank_balance = 1000
while bank_balance > 0:
    withdraw_amount = int(input("Enter the amount to withdraw: "))
    if withdraw_amount > bank_balance:
        print("Insufficient balance.")
    else:
        bank_balance -= withdraw_amount
        print(f"Withdrawn: {withdraw_amount}. Remaining balance: {bank_balance}")
        
        
        
# a loop that does not terminate - infinite loop
# we can use break statement to exit the loop
# example of infinite loop - user input until user enters 'exit'
while True:
    user_input = input("Enter something (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")



# --- While Loop Exercise for Students ---
# EXERCISE: Write a while loop that acts as a "Guess the Number" game.
# Set a secret number (e.g., secret_number = 7). Keep asking the user to 
# input a guess using `input()` until their guess matches the secret number. 
# Print a congratulatory message when they guess correctly.
#
# (Student Exercise Space - Write your code below this comment)
# secret_number = 7
# guess = int(input("Guess a number between 1 and 10: "))
# while guess != secret_number:
#     print("Wrong guess, try again!")
#     guess = int(input("Guess a number between 1 and 10: "))
# print("Correct! You guessed the secret number.")


# ==========================================
# PART 2: THE FOR LOOP
# ==========================================
# A for loop is used for iterating over a sequence (such as a list, tuple, 
# dictionary, set, or string). It is ideal when you know beforehand how 
# many times you want to execute a block of code.

print("--- FOR LOOP EXAMPLES & EXERCISE ---")

# --- For Loop Example 1: Iterating Through a List ---
# Automatically loops through each item in a collection without manual indexing.
students = ["Alice", "Brian", "Clara", "David"]
print("Class Attendance List:")
for student in students:
    print(f"- {student} is present.")
print()


# --- For Loop Example 2: Using range() for Calculations ---
# The range() function generates a sequence of numbers, perfect for counting loops.
print("Multiplication Table for 3:")
for i in range(1, 6):  # Loops from 1 to 5
    result = 3 * i
    print(f"3 x {i} = {result}")
print()


# --- For Loop Exercise for Students ---
# EXERCISE: Given a list of student scores [45, 67, 89, 32, 90, 78], 
# write a for loop that prints "Pass" if the score is 50 or above, 
# and "Fail" if the score is below 50 alongside the score value.
#
# (Student Exercise Space - Write your code below this comment)
# scores = [45, 67, 89, 32, 90, 78]
# for score in scores:
#     if score >= 50:
#         print(f"Score {score}: Pass")
#     else:
#         print(f"Score {score}: Fail")


# ==========================================
# PART 3: HOW PYTHON BREAKS AN UNENDING (INFINITE) LOOP
# ==========================================
# An infinite loop happens when the loop condition never evaluates to False 
# on its own, causing the program to run forever and potentially crash or freeze.
# 
# Python provides two main ways to deal with or break unending loops:

# 1. The `break` Statement:
# You can forcefully exit a loop from the inside using `break` when a 
# specific condition is met.
# Example:
counter = 1
while True:  # Looks like an infinite loop
    print(f"Loop iteration {counter}")
    if counter >= 3:
        print("Breaking out of the infinite loop safely!")
        break  # Stops the loop immediately
    counter += 1
print()


# 2. Emergency Manual Interruption (Keyboard Interrupt):
# If you run an infinite loop in your terminal or script and it gets stuck 
# without a `break` condition, you can force-stop Python execution by 
# pressing `Ctrl + C` on your keyboard. This raises a `KeyboardInterrupt` 
# error and terminates the script.


# ==========================================
# NB: WHAT TO KEEP IN MIND WHEN CREATING LOOPS
# ==========================================
# 1. Always update your loop variables: 
#    In a while loop, ensure that whatever controls your condition (like a counter 
#    or balance) actually changes inside the loop. If it never changes, you 
#    create an accidental infinite loop.
#
# 2. Mind your indentation: 
#    Python relies heavily on clean indentation. Code inside the loop must be 
#    indented correctly. Anything outside the indentation block runs *after* 
#    the loop finishes.
#
# 3. Choose the right loop tool:
#    - Use a `for` loop when iterating over known collections, lists, or a 
#      fixed number of steps (`range`).
#    - Use a `while` loop when looping depends