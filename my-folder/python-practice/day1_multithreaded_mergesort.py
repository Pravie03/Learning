import threading

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Sort each half using threads
    t1 = threading.Thread(target=lambda: left.sort())
    t2 = threading.Thread(target=lambda: right.sort())

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Test the function
unsorted = [34, 7, 23, 32, 5, 62]
sorted_list = merge_sort(unsorted)
print("Sorted List:", sorted_list)