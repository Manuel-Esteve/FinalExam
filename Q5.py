# Q5:

import re

def find_pattern_occurrences(text):
    """
    Finds all occurrences of a pattern that starts with 'C',
    has unlimited letters in between, and ends with 'jeb'.
    :param text: The text to search in.
    :return: The number of matches found.
    """
    pattern = r'C\w*jeb' # Establish the pattern
    matches = re.findall(pattern, text) # Find matches
    return len(matches) # Return Matches

# Example:
text_sample = "Cajeb Cbjeb Ccjeb Cdjeb"
print(find_pattern_occurrences(text_sample))