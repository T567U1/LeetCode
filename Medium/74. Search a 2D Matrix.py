class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        for front, back in zip(matrix, matrix[::-1]):
            if target in front or target in back:
                return True
            elif front == back and target not in front:
                return False
            
