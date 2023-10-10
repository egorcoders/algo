# def create_distance_matrix(N, M):
#     matrix = [[0] * M for _ in range(N)]
#
#     for i in range(N):
#         for j in range(M):
#             distance = min(i, N - i - 1, j, M - j - 1)
#             matrix[i][j] = distance
#
#     return matrix
#
# # Пример использования
# N = 5
# M = 5
#
# distance_matrix = create_distance_matrix(N, M)
#
#
# # Вывод матрицы
# for row in distance_matrix:
#     print(row)

#
# #
# def shool(x, y):
#     h = [0] * y
#     f = []
#
#     for _ in range(x):
#         f.append(h)
#
#     for i in range(x):
#         for j in range(y):
#             d = min(i, x - i - 1, j, y - j - 1)
#             f[i][j] = d
#     return f
#
#
# ans = shool(7, 8)
# for s in ans:
#     print(s)
vacation_selfie = ['a', 'b'] * 10
lst = sum([1 for a in vacation_selfie if a == 'a'])
print(lst)
