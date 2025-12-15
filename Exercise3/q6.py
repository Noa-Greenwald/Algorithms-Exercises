from q5 import max_heapify

def build_max_heap(arr, key=lambda x: x):
    heap_size = len(arr)
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(arr, i, heap_size, key)

if __name__ == "__main__":
    arr = [3, 9, 2, 1, 4, 5]
    build_max_heap(arr)
    print(arr)
