"""
Solution for the Rick riddle problem    
"""

import string
from copy import deepcopy
from itertools import product


def has_no_double_letters(text):
    """
    Checks if a string has no consecutive letters of the same kind.

    Args:
        text: The string to check.

    Returns:
        True if there are no double letters, False otherwise.
    """
    # Previous character is None when index is 0
    previous = None

    for char in text:
        # ? char is ignored
        if char == "?":
            return True

        # When the repetion is detected, a False is returned
        if char == previous:
            return False

        # The next iteration changes the prevoius character
        previous = char

    return True


def logic(riddle, letters):
    """
    Replaces question marks in a string with lowercase letters without consecutive duplicates.

    Args:
        riddle: The string with question marks.

    Returns:
        A string with the question marks replaced by lowercase letters, avoiding duplicates.
    """
    riddle_copy = deepcopy(riddle)

    for replace in letters:
        index = riddle_copy.find("?")
        riddle_copy = riddle_copy[:index] + replace + riddle_copy[index + 1 :]

        if not has_no_double_letters(riddle_copy):
            return None

    return riddle_copy


def solution(riddle):
    """
    This function replaces all question marks with lowercase letters in a way that
    no two consecutive letters are the same. It returns a list of all possible
    solutions.

    Args:
        riddle (str): The string containing the puzzle with letters and question marks.

    Returns:
        list: A list of strings representing valid solutions to the puzzle.

    Raises:
        ValueError: If the given string contains invalid characters, has
            duplicated letters in the original riddle, or exceeds the maximum
            allowed length of 100,000 characters.
    """
    # List in which the answers will be stored
    outcomes = []

    # Checks if riddle is lowercase and only has ? as special character
    valid_letters = string.ascii_lowercase

    for char in riddle:
        if char not in valid_letters + "?":
            raise ValueError(f"{riddle} has not valid chars")

    # Checks if there is duplicated letters in the original riddle
    if not has_no_double_letters(riddle):
        raise ValueError(f"{riddle} has duplicated letters")

    # Checks if the lenght of the string is max = 100000
    if len(riddle) > 100000:
        raise ValueError(f"{riddle} too long, 100000 is the maxiumum lenght for riddle")

    # Implement the logic
    # Extract the maximum number of permutations
    max_count = riddle.count("?")
    perms = product(valid_letters, repeat=max_count)

    # Calls the logic function for each permutation
    for letters in perms:
        result = logic(riddle, letters)
        if result:
            outcomes.append(result)

    return outcomes
