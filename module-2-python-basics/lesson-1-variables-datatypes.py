"""
Module 2 — Lesson 1: Variables & Data Types
Student: Bondoc, Julien Mark
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================

Consider variables to be storage containers
labeled by name in your room, while the data
types represent what actually goes into the
container. Can you store soup in a shoebox
made of paper? Similarly, in programming,
the purpose of the variable is to store data
that can be accessed later, while the data type
informs the computer about the type of data
in the variable,

============================================
KEY VOCABULARY
============================================
- variable: A name assigned to store information in a computer program
- data type: The type or classification of information stored in a variable
- int: Abbreviation for interger, which refers to whole numbers without decimals (ex: 5, -8)
- float: Abbreviation for floating-point number, which refers to numbers with decimals (ex: 3.14, 19.99).
- string: Characters forming text information enclosed by quotation marks (ex: "Hello World").
- boolean: A data type containing only two possible values: True or False.
- array / list: A collection containing multiple values in a single variable.
============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
username = "Jules"
user_age = 21
account_balance = 120.50
is_active_member = True

print("User:", username)
print("Balance: $", account_balance)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Incorrect data type when working with calculations
and outputting text.

The most common mistake is adding string and
numerical values without converting them into
another data type, for example, "Score: " + 100
in Python or adding user input from a web form
in numeric format, but not converting it before
that. By default, user input in the web form is
stored as a string, so "10" + "5" returns 10
instead of 15.

How to fix it: Verify the data type of each
variable and convert the string into the
appropriate format using available functions.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
