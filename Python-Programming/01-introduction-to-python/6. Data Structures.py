# ==============================================================================
# DATA STRUCTURES IN PYTHON
# ==============================================================================
# 
# What are Data Structures?
# Data structures are specialized containers that organize, manage, and store data 
# efficiently in memory.
# 


# ==============================================================================
# 1. LISTS (Mutable & Ordered Collections)
# ==============================================================================
# Created with square brackets `[]`. Ordered, changeable (mutable), and allows duplicates.
# 
# Example A Games
games_list = ["Football", "Hockey", "Rugby", "Chess", "Swimming"]
print("Games:", games_list)

# Accessing elements:
print("First game:", games_list[0])

# Modifying an element:
games_list[1] = "Dart"  # Changing "Hockey" to "Dart"
print("After changing index 1:", games_list)

# Moving/Reordering elements (e.g., moving an item by popping and inserting):
# Let's move "Hockey" from index 1 to the end
moved_game = games_list.pop(1)
games_list.append(moved_game)
print("After moving Hockey to the back:", games_list)

# Example B: Installed software modules
installed_modules = ["Dashboard", "UserAuth", "DatabaseConnector", "Logger"]
installed_modules[1] = "OAuthAuthentication"
print("Technical List - Modules:", installed_modules, "\n")


# ==============================================================================
# 2. TUPLES (Immutable & Ordered Collections)
# ==============================================================================
# Created with parentheses `()`. Ordered, but IMMUTABLE (cannot be changed once created).
# 
# Example A: A Favorite Smoothie Recipe Ingredients (Fixed proportions)
smoothie_recipe = ("Banana", "Mango", "Yogurt", "Honey")
print("Fun Tuple - Smoothie Ingredients:", smoothie_recipe)

# Accessing elements:
print("Primary fruit:", smoothie_recipe[0])

# Demonstrating Immutability:
# smoothie_recipe[1] = "Strawberry"  # This would crash with a TypeError!
# If you *really* need to change a tuple, you convert it to a list first:
temp_list = list(smoothie_recipe)
temp_list[1] = "Pineapple"
smoothie_recipe = tuple(temp_list)
print("Updated Smoothie Recipe Tuple:", smoothie_recipe)

# Example B (Serious/Desktop App): Database connection configurations
db_config = ("localhost", 5432, "admin_db", True)
print("Technical Tuple - DB Config:", db_config, "\n")


# ==============================================================================
# 3. SETS (Unordered Collections with NO Duplicates)
# ==============================================================================
# Created with curly braces `{}` or `set()`. Unordered, mutable, but NO duplicates.
# 
# Example A: Team Sports Played in a Neighborhood
sports_set = {"Football", "Basketball", "Hockey", "Football", "Basketball"}
print("Fun Set - Sports (Notice duplicates are automatically removed):", sports_set)

# Adding a new sport:
sports_set.add("Volleyball")
print("After adding Volleyball:", sports_set)

# Trying to add a duplicate sport (Python ignores it silently):
sports_set.add("Football")
print("After trying to add duplicate 'Football':", sports_set)

# Example B (Serious/Desktop App): Tracking unique user session IDs
active_sessions = {"usr_001", "usr_002", "usr_003", "usr_001"}
print("Technical Set - Unique Sessions:", active_sessions, "\n")


# ==============================================================================
# 4. DICTIONARIES (Key-Value Pair Collections)
# ==============================================================================
# Created with curly braces `{}` using `key: value` pairs. Optimized for lookups.
# 
# Example A (Light & Fun): Details of a Favorite Video Game Character
player_profile = {
    "character_name": "ShadowNinja",
    "level": 42,
    "health_points": 85.5,
    "is_online": True,
    "inventory": ["Sword", "Shield", "Potion"]
}
print("Fun Dictionary - Character Stats:")
print(f"Name: {player_profile['character_name']} | Level: {player_profile['level']}")

# Modifying and adding values:
player_profile["level"] = 43  # Level up!
player_profile["guild"] = "CyberTitans"  # Add new key-value pair

# Example B (Serious/Desktop App): Desktop application user preferences config
user_config = {
    "username": "kioo_admin",
    "role": "SuperAdmin",
    "theme_dark": True
}
print("Technical Dictionary - User Config:", user_config)