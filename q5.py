import random
import string

def insertion_sort(a, key=None):
    if key is None:
        key = lambda x: x

    n = len(a)

    for i in range(1, n):
        current_item = a[i]
        current_key = key(current_item)
        j = i - 1
        while j >= 0 and key(a[j]) > current_key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = current_item


def generate_random_string(length=5):
    """יוצר מחרוזת אקראית באורך נתון."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_float():
    """יוצר מספר ממשי אקראי."""
    return random.uniform(1.0, 100.0)


def generate_random_int():
    """יוצר מספר שלם אקראי."""
    return random.randint(1, 1000)


def generate_random_tuple():
    """יוצר tuple אקראי: (str, float, int)."""
    return (
        generate_random_string(),
        generate_random_float(),
        generate_random_int()
    )


if __name__ == "__main__":

    # יצירת רשימת בסיס של 10 tuples אקראיים
    base_list = [generate_random_tuple() for _ in range(10)]

    print("--- רשימת בסיס מקורית (10 tuples [str, float, int]) ---")
    for item in base_list:
        print(item)
    print("-" * 50)

    # 1. מיון לפי הפריט הראשון (מחרוזת, אינדקס 0)
    list1 = base_list[:]  # יצירת עותק
    key_func_str = lambda x: x[0]

    print("## 1. מיון לפי הפריט הראשון (מחרוזת)")
    insertion_sort(list1, key=key_func_str)
    for item in list1:
        print(item)
    print("-" * 50)

    # 2. מיון לפי הפריט השני (Float, אינדקס 1)
    list2 = base_list[:]  # יצירת עותק
    key_func_float = lambda x: x[1]

    print("## 2. מיון לפי הפריט השני (float)")
    insertion_sort(list2, key=key_func_float)
    for item in list2:
        print(item)
    print("-" * 50)

    # 3. מיון לפי הפריט השלישי (Integer, אינדקס 2)
    list3 = base_list[:]  # יצירת עותק
    key_func_int = lambda x: x[2]

    print("## 3. מיון לפי הפריט השלישי (integer)")
    insertion_sort(list3, key=key_func_int)
    for item in list3:
        print(item)
    print("-" * 50)