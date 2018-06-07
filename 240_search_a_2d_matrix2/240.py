class Solution(object):
    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix) - 1
        c = 0

        cols = len(matrix[0])
        while r >= 0 and c < cols:
            if matrix[r][c] == target:
                return True

            if matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False
    # 95.84%


    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols-1

        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True

            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False
        
sol = Solution()

m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
t = 5
print(sol.searchMatrix(m, t))

t = 20
print(sol.searchMatrix(m, t))
