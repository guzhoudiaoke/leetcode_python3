#class Solution:
#    def exist(self, board, word):
#        """
#        :type board: List[List[str]]
#        :type word: str
#        :rtype: bool
#        """
#        def dfs(r, c, index):
#            if index + 1 == len(word):
#                return True
#
#            ch = board[r][c]
#            board[r][c] = '#'
#            for mv in moves:
#                rr, cc = r + mv[0], c + mv[1]
#                if rr >= 0 and rr < num_row and cc >= 0 and cc < num_col:
#                    if board[rr][cc] == word[index+1] and dfs(rr, cc, index+1):
#                        return True
#
#            board[r][c] = ch
#            return False
#
#        if len(word) == 0:
#            return True
#
#        moves = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
#        num_row, num_col = len(board), len(board[0])
#        if num_row == 0 or num_col == 0 or len(word) > num_row*num_col:
#            return False
#
#        for i in range(num_row):
#            for j in range(num_col):
#                if board[i][j] == word[0] and dfs(i, j, 0):
#                    return True
#
#        return False

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(r, c, index):
            if index + 1 == len(word):
                return True

            ch = board[r][c]
            board[r][c] = '#'

            if r+1 < num_row and board[r+1][c] == word[index+1] and dfs(r+1, c, index+1):
                return True
            if c+1 < num_col and board[r][c+1] == word[index+1] and dfs(r, c+1, index+1):
                return True
            if r-1 >= 0 and board[r-1][c] == word[index+1] and dfs(r-1, c, index+1):
                return True
            if c-1 >= 0 and board[r][c-1] == word[index+1] and dfs(r, c-1, index+1):
                return True

            board[r][c] = ch
            return False


        if len(word) == 0:
            return True

        num_row, num_col = len(board), len(board[0])
        if num_row == 0 or num_col == 0 or len(word) > num_row*num_col:
            return False

        for i in range(num_row):
            for j in range(num_col):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False


sol = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(sol.exist(board, "ABCCED"))

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(sol.exist(board, "SEE"))

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(sol.exist(board, "ABCB"))
