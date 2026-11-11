# ==============================================================================
# MODULES AND PACKAGES IN PYTHON
# ==============================================================================
# 
# What is a Module?
# A module is simply a file containing Python code—such as functions, classes, 
# and variables—saved with a `.py` extension. Modules allow you to organize 
# your code logically into separate files, making large applications modular, 
# readable, and maintainable instead of cramming everything into one massive script.
#
# When you need code from another module, you bring it into your current script 
# using the `import` keyword (e.g., `import math` or `from datetime import date`).


# ==============================================================================
# 1. THE PYTHON ECOSYSTEM: BUILT-IN VS. THIRD-PARTY MODULES
# ==============================================================================
# 
# A. Built-in Modules:
# Python comes "batteries included" with standard modules that are pre-installed 
# when you install Python. You don't need to download anything extra; just import them.
# Examples: `math`, `random`, `datetime`, `os`, `sys`.
#
import math
print("Built-in Math Example - Square root of 64:", math.sqrt(64))


# B. Third-Party Modules & Data Science Giants:
# Developed by the open-source community and hosted on PyPI (Python Package Index). 
# For data science, analytics, and machine learning, professionals leverage powerhouse libraries:
# - NumPy: Fast numerical computing and multi-dimensional array operations.
# - Pandas: Powerful data manipulation, cleaning, and DataFrame structures.
# - Scikit-learn: Industry-standard machine learning algorithms and modeling pipelines.


# C. Desktop Application GUI Frameworks:
# For building desktop applications (crucial for your diploma project modules), 
# you will rely heavily on specialized GUI modules:
# - Tkinter: Python's built-in standard GUI library (lightweight, easy to start with).
# - PyQt / PySide: Professional-grade, feature-rich bindings for the Qt framework 
#   (ideal for advanced, polished desktop applications with custom styling).


# ==============================================================================
# 2. INSTALLING THIRD-PARTY MODULES USING PIP (`python -m pip`)
# ==============================================================================
# Since third-party modules don't come built into Python, you must download and 
# install them onto your machine. Python uses a package manager called `pip`.
# 
# Best Practice Installation Command:
# Always use `python -m pip install <package_name>` in your terminal or command prompt.
# Using `python -m` ensures that the package is installed specifically into the 
# active Python environment you are currently running.
#
# Example Terminal Commands:
#   python -m pip install pandas
#   python -m pip install numpy
#   python -m pip install PyQt6
#   python -m pip install customtkinter  # Great for modern-looking desktop apps in Tkinter
#
# To verify installed packages or check versions:
#   python -m pip list


# ==============================================================================
# 3. DEVELOPING YOUR OWN CUSTOM MODULES (THE CALCULATOR EXAMPLE)
# ==============================================================================
# Just as you can import Python's modules, you can turn your own custom functions 
# into custom modules!
# 
# Imagine you are building a desktop calculator app for your students. Instead of 
# putting the math logic and the window UI in one file, you can split them:
# 
# --- FILE 1: `my_calculator_module.py` (Save this separately) ---
# """
# my_calculator_module.py
# A custom module containing reusable arithmetic functions.
# """
# 
# def add(a, b):
#     return a + b
# 
# def subtract(a, b):
#     return a - b
# 
# def multiply(a, b):
#     return a * b
# 
# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero!"
#     return a / b
# 
# -----------------------------------------------------------------
# 
# --- FILE 2: `main_app.py` (Your running script where you import it) ---
# 
# import my_calculator_module as calc
# 
# result_sum = calc.add(50, 25)
# result_product = calc.multiply(12, 4)
# 
# print(f"Custom Module Addition: {result_sum}")
# print(f"Custom Module Multiplication: {result_product}")
# 
# -----------------------------------------------------------------
# 
# Why are Custom Modules Important?
# 1. Separation of Concerns: Your database logic, UI layout, and mathematical 
#    calculations live in separate, organized files.
# 2. Team Collaboration: In student projects or workplace software development, 
#    different team members can work on separate modules simultaneously without 
#    breaking each other's code.
# 3. Code Reusability Across Projects: You can reuse your custom calculator or 
#    database utility module in future desktop apps without rewriting code!



## Assignment play around with some advanced modules pandas, pygame, numpy, Qt, django, flask, matplotlib, seaborn, scikit-learn, tensorflow, keras, opencv, pillow, requests, beautifulsoup4, sqlalchemy, pytest, sphinx, jupyter, streamlit, dash, plotly, bokeh, scrapy, pyinstaller, py2exe