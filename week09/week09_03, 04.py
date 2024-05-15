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
        rows, cols = len(self.matrix), len(self.matrix[0])
        l = 0
        
        for r in range(rows):
            if l >= cols:
                return
            i = r
            while self.matrix[i][l] == 0:
                i += 1
                if i == rows:
                    i = r
                    l += 1
                    if cols == l:
                        return
            self.swap_rows(i, r)
            lv = self.matrix[r][l]
            self.scale_row(r, 1.0 / lv)
            for i in range(rows):
                if i != r:
                    lv = self.matrix[i][l]
                    self.add_scaled_row(r, i, -lv)
            l += 1
    def print_matrix(self):
        for i in self.matrix:
            print(i)
            
            


matrix = [[1, 2, 3], [0, 1, 2], [2, 3, 4]]
rref = ReducedRowEchelonForm(matrix)
rref.to_reduced_row_echelon_form()
print(rref)
rref.print_matrix()