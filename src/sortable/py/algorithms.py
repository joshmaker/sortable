__all__ = ("bubble", "insertion", "quicksort")


def _compare(a, b, key=None):
    if key is None:
        return a < b
    return key(a) < key(b)


def bubble(arr, key=None):
    length = len(arr)
    if length <= 1:
        return

    for _ in range(0, length):
        for i in range(1, length):
            if _compare(arr[i], arr[i - 1], key):
                arr[i - 1], arr[i] = arr[i], arr[i - 1]


def insertion(arr, key=None):
    if len(arr) <= 1:
        return

    for i in range(1, len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and _compare(item, arr[j], key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item


def quicksort(arr, key=None):
    length = len(arr)
    if length <= 1:
        return

    less = []
    greater = []
    pivot = arr[length - 1]

    index = 0
    for i in range(0, length):
        item = arr[index]
        if _compare(item, pivot, key):
            less.append(arr.pop(index))
        elif _compare(pivot, item, key):
            greater.append(arr.pop(index))
        else:
            index += 1

    quicksort(less, key)
    quicksort(greater, key)

    # prepend `less` and append `greater` to the list to change it in place
    arr[:0] = less
    arr[length:] = greater
    return arr
