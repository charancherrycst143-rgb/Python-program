
arr = [14, 16, 87, 36, 25, 89, 34]
M, N = 1, 3   # Example values

arr_sorted = sorted(arr)

mth_max = arr_sorted[-M]  
nth_min = arr_sorted[N-1] 

print(f"{M}st Maximum Number =", mth_max)
print(f"{N}rd Minimum Number =", nth_min)
print("Sum =", mth_max + nth_min)
print("Difference =", mth_max - nth_min)
