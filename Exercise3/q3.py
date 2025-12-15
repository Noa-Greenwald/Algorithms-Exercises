#א
def parent(i):
    return (i - 1) // 2
#ב
def left(i):
    return 2 * i + 1
#ג
def right(i):
    return 2 * i + 2

if __name__ == "__main__":
    print(parent(3))
    print(left(1))
    print(right(1))
