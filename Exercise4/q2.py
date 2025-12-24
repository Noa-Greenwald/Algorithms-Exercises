def partition(arr, left, right, key):
    pivot = arr[right]
    pivot_key = key(pivot)
    i = left
    for j in range(left, right):
        if key(arr[j]) <= pivot_key:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_kth(arr, left, right, k, key=lambda x: x):
    if left <= right:
        pivot_index = partition(arr, left, right, key)

        if pivot_index == k:
            return arr[pivot_index]
        elif k < pivot_index:
            return quick_kth(arr, left, pivot_index - 1, k, key)
        else:
            return quick_kth(arr, pivot_index + 1, right, k, key)



arr1 = [7, 2, 1, 6, 8, 5, 3, 4]

print(quick_kth(arr1.copy(), 0, len(arr1) - 1, 0))  # הקטן ביותר → 1
print(quick_kth(arr1.copy(), 0, len(arr1) - 1, 3))  # הרביעי בגודלו → 4
print(quick_kth(arr1.copy(), 0, len(arr1) - 1, 7))  # הגדול ביותר → 8

arr2 = [(1, 5), (2, 3), (3, 1)]
print(quick_kth(arr2.copy(), 0, len(arr2) - 1, 0, key=lambda x: x[1]))  # מחזיר (3, 1)
