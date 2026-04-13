def comparator(a, b):
    if type(a) != type(b):
        if isinstance(a, (int, float)) and isinstance(b, str):
            return False
        if isinstance(a, str) and isinstance(b, (int, float)):
            return True

    return b > a


def bubble_sort(massiv, cmp=None):
    if cmp is None:
        cmp = lambda a, b: (b > a)
    if len(massiv) == 0:
        return
    n = len(massiv)
    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if cmp(massiv[j],massiv[j + 1]):
                massiv[j], massiv[j + 1] = massiv[j + 1], massiv[j]
                swapped = True
        if not swapped:
            break


r_sorting = [4, 4, 8, 4, 2, 5, "HI", 'g', 0.67, 'a']
bubble_sort(r_sorting, cmp=comparator)
print(r_sorting)
