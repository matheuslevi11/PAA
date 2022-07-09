def remove_option(options, opt):
    options.remove(opt)
    return options

def viable(matrix):
    # Verificando soma das linhas
    line = 0
    while line < 3:
        sum = 0
        for j in range(3):
            if matrix[line][j] == 0:
                sum = 15
                break
            sum += matrix[line][j]
        if sum != 15:
            return False
        line += 1
    # Verificando soma das colunas
    column = 0
    while column < 3:
        sum = 0
        for i in range(3):
            if matrix[i][column] == 0:
                sum = 15
                break
            sum += matrix[i][column]
        if sum != 15:
            return False
        column += 1
    # Verificando soma da diagonal principal
    sum = 0
    for i in range(3):
        if matrix[i][i] == 0:
                sum = 15
                break
        sum += matrix[i][i]
    if sum != 15:
        return False
    # Verificando soma da diagonal secundária
    sum = 0
    for i in range(3):
        if matrix[i][2-i] == 0:
                sum = 15
                break
        sum += matrix[i][2-i]
    if sum != 15:
        return False
    
    return True


def magic_cube(matrix, i, j, options):
    if i == 3:
        print(matrix)
        return

    for opt in options:
        matrix[i][j] = opt
        if viable(matrix):
            if j == 2:
                magic_cube(matrix, i+1, 0, remove_option(options.copy(), opt))
            else:
                magic_cube(matrix, i, j+1, remove_option(options.copy(), opt))
        matrix[i][j] = 0


if __name__ == '__main__':
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(0)
    
    magic_cube(matrix, 0, 0, list(range(1, 10)))
    