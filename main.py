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


def dot_product_element(mat_a, mat_b, ri, ci):
    return 0


res_mat = [[dot_product_element(mat_1, mat_2, row_index, col_index) for col_index in range(l)] for row_index in range(n)]

print(res_mat)
