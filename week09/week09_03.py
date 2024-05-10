class ReducedRowEchelonForm:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        return "RREF로 변경된 행렬은 " + str(self.matrix) + " 입니다"
    def swap_rows(self, i, j):
        self.matrix[i], self.matrix[j] = self.matrix[j], self.matrix[i]
    def scale_row(self, i, scale):
        self.matrix[i] = [scale * x for x in self.matrix[i]]
    def add_scaled_row(self, source_row, target_row, scale):
        self.matrix[target_row] = [
        x + scale * y for x, y in zip(self.matrix[target_row], self.matrix[source_row])
        ]
    def to_reduced_row_echelon_form(self):
        for i in range(len(self.matrix)):
            to_div = self.matrix[i][0]
            for j in range(len(self.matrix[i])):
                if to_div != 0:
                    self.matrix[i][j] /= to_div
        for i in range(len(self.matrix)):
            
            


matrix = [[1, 2, 3], [0, 1, 2], [2, 3, 4]]
rref = ReducedRowEchelonForm(matrix)
rref.to_reduced_row_echelon_form()
print(rref)