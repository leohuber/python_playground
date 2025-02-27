# Formatted Strings (F-Strings)
# F-strings provide a way to embed expressions inside string literals, using curly braces {}.

# %%
name = "Alice"
age = 30

# Basic usage
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# Expressions inside f-strings
calculation = f"5 + 3 = {5 + 3}"
print(calculation)

# Calling functions
def to_uppercase(s):
    return s.upper()

shout = f"{to_uppercase('hello')} world!"
print(shout)

# Formatting numbers
pi = 3.14159
formatted_pi = f"Pi to three decimal places: {pi:.3f}"
print(formatted_pi)

# Using dictionaries
person = {"name": "Bob", "age": 25}
intro = f"Name: {person['name']}, Age: {person['age']}"
print(intro)

# Using f-strings with multiline strings
multiline = f"""
Name: {name}
Age: {age}
"""
print(multiline)

# %%
# # Raw strings (R-Strings)
# R-strings are string literals that treat backslashes as literal characters.

# %%
# Basic usage
raw_string = r"This is a raw string with a backslash: \\"
print(raw_string)

# Raw strings with newlines
raw_multiline = r"First line\nSecond line"
print(raw_multiline)

# Raw strings with file paths
file_path = r"C:\Users\leo\Development\projects\python_playground\src\basic_types\strings_cells.py"
print(file_path)
# %%
