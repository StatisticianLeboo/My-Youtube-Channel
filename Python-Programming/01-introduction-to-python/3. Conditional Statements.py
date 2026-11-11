# ==========================================
# WHAT ARE CONDITIONAL STATEMENTS IN PYTHON?
# ==========================================

# Conditional statements allow your program to make decisions and execute 
# different blocks of code depending on whether a specific condition is 
# True or False. They form the backbone of decision-making logic in programming.
# 
# Python uses three primary keywords to handle conditional logic:
# 1. if    - Evaluates a condition. If True, executes the indented code block.
# 2. elif  - Short for "else if". Evaluates an alternative condition if the 
#            preceding 'if' or 'elif' condition evaluated to False.
# 3. else  - Acts as a catch-all. Executes its code block only if all preceding 
#            conditions evaluated to False.


# ==========================================
# EXAMPLE 1: Simple if Statement
# ==========================================

temperature = 28

if temperature > 25:
    print("It's a warm day outside!")  # Executes because 28 > 25 is True


# ==========================================
# EXAMPLE 2: if-else Statement
# ==========================================

score = 45

if score >= 50:
    print("Congratulations, you passed!")
else:
    print("You did not pass. Try again!")  # Executes because 45 >= 50 is False


# ==========================================
# EXAMPLE 3: if-elif-else Ladder
# ==========================================
# Used when you need to check multiple conditions sequentially.

marks = 78

if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"  # Executes because 78 >= 70 is True (checks stop here)
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Your grade is: {grade}")


# ==========================================
# EXAMPLE 4: Nested Conditional Statements
# ==========================================
# Conditional statements can be placed inside other conditional statements 
# to handle multi-layered logic.

is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Access granted: Welcome to the Admin Panel.")
    else:
        print("Access granted: Welcome to the User Dashboard.")  # Executes
else:
    print("Access denied: Please log in first.")