def highest_product(arr):
    arr.sort()
    
    # Case 1: Top 3 positive numbers
    prod1 = arr[-1] * arr[-2] * arr[-3]

    # Case 2: Two large negatives * largest positive
    prod2 = arr[0] * arr[1] * arr[-1]

    return max(prod1, prod2)


# Test
numbers = [1, 10, -5, 1, -100]
print("Highest Product of 3 numbers:", highest_product(numbers))