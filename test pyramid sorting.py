import random
import pyramid

localElement = []
pyramid.heap_sort(localElement)


def check(data):
    for i in range(0, len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


check(localElement)
print(check(localElement))

localElement = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pyramid.heap_sort(localElement)
check(localElement)
print(check(localElement))

localElement = [1]
pyramid.heap_sort(localElement)
check(localElement)
print(check(localElement))

localElement = [1, 2]
pyramid.heap_sort(localElement)
check(localElement)
print(check(localElement))

localElement = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pyramid.heap_sort(localElement)
check(localElement)
print(check(localElement))

for i in range(0, 9):
    array = []
    for j in range(0, 10000):
        array.append(random.randint(0, 1000000))

#print(array)
localElement = [array]
pyramid.heap_sort(localElement)
check(localElement)
print(check(localElement))

localElement = ['c', 'j', 'k', 't', 'b']
pyramid.heap_sort(localElement)
check(localElement)
print(check(localElement))

localElement = ['strong', 'sebgbsdfva', 'HI']
pyramid.heap_sort(localElement)
check(localElement)
print(check(localElement))

localElement = [0.3, 0.4, 0.2, 0.1]
pyramid.heap_sort(localElement)
check(localElement)
print(check(localElement))