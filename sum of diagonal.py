
matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(len(matrix) ** 0.5)  

diagonal = []
for i in range(n):
    diagonal.append(matrix[i * n + i]) 

print("Diagonal elements are:", diagonal)
print("Sum of diagonal elements =", sum(diagonal))
