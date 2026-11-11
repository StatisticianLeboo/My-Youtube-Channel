# A function is a resuable set of code that allows you to implement a process
# 
# In built functions are 

vegetables = ['kales', 'onions', 'cabbages']

age = 23

# Common in built funtion 

# print() - retun

print("List of vegetables: ")
print(vegetables)

print("Age: ", age)


# len() - returns the length of a list, string, or other iterable
print("Length of vegetables list: ", len(vegetables))

# int() - converts a value to an integer
age_str = "23"

print("Type of age_str: ", type(age_str))

age_int = int(age_str)
print("Type of age_int: ", type(age_int))
print("Age as integer: ", age_int)

# str() - converts a value to a string
age_str_again = str(age_int)
print("Type of age_str_again: ", type(age_str_again))
print("Age as string: ", age_str_again)

# range() - generates a sequence of numbers
print("Numbers from 0 to 4: ", list(range(5)))


# input() - gets user input from the console

name = input("Enter your name: ")
print("Hello, ", name)

# output() - displays output to the console
print("This is an example of output using the print() function.")


# other functions include math functions like abs(), round(), min(), max(), sum(), etc.