from random_tuples import create_random_tuples


# ---------------------------------------
# סעיף א – פונקציה למציאת מינימום
# ---------------------------------------
def find_min(a, key):
    if not a:
        return None

    min_item = a[0]
    min_key_val = key(a[0])

    for item in a[1:]:
        val = key(item)
        if val < min_key_val:
            min_key_val = val
            min_item = item

    return min_item


# פונקציה למציאת מקסימום (לסעיף ב')
def find_max(a, key):
    if not a:
        return None

    max_item = a[0]
    max_key_val = key(a[0])

    for item in a[1:]:
        val = key(item)
        if val > max_key_val:
            max_key_val = val
            max_item = item

    return max_item


# ---------------------------------------
# סעיף ב – תכנית מלאה
# ---------------------------------------
def main():
    # יצירת מערך עם 100 tuples מסוגים [int, float, str]
    data = create_random_tuples(100, 3, [int, float, str])

    # הפריט השלישי הוא x[2] – מחרוזת
    key_func = lambda x: x[2]

    # חיפוש מינימום ומקסימום לפי הפריט השלישי
    min_item = find_min(data, key=key_func)
    max_item = find_max(data, key=key_func)

    # הדפסת הערכים עצמם (לא כל הטופל)
    print(f"min={min_item[2]}")
    print(f"max={max_item[2]}")


if __name__ == "__main__":
    main()
