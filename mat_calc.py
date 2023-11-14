import numpy as np
import pandas as pd

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    
    return np.array(matrix)

def display_matrix(matrix, label):
    df = pd.DataFrame(matrix)
    df.index += 1  # Indexing starts from 1
    df.columns += 1  # Columns start from 1
    print(f"{label} Matrix:")
    print(df)

def matrix_calculator():
    print("Matrix Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    
    choice = int(input("Enter your choice (1/2/3/4): "))
    
    if choice == 1 or choice == 2 or choice == 3:
        matrix1 = input_matrix()
        matrix2 = input_matrix()

    if choice == 1:
        result = np.add(matrix1, matrix2)
        display_matrix(result, "Resultant")
    elif choice == 2:
        result = np.subtract(matrix1, matrix2)
        display_matrix(result, "Resultant")
    elif choice == 3:
        result = np.dot(matrix1, matrix2)
        display_matrix(result, "Resultant")
    elif choice == 4:
        matrix = input_matrix()
        result = np.transpose(matrix)
        display_matrix(result, "Transposed")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    matrix_calculator()
