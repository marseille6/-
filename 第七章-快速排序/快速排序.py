"""
__author__='marseille'
datetime:2020/11/10

"""
class QuickSort:
    def main(self, nums: list):
        self.quick_sort(nums,0,len(nums) - 1)
        return nums
    def quick_sort(self,A,p,r):
        if p < r:
            q = self.partition(A,p,r)
            self.quick_sort(A,p,q-1)
            self.quick_sort(A,q+1,r)
    def partition(self,A,p,r):
        x = A[r]
        i = p - 1
        for j in range(p,r):
            if A[j] <= x:
                i = i + 1
                A[i],A[j] = A[j],A[i]
        A[i+1],A[r] = A[r],A[i+1]
        return i + 1
if __name__ == "__main__":
    pass
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums,0,len(nums) - 1)
        return nums
    def quick_sort(self,A,p,r):
        if p < r:
            q = self.partition(A,p,r)
            self.quick_sort(A,p,q-1)
            self.quick_sort(A,q+1,r)
    def partition(self,A,p,r):
        x = A[r]
        i = p - 1
        for j in range(p,r):
            if A[j] <= x:
                i = i + 1
                A[i],A[j] = A[j],A[i]
        A[i+1],A[r] = A[r],A[i+1]
        return i + 1
"""