num = int(input('Input "num": '))
matrix = []

print('num=', num)
print('matrix=', matrix)

for i in range(num):
    matrix.append(list(map(int, input('Input raw of matrix'
                                      ' (separate <space>):').split())))


print('matrix=', matrix)


for i in matrix:
    for j in i:
        print(j, end='')
    print()

# primary_diagonal = 0
# secondary_diagonal = 0

    primary_diagonal = sum(matrix[i][i] for i in range(num))
    secondary_diagonal = sum(matrix[i][num - i - 1] for i in range(num))


result = abs(primary_diagonal - secondary_diagonal)

print('diagonal_difference=', result)
