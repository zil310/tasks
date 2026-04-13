def is_balanced(expression):
    stack = []
    # Словарь: закрывающая -> открывающая
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    # Множество открывающих скобок для быстрой проверки
    opening = set(pairs.values())

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

bracket = input('Enter your brackets:')
print(is_balanced(bracket))