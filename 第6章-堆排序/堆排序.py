
"""
__author__='marseille'
datetime:2020/11/14

"""
class HEAP_SORT:
    def __init__(self,A):
        self.heapsize = len(A) - 1
        self.A = A
        self.build_max_heap(self.A)
    def HeapSize(self):
        return self.heapsize + 1
    def parent(self,i):
        return (i - 1) // 2
    def left(self,i):
        return 2 * i + 1
    def right(self,i):
        return 2 * i + 2
    def max_heapify(self,A,i):#维护最大堆的性质
        l = self.left(i)
        r = self.right(i)
        if l <= self.heapsize and A[l] > A[i] :
            largest = l
        else:
            largest = i
        if r <= self.heapsize and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i],A[largest] = A[largest],A[i]
            self.max_heapify(A,largest)
    def build_max_heap(self,A):
        build_start = (len(A) - 2) // 2
        for i in range(build_start,-1,-1):  # 自底向上建堆 建立一个最大堆
            self.max_heapify(A,i)
    def heap_sort(self):
        for i in range(len(self.A) - 1,0,-1):
            self.A[0],self.A[i] = self.A[i],self.A[0]
            self.heapsize = self.heapsize - 1
            self.max_heapify(self.A,0)
        return self.A
if __name__ == "__main__":
    A = [5,2,3,1]
    hS = HEAP_SORT(A)
    print(hS.heap_sort())