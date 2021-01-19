# Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the
# lines using a regular expression and the findall() method
# Compute the average of the numbers and
# print out the average as an integer.
import re
container = []
numbers = []
fhandler = open('mbox-short.txt')
for line in fhandler:
    container += re.findall("^New Revision: *([0-9]+)",line)
for string in container:
    numbers.append(int(string))
average = (sum(numbers)/ len(numbers))
print(numbers)
print(int(average))