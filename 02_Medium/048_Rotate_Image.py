'''
48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        flat=[]
        # flatten the matrix
        for i in range(n):
            flat=flat+matrix[i]
        # after rotating
        # i row in matrix must be flat[i::n][::-1]
        for i in range(n):
            target=flat[i::n][::-1]
            matrix[i]=target
'''
Flatten matrix to 1-D array
e.g.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
then flat=[1,2,3,4,5,6,7,8,9]
After rotating the matrix
the i row array in matrix
must be i, i+n, i+2n.... and then reverse it
i.e.
i row must be flat[i::n][::-1]
'''