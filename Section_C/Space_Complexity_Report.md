# Report: Space Complexity of ISBN-13 Validator

The space complexity of an algorithm refers to the amount of memory it requires to complete its execution. This report aims to analyze the worst-case space complexity 
of the ISBN-13 validator function implemented in Python.

The ISBN-13 validator function takes as input a string of numbers (possibly with an X at the end) and returns one of three possible outputs:

- "Invalid" if the input is not a valid ISBN-10 or ISBN-13.
- "Valid" if the input is a valid ISBN-13.
- If the input is a valid ISBN-10, convert it into an ISBN-13 and return the ISBN-13 number.

The function works by first checking if the input is a valid ISBN-13. If it is, it returns "Valid". If it is not, it checks if the input is a valid ISBN-10. 
If it is, it converts it into an ISBN-13 and returns the ISBN-13 number. If it is not a valid ISBN-10, it returns "Invalid".

The space complexity of the ISBN-13 validator function depends on several factors, including the size of the input string and the number of intermediate variables 
used in the function. Let's break down the function and analyze the space complexity of each step.

### Step 1: Parsing the Input

The function first parses the input string to remove any leading or trailing whitespace characters. This step requires a small amount of additional memory to store 
the new string without the whitespace characters. 

The space complexity of this step is O(n), where n is the length of the input string.

### Step 2: Validating ISBN-13
The function checks if the input is a valid ISBN-13 by calculating the sum of the product of each digit and its corresponding weight. This step requires a 
constant amount of additional memory to store the sum and the intermediate variables used in the calculation. 

The space complexity of this step is O(1).

### Step 3: Converting ISBN-10 to ISBN-13
If the input is not a valid ISBN-13, the function checks if it is a valid ISBN-10 by calculating the sum of the product of each digit and its corresponding weight. 
This step requires a constant amount of additional memory to store the sum and the intermediate variables used in the calculation. 

The space complexity of this step is also O(1).

If the input is a valid ISBN-10, the function converts it into an ISBN-13 by appending the prefix "978" to the beginning of the string and calculating the check digit. 
This step requires a small amount of additional memory to store the new string with the prefix and the check digit. 

The space complexity of this step is O(n), where n is the length of the input string.

### Overall Space Complexity

The worst-case space complexity of the ISBN-13 validator function is O(n), where n is the length of the input string. 
This worst-case scenario occurs when the input is a valid ISBN-10 that needs to be converted to an ISBN-13. In this case, 
the function needs to store the original input string, the new string with the prefix and the check digit, and several intermediate variables used in the calculations.

In most cases, however, the function requires only a small amount of additional memory to store the input string and a few intermediate variables. 
Therefore, the overall space complexity of the ISBN-13 validator function can be considered to be O(1) for practical purposes.

### Conclusion

In conclusion, the worst-case space complexity of the solution presented here for ISBN verification is O(n), where n is the length of the input ISBN string. 
This space complexity is proportional to the input size, meaning that the amount of memory used by the algorithm increases linearly with the size of the input.

However, the solution does not create any data structures or variables that scale with the input size, making it memory efficient. 
Therefore, the algorithm should be able to handle large inputs without running into any memory issues.

Overall, the space complexity of the solution is efficient and proportional to the size of the input, making it a good choice for ISBN verification tasks.
