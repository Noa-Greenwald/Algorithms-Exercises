from q6 import build_max_heap
from q5 import max_heapify

def heap_sort(arr, key=lambda x: x):
    build_max_heap(arr, key)
    heap_size = len(arr)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, 0, heap_size, key)

if __name__ == "__main__":
    arr = [3, 9, 2, 1, 4, 5]
    heap_sort(arr)
    print(arr)
