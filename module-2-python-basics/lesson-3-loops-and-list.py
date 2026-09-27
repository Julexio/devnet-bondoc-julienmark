"""
Module 2 — Lesson 3: Loops & Lists
Student: [your name]
Date: [date]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Consider a list similar to a grocery list
written on paper. It simply consists of items
kept in a definite order. A loop can be considered
as hiring an assistant who runs through the list
and does something to each and every item of the list.
There is no need to write the same thing again and
again. Just write once and let the computer do the rest.
============================================
KEY VOCABULARY
============================================
- list: A sequence of values or objects saved
into one variable within square brackets []

- for loop: A loop in which some operations
are executed for a fixed number of times;
often done by iterating through each object in the list.

- while loop: A loop in which repetition happens
repeatedly until a certain condition becomes False.

- index: The number representing the position
of any object in the list; it starts from zero for the first object.

- iteration:  Each time a loop is executed.

- Infinite loop: A situation in which a
while loop runs infinitely as the condition does not become False.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

student_fees = [10, 20, 50, 100]
total_collected = 0
print("Processing payments...")
for fee in student_fees:
    total_collected += fee
    print(f"Collected: ${fee}")
print(f"Total Revenue: ${total_collected}")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Off-by-one bugs and forgetting zero-based index counting.

One frequent problem is the fact that lists start
counting from index 0 and not from 1. When the list
contains 4 elements, then their indexes will be 0, 1, 2, 3.
Accessing my_list[4] will return the "IndexOutOfBounds"
exception because there is no such index.One other
serious problem is writing while loop and not changing
the loop control variable, which leads to infinite loop.

How to prevent it: Remember that the length of the
list is always one more than its maximum index number.
When using while loops, make sure to change the state
within the body of the loop so that it could evaluate to False.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
