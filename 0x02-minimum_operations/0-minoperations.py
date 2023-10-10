#!/usr/bin/python3
'''Module for Minimum Operations challenge in Python3.'''

def minOperations(n):
    '''Calculates the fewest number of operations
    to achieve n H characters.
    
    Parameters:
    - n: The target number of H characters.

    Returns:
    - An integer: Number of operations needed
    If n is impossible to achieve, return 0.
    '''
    pasted_chars = 1  # Initial number of H characters in the file
    clipboard = 0  # Number of H characters copied to clipboard
    counter = 0  # Operations counter

    while pasted_chars < n:

        # If clipboard is empty, copy all H characters from the file
        if clipboard == 0:
            clipboard = pasted_chars
            counter += 1

        # If only one H character in file, paste from clipboard
        if pasted_chars == 1:
            pasted_chars += clipboard
            counter += 1
            continue

        remaining = n - pasted_chars  # Num of H xters needed to reach target
        
        # Check if achieving target is impossible
        if remaining < clipboard:
            return 0

        # If the target isn't a multiple of the current number of H characters
        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            counter += 1
        else:
            # Copy and paste the H characters
            clipboard = pasted_chars
            pasted_chars += clipboard
            counter += 2

    # Return the number of operations if target is achieved
    if pasted_chars == n:
        return counter
    else:
        return 0

