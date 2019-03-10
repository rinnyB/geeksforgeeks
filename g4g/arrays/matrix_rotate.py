# https://www.geeksforgeeks.org/rotate-matrix-90-degree-without-using-extra-space-set-2/

def transpose(matr, n):  # inplace transpose
    for i in range(0, n):  # rows
        for j in range(i, n):  # cols
            (matr[i][j], matr[j][i]) = (matr[j][i], matr[i][j])

def reverse_rows(matr, n): # inplace reverse_rows
    for i in range(0, n):
        matr[i].reverse()


def print_matrix(matr, n): # >_>
    for row in matrix:
        for el in row:
            print(el, end=" ")
    print()


cases = int(input())
for case in range(cases):
    n = int(input())
    data = [int(e) for e in input().strip().split(" ")]
    matrix = [data[i: i + n] for i in range(0, n * n, n)]
    transpose(matrix, n)
    reverse_rows(matrix, n)
    print_matrix(matrix, n)
