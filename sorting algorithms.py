def insertionsort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0: # comparing
            arr[j - 1], arr[j] = arr[j], arr[j - 1] # swapping
            j -= 1 # comparing elements on the left as well until in place

l = [5, 3, 7, 21, 4, 2, 8]
insertionsort(l)
print(l)

arr = ["caa", "Ba", "ab", "bb"]


def quicksort(lst):
    if not lst:
        return []
    n = quicksort([i for i in lst[1:] if i < lst[0]]) + [lst[0]] + quicksort([i for i in lst[1:] if i >= lst[0]])
    return (n)
print(quicksort(arr))