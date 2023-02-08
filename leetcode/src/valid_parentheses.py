"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""


def is_valid(s: str) -> bool:
    # pairs = {'(': ')', '[': ']', '{': '}', ')': 'q', ']': 'q', '}': 'q'}
    pairs = {'(': ')', '[': ']', '{': '}'}
    if len(s) == 1:
        return False
    parentheses = list(s)
    while True:
        i, l = 0, len(parentheses)
        while i < len(parentheses)-1:
            if parentheses[i] not in pairs:
                i += 1
                continue
            if parentheses[i+1] == pairs[parentheses[i]]:
                parentheses.pop(i)
                parentheses.pop(i)
            else:
                i += 1
        if not parentheses:
            return True
        if len(parentheses) == l:
            return False


# --------------------------------------------------------------
def is_valid1(s: str) -> bool:
    # Create a pair of opening and closing parentheses.
    pairs = {'(': ')', '[': ']', '{': '}'}
    # Create stack data structure.
    stack = []
    # Traverse each character in input string.
    for idx in s:
        # If open parentheses are present, append it to stack.
        if idx in '([{':
            stack.append(idx)
        # If the character is closing parentheses, check that the same type opening parentheses is being pushed
        # to the stack or not. If not, we need to return false.
        elif len(stack) == 0 or idx != pairs[stack.pop()]:
            return False
    # At last, we check if the stack is empty or not.
    # If the stack is empty it means every opened parenthesis is being closed and we can return true,
    # otherwise we return false.
    return len(stack) == 0


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))

print(is_valid1("()"))
print(is_valid1("()[]{}"))
print(is_valid1("(]"))
print(is_valid1("([)]"))
