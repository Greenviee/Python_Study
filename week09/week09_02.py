class ReducedRowEchelonForm:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        return "현재 입력된 행렬은 " + str(self.matrix) + " 입니다"          

matrix = [[1, 2, 3], [0, 1, 2], [2, 3, 4]]
rref = ReducedRowEchelonForm(matrix)
print(rref)