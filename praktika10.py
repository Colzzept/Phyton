with open(r"C:\Users\dimat\OneDrive\Desktop\gg\tabl.txt", "r") as f:
    matrix = []
    for line in f:
        cleaned_line = line.replace('[', '').replace(']', '').replace(',', '')
        r = [int(x) for x in cleaned_line.split()]
        matrix.append(r)  

def transpose_matrix(matrix):
    transposed = [[0] * len(matrix) for i in range((len(matrix)))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transposed[j][i] = matrix[i][j]
    return transposed

res = transpose_matrix(matrix)

with open(r"C:\Users\dimat\OneDrive\Desktop\gg\tabl2.txt", "w") as matrix2:
    for line in res:
        line_str = ' '.join(map(str, line)) + '\n'
        matrix2.write(line_str)

print("Файл создан")