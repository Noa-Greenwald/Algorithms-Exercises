from q3 import parent

def is_max_heap(arr, i=0, key=lambda x: x):
    n = len(arr)
    for j in range(i + 1, n):
        if key(arr[parent(j)]) < key(arr[j]):
            return False
    return True

if __name__ == "__main__":
    arr1 = [9, 4, 5, 1, 3, 2]
    arr2 = [3, 9, 2, 1, 4, 5]
    print(is_max_heap(arr1))
    print(is_max_heap(arr2))
