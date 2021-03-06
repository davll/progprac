# Maximal Square
#
# f[i,j] = the size of the square whose lower-right corner is at (i,j)
#
# f[i,j] = M[0,j]   if i = 0
#        = M[i,0]   if j = 0
#        = 0        if M[i,j] = 0
#        = min { f[i-1,j-1], f[i,j-1], f[i-1,j] } + 1 otherwise
#
# https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
#

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        if not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for j in range(0, n):
            if matrix[0][j] == '1':
                dp[0][j] = 1
        for i in range(1, m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        result = 0
        for i in range(0, m):
            for j in range(0, n):
                result = max(result, dp[i][j])
        return result * result
