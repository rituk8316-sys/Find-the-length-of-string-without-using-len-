# Program to find the length of a string without using len()
# Author: Your Name
# Description: This program counts characters in a string manually

def string_length(text):
    count = 0

    for char in text:
        count += 1

    return count


# Taking input from user
input_string = input("Enter a string: ")

# Function call
length = string_length(input_string)

# Output
print("Length of string is:", length)
