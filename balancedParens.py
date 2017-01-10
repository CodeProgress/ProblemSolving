
def has_balanced_parens(a_str):
    stack = []
    for char in a_str:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if is_stack_empty(stack): 
                return False
            else: 
                stack.pop()
    return is_stack_empty(stack)

def is_stack_empty(stack):
    return len(stack) == 0

assert has_balanced_parens("()") == True
assert has_balanced_parens("(")  == False
assert has_balanced_parens(")")  == False
assert has_balanced_parens("())")  == False
assert has_balanced_parens("()(")  == False
assert has_balanced_parens("")  == True
assert has_balanced_parens("abc")  == True
assert has_balanced_parens("(abcd)(efgh)((((((((((()()()()()()()()))))))))))") == True
assert has_balanced_parens("(abcd)(efgh)((((((((((()()()()()()()())))))))))))") == False
