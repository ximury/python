from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        sums = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                print('max: ', max(j-K, 0))
                print('min: ', min(j+K+1, n))
                print(mat[i][max(j - K, 0):min(j + K + 1, n)])
                sums[i][j] = sum(mat[i][max(j - K, 0):min(j + K + 1, n)])

        print(sums)
        res = [[0] * n for _ in range(m)]
        for i in range(0, m):
            for j in range(n):
                res[i][j] = sum([sums[p][j] for p in range(max(i - K, 0), min(i + K + 1, m))])
        return res


c = Solution
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(c.matrixBlockSum(c, mat, 1))

"""
给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，
其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 
i - K <= r <= i + K, j - K <= c <= j + K 
(r, c) 在矩阵内。
 
示例 1：
输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
"""