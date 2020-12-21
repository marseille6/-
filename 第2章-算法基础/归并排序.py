"""
__author__='marseille'
datetime:2020/11/10

"""
import sys
class MergeSort:
    def __init__(self):
        self.MAX_INT = sys.maxsize  # python 里的最大整数 也不用很较真 再大也是可以的 取决于内存大小
    def main(self,A):
        self.merge_sort(A,0,len(A) - 1)
        return A
    def merge(self,A,p,q,r):
        n1 = q - p + 1  # 左数组
        n2 = r - q   #   右数组
        L = [0 for i in range(n1 + 1)] #  n1个数字，下标为[0...n1-1] 一个哨兵下标为n1
        R = [0 for i in range(n2 + 1)] #  n2个数字，下标为[0...n2-1] 一个哨兵下标为n2
        for i in range(n1):
            L[i] = A[p + i]
        for i in range(n2):
            R[i] = A[q + i + 1]

        L[n1] = self.MAX_INT
        R[n2] = self.MAX_INT
        i = 0
        j = 0
        for k in range(p,r+1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
    ## 不使用哨兵，多加两个判断
    def mergeX(self,A,p,q,r):
        n1 = q - p + 1
        n2 = r - q
        L = [0 for i in range(n1)]
        R = [0 for i in range(n2)]
        for i in range(n1):
            L[i] = A[p + i]
        for i in range(n2):
            R[i] = A[q + i + 1]
        i = 0
        j = 0
        for k in range(p,r + 1):
            if i >= n1:
                A[k] = R[j]
                j = j + 1
            elif j >= n2:
                A[k] = L[i]
                i = i + 1
            elif L[i] <= R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1

    def merge_sort(self,A,p,r):
        if p < r:
            q = p + (r - p) // 2
            self.merge_sort(A,p,q)
            self.merge_sort(A,q + 1,r)
            self.mergeX(A,p,q,r)
if __name__ == "__main__":
    A = [5,2,3,1,-6,-9,-10,56,99]
    a = MergeSort()
    print(a.main(A))
