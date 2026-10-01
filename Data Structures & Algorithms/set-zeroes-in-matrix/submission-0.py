class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols = [False] * len(matrix), [False] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i], cols[j] = True, True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] or rows[j]:
                    matrix[i][j] = 0