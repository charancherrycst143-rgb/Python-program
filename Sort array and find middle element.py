
arr = [90, -90, 80, 66, 78, 10]
arr_sorted = sorted(arr)
print("Sorted Array (Ascending):", arr_sorted)
n = len(arr_sorted)
mid = arr_sorted[n // 2] if n % 2 != 0 else arr_sorted[(n//2) - 1]
print("Middle element:", mid)
