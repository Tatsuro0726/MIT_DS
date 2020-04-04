
N = 2
K = 1
size = 3
M = [['#', '.','#'], ['.','#','.'],['#','.', '#']]
final_size = (size * size)**size

for i in range(size):
    for j in range(size):
        if M[i][j] == '#':
            for r in range(size):
                print(M[i][r], end='')
        else:
            print('.' * size, end='')
    print()