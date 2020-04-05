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

res_mat = [[sum([mat_1[i][j] * mat_2[j][k] for j in range(m)]) for k in range(l)] for i in range(n)]

print(res_mat)
