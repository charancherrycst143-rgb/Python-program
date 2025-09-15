
A = [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3]]

B = [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3]]

C = [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3]]

result_AB = [[0, 0, 0] for _ in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            result_AB[i][j] += A[i][k] * B[k][j]
final_result = [[0, 0, 0] for _ in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            final_result[i][j] += result_AB[i][k] * C[k][j]
print("Multiplication of the 3 matrices:")
for row in final_result:
    print(" ".join(map(str, row)))
