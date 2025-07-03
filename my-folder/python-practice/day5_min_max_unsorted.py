def find_min_max(arr):
    if not arr:
        return None, None

    smallest = largest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest


# Test
arr = [17, 2, 99, -5, 23]
min_val, max_val = find_min_max(arr)
print(f"Smallest = {min_val}, Largest = {max_val}")