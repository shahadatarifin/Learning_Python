m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

l = [
    [1, 2, 1],
    [6, 2, 3],
    [4, 2, 1]
]

c = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        for k in range(3):
            c[i][j] = c[i][j] + (m[i][j]*l[k][j])
print(c)