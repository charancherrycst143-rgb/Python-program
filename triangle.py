rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")

    # Print ascending numbers
    for j in range(i, i + i):
        print(j, end=" ")

    # Print descending numbers
    for j in range(i + i - 2, i - 1, -1):
        print(j, end=" ")

    print()