"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Bondoc, Julien Mark
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
In simple terms, control flow is about telling
your code what decision to make. For example,
when crossing the road, there’s a set of rules
that you follow: IF the light is green, then
move on; ELIF the light is yellow, then stop;
ELSE (in case the light is red), then don’t
move. Without control flow, a program would
blindly run every line from the beginning to
the end.
============================================
KEY VOCABULARY
============================================
- condition: A statement or an inquiry which
gives either true or false

- if / elif / else: The key words which make
up the basis of an “if” statement – “if”
checks whether the primary condition is
valid, “elif” checks further conditions
if the preceding ones are not valid,
“else” is the alternative case when
none of the conditions is valid.

- comparison operator: Symbols used for
comparing two operands (such as ==, !=, >, <, >=, <=).

- boolean expression: An expression which gives
a true or a false value as a result.

- Logical operators: “And”, “or” and “not” operators.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

user_role = "admin"
is_logged_in = True

if not is_logged_in:
    print("Access Denied: Please log in first.")
elif user_role == "admin":
    print("Welcome back, Admin! Redirecting to full control dashboard...")
elif user_role == "editor":
    print("Welcome! Redirecting to content management panel...")
else:
    print("Welcome! Redirecting to standard view...")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)

Using the single equals = sign, instead of a
double equals == sign in conditions.

One of the most popular mistakes made by beginners
is using if age = 18: instead of if age == 18:.
One equals sign means setting a value in a variable,
and two equals signs mean checking the equality of
two values. For example, in Python language, the use
of = sign in a condition leads to a syntax error,
but in PHP or C languages it will be the accidental
reassignment of a variable and some strange bugs will
happen as the block will be executed anyway.

How to avoid it: Don't forget about the difference
between assignment and comparison operators.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
