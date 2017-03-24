"""
A string can be "reduced" by deleting pairs of adjacent letters.
This process is repeated until no pairs of adjacent letters exist.
For example: 'ffz' can be reduced to 'z'
'zaaz' -> 'Empty String'
'abbcddeffg' -> 'aceg'
"""

def reduce_string(a_str):
    if len(a_str) == 0:
        return "Empty String"
    
    if not can_be_reduced(a_str):
        return a_str
    
    return reduce_string(delete_first_pair_of_adj_letters(a_str))

def can_be_reduced(a_str):
    if len(a_str) <= 1:
        return False
    for i in range(len(a_str)-1):
        if a_str[i] == a_str[i+1]:
            return True
    return False

def delete_first_pair_of_adj_letters(a_str):
    if len(a_str) <= 1:
        return a_str
    for i in range(len(a_str)-1):
        if a_str[i] == a_str[i+1]:
            return a_str[:i] + a_str[i+2:]
    return a_str

assert reduce_string("ffz") == "z"
assert reduce_string("zaaz") == "Empty String"
assert reduce_string("abbcddeffg") == "aceg"
