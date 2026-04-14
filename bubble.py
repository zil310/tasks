r_sorting = [4, 4, 8, 4, 2, 5, 0, 54, 2, 23, 1, 0.5, 'j', 'HI', 'sdgsdg','sjdkfhsjkf', 'sdf']

#написать проверку ассертами
def bubble_sort(massiv, key=None):
    if key is None:
        key = lambda x: x
    if len(massiv) == 0:
        return
    n = len(massiv)
    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if key(massiv[j]) > key(massiv[j + 1]):
                massiv[j], massiv[j + 1] = massiv[j + 1], massiv[j]
                swapped = True
        if not swapped:
            break


bubble_sort(r_sorting, key=str)
print(r_sorting)
