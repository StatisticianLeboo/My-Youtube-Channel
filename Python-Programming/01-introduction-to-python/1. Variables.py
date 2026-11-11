# %% ===================================================================
# SECTION 1: VARIABLES & DATA TYPES
# =======================================================================
# Python is dynamically typed: you do NOT declare a type before a
# variable name (unlike C++/Java's `int age = 23;`). The variable is
# created the moment you assign it a value, and Python figures out the
# type automatically.

student_name = "Amina"        # str   -> text
age = 23                      # int   -> whole number
gpa = 3.8                     # float -> decimal number
is_active = True              # bool  -> True / False (capital letters!)
graduation_year = None        # NoneType -> deliberately "no value yet"

# f-strings are the modern, preferred way to build output text.
# Put the variable name directly inside { } inside a string marked f"...".
print(f"{student_name} is {age} years old, GPA {gpa}, active: {is_active}")
