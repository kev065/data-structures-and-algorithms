def is_balanced(expression):

    # Initialize an empty list to use as a stack
    stack = []

    # Define a dictionary to map opening brackets to their corresponding closing brackets
    brackets = {"(": ")", "{": "}", "[": "]"}
    
    # Iterate over each character in the expression
    for char in expression:

        # If the character is an opening bracket, push it onto the stack
        if char in brackets:
            stack.append(char)

        # If the stack is empty or the top of the stack does not match the closing bracket, return False
        elif len(stack) == 0 or brackets[stack.pop()] != char:
            return False
    
    # If the stack is empty after processing the entire expression, the brackets are balanced
    return len(stack) == 0


expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
