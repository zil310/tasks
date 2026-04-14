sorting = [1,5,6,45,23,564,8,8,564,435,234,534,567,678,0]


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def creating_a_tree(n, i, array):
    largest = i
    l_branch = i * 2 + 1
    r_branch = i * 2 + 2
    if l_branch < n and array[largest] < array[l_branch]:
        largest = l_branch

    if r_branch < n and array[largest] < array[r_branch]:
        largest = r_branch
    if largest != i:
        swap(array, largest, i)
        creating_a_tree(n, largest, array)


def heap_sort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        creating_a_tree(n, i, array)

    for i in range(n - 1, 0, -1):
        swap(array, i, 0)
        creating_a_tree(i, 0, array)


heap_sort(sorting)
print(sorting)