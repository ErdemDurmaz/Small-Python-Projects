'''
Question: Write a program which will find all such numbers which are divisible by
7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: Consider use range(#begin, #end) method

'''
numbers = range(2000,3201)
for n in numbers:
    if n % 5 == 0:
        continue
    if n % 7 == 0:
            print(n)