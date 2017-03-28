
bracket_match_dict = {'(': ')', '{': '}', '[': ']'}

def are_brackets_balanced(brackets):
    stack = []
    for b in brackets:
        if b in bracket_match_dict:
            stack.append(b)
        else:
            if not stack:
                return False
            if bracket_match_dict[stack.pop()] != b:
                return False
    return len(stack) == 0

a = '[{[()]}]'
b = '{{[(])}'
c = '{([[(())]])}'
assert are_brackets_balanced(a)
assert not are_brackets_balanced(b)
assert are_brackets_balanced(c)
