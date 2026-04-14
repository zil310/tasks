import random
import bubble

localElement = []
bubble.bubble_sort(localElement)


def check(data):
    for i in range(0, len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


check(localElement)
assert check(localElement), 'Error'

localElement = ['0'] * 100
bubble.bubble_sort(localElement)
assert check(localElement), 'Error'

localElement = [1]
bubble.bubble_sort(localElement)
assert check(localElement), 'Error'

localElement = [1, 2]
bubble.bubble_sort(localElement)
assert check(localElement), 'Error'

localElement = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bubble.bubble_sort(localElement)
assert check(localElement), 'Error'

for i in range(0, 9):
    array = []
    for j in range(0, 10000):
        array.append(random.randint(0, 1000000))

# print(array)
localElement = [array]
bubble.bubble_sort(localElement)
assert check(localElement), 'Error'

localElement = ['c', 'j', 'k', 't', 'b']
bubble.bubble_sort(localElement)
assert check(localElement), 'Error'

localElement = ['strong', 'sebgbsdfva', 'HI']
bubble.bubble_sort(localElement)
assert check(localElement), 'Error'

localElement = [0.3, 0.4, 0.2, 0.1]
bubble.bubble_sort(localElement)
assert check(localElement), 'Error'
