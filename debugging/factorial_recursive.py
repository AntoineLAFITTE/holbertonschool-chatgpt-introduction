#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
    n (int): The non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer n. If n is 0, returns 1 since 0! is defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the integer argument from the command line,
# calculate its factorial, and print the result

f = factorial(int(sys.argv[1]))
print(f)

