from q3 import left, right

def max_heapify(arr, i, heap_size, key=lambda x: x):
    l = left(i)
    r = right(i)
    largest = i

    if l < heap_size and key(arr[l]) > key(arr[largest]):
        largest = l
    if r < heap_size and key(arr[r]) > key(arr[largest]):
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size, key)

if __name__ == "__main__":
    arr = [3, 9, 2, 1, 4, 5]
    max_heapify(arr, 0, len(arr))
    print(arr)
