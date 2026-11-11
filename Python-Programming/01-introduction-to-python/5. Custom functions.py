# ==========================================
# CUSTOM (USER-DEFINED) FUNCTIONS IN PYTHON
# ==========================================
# 
# What are Custom Functions?
# While built-in functions (like print() or len()) are provided by Python, 
# custom functions are blocks of reusable code that *you* write yourself using 
# the `def` keyword. 
# 
# Why use them?
# 1. Reusability: Write once, call multiple times.
# 2. Maintainability: Fix a bug in one place instead of across 50 places.
# 3. Modularity: Break complex diploma-level logic into clean, readable pieces.
#
# Anatomy of a Function:
# def function_name(parameter1, parameter2):
#     # logic block
#     return result


# def function_name(param1: type = default_value, *args, **kwargs) -> return_type:
#     """
#     [Docstring]: Description of what the function does, its parameters, 
#     and what it returns. Accessible via help(function_name) or __doc__.
#     """
#     # [Function Body]: Local business logic, data processing, or algorithms
#     
#     # [Return Statement]: Passing results back to the caller (or returning None)
#     return result


# ==========================================
# EXAMPLE 1: 1 Variable Function
# Task: Compute the area of a circle given its radius.
# Formula: Area = pi * r^2
# ==========================================

def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

# Testing the function:
my_radius = float(input("Enter the radius of the circle: "))
result_area = calculate_circle_area(my_radius)
print(f"Area of circle with radius {my_radius}: {result_area:.2f}")


# ==========================================
# EXAMPLE 2: 2 Variable Function
# Task: Compute employee net pay after a fixed deduction.
# ==========================================

def calculate_net_pay(basic_salary, tax_deduction):
    net_pay = basic_salary - tax_deduction
    return net_pay

# Testing the function:
salary = 45000.00
tax = 6750.50
final_take_home = calculate_net_pay(salary, tax)
print(f"Net Pay: Ksh {final_take_home:,.2f}")


# ==========================================
# EXAMPLE 3: 3 Variable Function
# Task: Compute Simple Interest for a bank loan or savings account.
# Formula: SI = (P * R * T) / 100
# ==========================================

def calculate_simple_interest(principal, annual_rate, time_years):
    interest = (principal * annual_rate * time_years) / 100
    total_amount = principal + interest
    return interest, total_amount

# Testing the function:
p = 100000  # Principal in Ksh
r = 12      # Annual rate in percentage
t = 3       # Time in years

earned_interest, total_payable = calculate_simple_interest(p, r, t)
print(f"Simple Interest: Ksh {earned_interest:,.2f} | Total Amount: Ksh {total_payable:,.2f}")


# ==========================================
# EXAMPLE 4: 4 Variable Function
# Task: Compute Compound Interest for a financial asset/investment.
# Formula: A = P * (1 + r/n)^(n*t)
# ==========================================

def calculate_compound_interest(principal, annual_rate, time_years, compounding_frequency):
    r_decimal = annual_rate / 100
    n = compounding_frequency
    t = time_years
    
    amount = principal * (1 + (r_decimal / n)) ** (n * t)
    compound_interest = amount - principal
    return amount, compound_interest

# Testing the function:
inv_principal = 250000
inv_rate = 10.5
inv_years = 5
frequency_per_year = 12  # Compounded monthly

final_val, total_ci = calculate_compound_interest(inv_principal, inv_rate, inv_years, frequency_per_year)
print(f"Future Investment Value: Ksh {final_val:,.2f} (Interest Earned: Ksh {total_ci:,.2f})")


# ==========================================
# EXAMPLE 5: Technical Diploma IT Example (Multi-Variable Business Logic)
# Task: Compute a student's final weighted course score.
# Weights: CATs = 30%, Practical Lab = 30%, Final Exam = 40%
# Includes validation logic using conditional statements inside the function.
# ==========================================

def compute_student_grade(cat_score, lab_score, exam_score):
    # Ensure scores don't exceed max bounds
    if cat_score > 30 or lab_score > 30 or exam_score > 40:
        return "Error: Invalid score inputs provided."
    
    total_score = cat_score + lab_score + exam_score
    
    # Grading tier logic
    if total_score >= 70:
        grade = "Distinction (A)"
    elif total_score >= 60:
        grade = "Credit (B)"
    elif total_score >= 50:
        grade = "Pass (C)"
    else:
        grade = "Fail (F)"
        
    return total_score, grade

# Testing the function:
student_total, student_grade = compute_student_grade(24, 27, 35)
print(f"Final Score: {student_total}/100 | Grade: {student_grade}")


# ==========================================
# EXAMPLE 6: Advanced Technical Example (Variable-Length Arguments `*args`)
# Task: Create a network server response time analyzer that accepts 
# any number of ping response metrics and computes the average latency.
# ==========================================

def analyze_server_latency(*latency_readings):
    if len(latency_readings) == 0:
        return "No readings available."
    
    avg_latency = sum(latency_readings) / len(latency_readings)
    max_latency = max(latency_readings)
    min_latency = min(latency_readings)
    
    return {
        "average": round(avg_latency, 2),
        "peak": max_latency,
        "lowest": min_latency
    }

# Testing the function with multiple dynamic server metrics (ms):
server_stats = analyze_server_latency(45.2, 52.8, 38.1, 61.4, 49.0)
print(f"Server Latency Diagnostics: {server_stats}")




# Additional examples


def calculate_system_storage(base_capacity_gb: float, allocation_factor: float = 1.15) -> float:
    """
    Computes the total allocated disk space required for virtual machines,
    including an overhead factor for system logs and snapshots.

    Parameters:
    -----------
    base_capacity_gb : float
        The raw storage requested by the client in gigabytes.
    allocation_factor : float, optional
        The multiplier for overhead buffer (default is 1.15, meaning 15% extra).

    Returns:
    --------
    float
        The final calculated storage requirement rounded to 2 decimal places.
    """
    total_required = base_capacity_gb * allocation_factor
    return round(total_required, 2)

# Checking the docstring programmatically (useful for dynamic app documentation):
# print(calculate_system_storage.__doc__)


# ==============================================================================
# 2. PARAMETER TYPES: POSITIONAL, KEYWORD, AND DEFAULTS
# ==============================================================================
# Python functions handle inputs in several flexible ways:
# - Positional Parameters: Must be provided in the exact order declared.
# - Keyword Parameters: Passed explicitly by name, making order irrelevant.
# - Default Parameters: Optional parameters that fall back to a preset value if omitted.

def configure_desktop_window(title: str, width: int = 1024, height: int = 768, resizable: bool = True):
    """Prints configuration settings for a desktop application window."""
    print(f"Window Config -> Title: '{title}' | Resolution: {width}x{height} | Resizable: {resizable}")

# Calling using positional arguments:
configure_desktop_window("Main Dashboard", 800, 600)

# Calling using keyword arguments (order doesn't matter, highly readable):
configure_desktop_window(title="Settings Panel", height=480, width=640, resizable=False)

# Calling using default values (omitting height, width, and resizable):
configure_desktop_window("Login Portal")


# ==============================================================================
# 3. VARIABLE-LENGTH ARGUMENTS: `*args` and `**kwargs`
# ==============================================================================
# When building desktop apps, you often won't know how many inputs a function 
# might receive (e.g., a dynamic list of file paths dropped into a GUI, or a 
# flexible configuration dictionary).
# 
# - `*args`: Collects any number of extra positional arguments into a TUPLE.
# - `**kwargs`: Collects any number of extra keyword arguments into a DICTIONARY.

def generate_system_report(report_title: str, *client_names, **audit_metadata):
    print(f"\n--- REPORT: {report_title} ---")
    
    print("Registered Clients (*args tuple):")
    for client in client_names:
        print(f"  - {client}")
        
    print("\nAdditional Audit Metadata (**kwargs dictionary):")
    for key, value in audit_metadata.items():
        print(f"  {key}: {value}")

# Testing `*args` and `**kwargs`:
generate_system_report(
    "Q3 IT Audit", 
    "Kioo Africa Labs", "Rose Cakes", "Kidogo ECD",  # These go into *args
    generated_by="Admin_Ian", version=2.4, secure_mode=True  # These go into **kwargs
)


# ==============================================================================
# 4. VARIABLE SCOPE (THE LEGB RULE)
# ==============================================================================
# Scope determines where in your code a variable can be seen or modified. 
# Python follows the LEGB rule when looking up variable names:
# L - Local: Defined inside the current function.
# E - Enclosing: Defined in any enclosing functions (nested functions).
# G - Global: Defined at the top level of the script or module.
# B - Built-in: Pre-assigned names in Python (like `print`, `len`, `sum`).

app_version = "v1.2.0-stable"  # GLOBAL scope

def deploy_application(environment: str):
    server_port = 8080  # LOCAL scope to this function
    
    print(f"Deploying application {app_version} to {environment} on port {server_port}...")
    
    def log_deployment():
        # This nested function can access 'server_port' from its ENCLOSING scope
        print(f"Internal Log: Port {server_port} successfully bound.")
        
    log_deployment()

deploy_application("Production")
# Note: Trying to print `server_port` or log_deployment outside the function 
# would raise a NameError because they are local/enclosed!


# ==============================================================================
# 5. RETURNING MULTIPLE VALUES (PACKING INTO TUPLES)
# ==============================================================================
# Unlike some languages that restrict you to a single return value, Python 
# allows you to return multiple values separated by commas. Python automatically 
# packs them into a single tuple under the hood.

def analyze_dataset_metrics(scores_list):
    if not scores_list:
        return 0, 0, 0.0
    
    total_count = len(scores_list)
    max_score = max(scores_list)
    mean_score = sum(scores_list) / total_count
    
    return total_count, max_score, mean_score  # Returns a tuple of 3 values

# Unpacking the returned tuple into distinct variables:
class_scores = [65, 72, 88, 91, 54, 79]
count, highest, average = analyze_dataset_metrics(class_scores)

print(f"\nDataset Statistics -> Count: {count} | Highest: {highest} | Average: {average:.2f}")


# ==========================================
# EXERCISE:
# ==========================================
# Exercise: Write a custom Python function named `calculate_mobile_money_fee` 
# that takes two parameters: `amount_sent` and `transaction_type` (e.g., "send" or "withdraw").
# 
# Rules to implement inside your function:
# 1. If the transaction type is "send", charge a flat 1.5% fee on the amount.
# 2. If the transaction type is "withdraw", charge a flat 2.5% fee on the amount, 
#    plus an additional Ksh 50 base charge.
# 3. Return the calculated fee amount. Test your function with different values!