import random

def create_matrix(rows, cols, min_val=-100, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Вывод матриц
def print_matrix(matrix, name):
    print ("Матрица ", name)
    for row in matrix:
        print([f"{x:4}" for x in row])

# Сложение матриц
def add_matrices(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("Размерности матриц не совпадают")
    
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

if __name__ == "__main__":
    m1 = create_matrix(10, 10)
    m2 = create_matrix(10, 10)
    
    print_matrix(m1, "A")
    print_matrix(m2, "B")
    
    m3 = add_matrices(m1, m2)
    print_matrix(m3, "A+B")
    