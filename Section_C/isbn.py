# Software Engineer: RIAAN VAN DEVENTER
# This was programmed for the HyperionDev Freelance Code Reviewer Take-Home Test
# Written on 22 February 2023

#------------------------------------------------------------------------------------------------
# The International Standard Book Number (ISBN) is a unique identifying number given to each published book. 
# ISBNs assigned after January 2007 are 13 digits long (ISBN-13), however books with 10-digit ISBNs are still in wide use.
#
# Create a function that takes a string of numbers (possibly with an X at the end) and...
#
# Return "Invalid" if it is not a valid ISBN-10 or ISBN-13.
# Return "Valid" if it is a valid ISBN-13.
# If it is a valid ISBN-10, convert it into an ISBN-13 and return the ISBN-13 number.
#
# Convert a valid ISBN-10 to ISBN-13 by tacking 978 to the start, then changing the last digit (the check digit) 
# so that the resulting number passes the ISBN-13 check.
#------------------------------------------------------------------------------------------------

#========== Functions for this project ==============
def isbn13(isbn_str):
    # Check if the input is a valid ISBN-10 or ISBN-13
    if len(isbn_str) == 10:
        # Validate ISBN-10
        total = 0
        for i in range(len(isbn_str)):
            # If the 10th digit is 'X', it represents 10
            if isbn_str[i] == 'X':
                total += 10 * (10 - i)
            else:
                total += int(isbn_str[i]) * (10 - i)

        if total % 11 != 0:
            # If the total is not divisible by 11, the ISBN-10 is invalid
            return "Invalid"
        else:
            # Convert ISBN-10 to ISBN-13
            isbn_str = '978' + isbn_str[:-1] # Add the prefix '978'
            total = 0
            for i in range(len(isbn_str)):
                if i % 2 == 0:
                    total += int(isbn_str[i])
                else:
                    total += int(isbn_str[i]) * 3
            isbn_str += str((10 - (total % 10)) % 10) # Calculate the check digit and append it to the ISBN
            return isbn_str

    elif len(isbn_str) == 13:
        # Validate ISBN-13
        total = 0
        for i in range(len(isbn_str)):
            if i % 2 == 0:      # Digits to multiply by 1
                total += int(isbn_str[i])
            else:
                total += int(isbn_str[i]) * 3

        if total % 10 != 0:
            # If the total is not divisible by 10, the ISBN-13 is invalid
            return "Invalid"
        else:
            # If the ISBN-13 is valid, return "Valid"
            return "Valid"

    else:
        # If the input is not a valid ISBN-10 or ISBN-13, return "Invalid"
        return "Invalid"

# ============  MAIN LOGIC - ISBN Validation  ===============

# Read ISBN numbers from input file

# The input file is named isbn_input.txt and contains one ISBN number per line, 
# this code will read each ISBN number, remove any leading/trailing whitespace, 
# and pass it to the isbn13 function to validate and convert it. 
# The result (either "Valid", "Invalid", or the converted ISBN-13 number) will be printed 
# for each ISBN number.

try:
    with open("isbn_input.txt", "r") as file:
        print()
        print("------------  ISBN Number Validation from file isbn_input.txt  -------------")
        for isbn in file:
            isbn_str = isbn.strip() # Remove any leading/trailing whitespace
            result = isbn13(isbn_str)
            print(f"{isbn_str}: {result}")
        print("----------------------------------------------------------------------------")
        print()

except FileNotFoundError:
    print()
    print("Error: input file not found\n")
except IOError:
    print()
    print("Error: could not read input file\n")
except:
    print()
    print("Error: an unknown error occurred\n")
finally:
    file.close() # Close the input file regardless of whether an exception was raised or not

# =================  END PROGRAM LOGIC HERE  ====================

