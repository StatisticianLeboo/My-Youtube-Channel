# ==============================================================================
# INTRODUCTION TO OBJECT-ORIENTED PROGRAMMING (OOP)
# ==============================================================================
# 
# Object-Oriented Programming often feels abstract because it changes how we 
# think about code. Instead of writing long procedural scripts from top to bottom, 
# OOP lets us build custom "blueprints" (Classes) and create interactive 
# "things" (Objects) from them that model the real world. 


# ==============================================================================
# 1. WHAT IS AN OBJECT? (THE CAR ANALOGY)
# ==============================================================================
# In the real world, almost everything is an object. 
# Take a **Car** as an object:
# - It has physical attributes (properties/state): wheels, steering wheel, body, 
#   chairs, engine, exhaust, color, model.
# - It has behaviors (actions it can perform): accelerate(), brake(), turn_left(), 
#   honk_horn().
# 
# In Python, an object bundles data (attributes) and actions (methods) together 
# into a single self-contained unit.


# ==============================================================================
# 2. WHAT IS A CLASS? (THE BLUEPRINT & THE DOG EXAMPLE)
# ==============================================================================
# If an object is a built house, a **Class** is the architectural blueprint. 
# You cannot live in a blueprint, but you can use it to build 10 identical 
# houses (or houses with different paint colors).
# 
# Classic Example: The `Dog` Class
# Let's define what a dog is conceptually, then create individual dog objects.

class Dog:
    # 1. The Constructor (`__init__`): This runs automatically when you create a new Dog.
    # It sets up the starting attributes (state) for that specific dog object.
    def __init__(self, breed_name, dog_name, age):
        self.breed = breed_name  # Attribute: Breed of the dog
        self.name = dog_name      # Attribute: Name of the dog
        self.age = age            # Attribute: Age in years

    # 2. A Method: A function inside a class that defines what the object can DO.
    def bark(self):
        return f"{self.name} ({self.breed}) barks: Woof! Woof! 🐶"

    def get_dog_info(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."


# Creating (instantiating) actual Dog objects from our Dog class blueprint:
dog1 = Dog("German Shepherd", "Rex", 3)
dog2 = Dog("Golden Retriever", "Buddy", 5)

# Interacting with our objects:
print(dog1.bark())              # Output: Rex (German Shepherd) barks: Woof! Woof!
print(dog2.get_dog_info())      # Output: Buddy is a 5-year-old Golden Retriever.
print()


# ==============================================================================
# 3. DEEP DIVE: ANATOMY OF A PYTHON CLASS STRUCTURE
# ==============================================================================
# Let's break down the keywords and structure of any Python class:
# 
# class ClassName:
#     def __init__(self, param1, param2):
#         self.param1 = param1  # Instance attribute
#         
#     def method_name(self):
#         # Action using self attributes
#         return something
#
# What is `self`? 
# `self` is simply a reference to the *current object* you are building or 
# interacting with. When you call `dog1.bark()`, Python automatically passes 
# `dog1` into `self` so the method knows it's talking about Rex, not Buddy.


# ==============================================================================
# 4. INHERITANCE: BUILDING UPON EXISTING CLASSES
# ==============================================================================
# Inheritance allows a new class (Child Class) to adopt all attributes and 
# methods of an existing class (Parent Class), saving you from rewriting code 
# and allowing you to add specialized features.
# 
# Example: A generic `AppWindow` parent class, and a specialized `WeatherAppWindow` 
# child class.

class AppWindow:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

    def render(self):
        return f"Rendering window '{self.title}' at {self.width}x{self.height}."


# WeatherApp inherits from AppWindow using `class Child(Parent):`
class WeatherAppWindow(AppWindow):
    def __init__(self, title, width, height, city_location):
        # `super()` calls the parent class constructor to handle title, width, height
        super().__init__(title, width, height)
        self.city_location = city_location  # New specialized attribute

    # Overriding / adding specialized methods for our weather app
    def fetch_weather_forecast(self):
        return f"Fetching live meteorological data for {self.city_location}..."

# Testing inheritance:
my_weather_app = WeatherAppWindow("Kioo Weather Desktop", 1024, 768, "Nairobi")
print(my_weather_app.render())                # Inherited from AppWindow!
print(my_weather_app.fetch_weather_forecast()) # Unique to WeatherAppWindow!
print()


# ==============================================================================
# 5. IMPORTANCE OF OOP & WHY IT MATTERS FOR DESKTOP APPLICATIONS
# ==============================================================================
# Why do we need OOP, especially 
# when building desktop applications (like with PyQt, Tkinter, or CustomTkinter)?
# 
# 1. UI Components are Objects: 
#    In desktop programming, every button, text box, menu bar, and window is 
#    an object created from a class. OOP gives you the exact mental model 
#    needed to manage multiple windows and widgets cleanly.
# 2. State Management: 
#    A desktop app needs to remember user settings, database connections, and 
#    session states across clicks. Classes bundle this state securely.
# 3. Code Reusability and Organization: 
#    Instead of a massive 2,000-line script full of tangled functions, OOP lets 
#    you separate concerns: a Database class handles data, a WeatherAPI class 
#    fetches forecasts, and a UI class renders buttons.


# ==============================================================================
# 6. PRACTICAL DESKTOP APP EXAMPLE: OBJECT-ORIENTED WEATHER FORECAST
# ==============================================================================
# Let's model a week-long weather forecasting tool for a desktop dashboard. 
# We'll use two classes: 
# 1. `DayForecast` to hold morning, midday, and evening predictions for a single day.
# 2. `WeeklyWeatherDashboard` to manage the whole week's data.

class DayForecast:
    def __init__(self, day_name, morning_cond, midday_cond, evening_cond, temp_c):
        self.day_name = day_name
        self.morning = morning_cond
        self.midday = midday_cond
        self.evening = evening_cond
        self.temp = temp_c

    def get_summary(self):
        return (f"[{self.day_name}] Temp: {self.temp}°C | "
                f"Morning: {self.morning} -> Midday: {self.midday} -> Evening: {self.evening}")


class WeeklyWeatherDashboard:
    def __init__(self, city):
        self.city = city
        self.forecasts = []  # A list to store DayForecast objects

    def add_daily_forecast(self, forecast_obj):
        self.forecasts.append(forecast_obj)

    def display_weekly_report(self):
        print(f"\n--- 7-DAY WEATHER DASHBOARD FOR {self.city.upper()} ---")
        for forecast in self.forecasts:
            print(forecast.get_summary())


# --- Testing our Weather Desktop App Backend ---
# 1. Initialize our dashboard for Nairobi
nairobi_weather = WeeklyWeatherDashboard("Nairobi")

# 2. Create individual day forecast objects
monday = DayForecast("Monday", "Foggy", "Sunny & Warm", "Clear", 24)
tuesday = DayForecast("Tuesday", "Cloudy", "Light Showers", "Breezy", 22)
wednesday = DayForecast("Wednesday", "Sunny", "Hot & Humid", "Partly Cloudy", 27)

# 3. Add them to our dashboard manager
nairobi_weather.add_daily_forecast(monday)
nairobi_weather.add_daily_forecast(tuesday)
nairobi_weather.add_daily_forecast(wednesday)

# 4. Generate the report
nairobi_weather.display_weekly_report()