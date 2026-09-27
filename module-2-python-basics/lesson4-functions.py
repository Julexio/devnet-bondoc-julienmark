"""
Module 4 — Lesson 1: Functions
Student: Bondoc, Julien Mark
Date: September 26, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
In fact, you can liken a function to a button
which is unique and customized to perform some
tasks for you. This means that instead of typing
the same 10 lines of codes again and again, you
just package them together, give them a name and
simply press the button whenever you want to use it.
You will feed the inputs and the function will
return the results to you.
============================================
KEY VOCABULARY
============================================
- function: This is a piece of code that is
designed to accomplish some particular job when invoked.

- parameter: This is the variable used inside
the function to accept input data from outside.

- argument: This is the real value that is
supplied to a function as input.

- return: This is the keyword used to send the
output result to the code that invoked the function.

- scope: This refers to the range of access for a
particular variable in a code.
============================================
MY OWN EXAMPLE(S)
============================================
"""
def apply_discount(price, discount_percent):
    savings = price * (discount_percent / 100)
    final_price = price - savings
    return final_price

apple_price = apply_discount(500, 10)
samsung_price = apply_discount(2500, 20)

print("Apple Final Price:", apple_price)
print("Samsung Final Price:", samsung_price)
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Not using return or getting confused between print() and return

One common problem in working with functions is
using print() in the body of the function,
rather than returning the value of a function.
When one prints() the value of the function,
the value appears on the screen, but cannot be
stored in a variable or used in further computations.
When trying to store the output of a function without
return, your variable will contain either None or empty value.
Prevent using print() only when you wish to display
some information directly onto the screen; otherwise,
always use return.
============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
""
