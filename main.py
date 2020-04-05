n, m, l = 3, 2, 4

mat_1 = [
    [1, 2],
    [2, 4],
    [3, 6]
]

mat_2 = [
    [10, 20, 30, 40],
    [20, 30, 40, 50]
]

res_mat = [[sum([mat_1[row_index][i] * mat_2[i][col_index] for i in range(m)]) for col_index in range(l)] for row_index in range(n)]

print(res_mat)
