if __name__ == "__main__":
    pass 
   # appels de fonction

def several_zeros():
    return [0] * 10
    
if __name__ == "__main__":
    print(several_zeros()) 

def several_zeros_custom(nb_zeros):
    return [0] * nb_zeros

def matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]

if __name__ == "__main__":
    print(matrix(3, 4))  

class Matrix:
    def __init__(self, rows, cols):
        self._matrix = [[0] * cols for _ in range(rows)]
    
    def get_value(self, row, col):
        if row < 0 or col < 0 or row >= len(self._matrix) or col >= len(self._matrix[0]):
            raise IndexError("Index hors de la matrice")
        return self._matrix[row][col]
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self._matrix == other._matrix

if __name__ == "__main__":
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    
    print(m1 == m2)  

    print(m1.get_value(1, 2))  

    try:
        print(m1.get_value(2, 3)) 
    except IndexError as e:
        print("Erreur:", e)