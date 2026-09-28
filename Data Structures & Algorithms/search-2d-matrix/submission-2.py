class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        var = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False