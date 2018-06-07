class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return

        # swap row
        for i in range(n // 2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
sol = Solution()

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
sol.rotate(matrix)
print(matrix)


matrix = [ [5, 1, 9, 11],
           [2, 4, 8, 10],
           [13,3, 6, 7 ],
           [15,14,12,16] ]
sol.rotate(matrix)
print(matrix)
