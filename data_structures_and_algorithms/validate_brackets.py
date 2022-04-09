from data_structures_and_algorithms.stack_and_queue import Queue,Stack


def validate_brackets(text):
    stack = Stack()
    for char in text:
        if char == '[' or char == '{' or char == '(':
            stack.push(char)
            continue
        if char == ']':
            if stack.is_empty() is False and stack.peek() == '[':
                stack.pop()
                continue
            else:
                return False
        if char == '}':
            if stack.is_empty() is False and stack.peek() == '{':
                stack.pop()
                continue
            else:
                return False
        if char == ')':
            if stack.is_empty() is False and stack.peek() == '(':
                stack.pop()
                continue
            else:
                return False

    return stack.is_empty()



if __name__ == "__main__":
    print(validate_brackets("{}"))
    print(validate_brackets("({})"))
    print(validate_brackets("(){}[]"))
    print(validate_brackets("(cooode)[{fellow}]"))
    print(validate_brackets("({)"))
    print(validate_brackets("(]("))
    print(validate_brackets("{(})"))
    print(validate_brackets("][]"))

