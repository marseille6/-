"""
__author__='marseille'
datetime:2020/11/9

"""
class INSERT_SORT:
    def main_ascend(self,A:[]):# 升序排列‘
        for j in range(1,len(A)):
            key = A[j]
            i = j -1
            while i >= 0 and A[i] > key:
                A[i+1] = A[i]
                i = i - 1
            A[i+1] = key
        return A
    def main_descend(self,A:list):# 降序排列
        for j in range(1,len(A)):
            key = A[j]
            i = j -1
            while i >= 0 and A[i] < key:
                A[i+1] = A[i]
                i = i - 1
            A[i+1] = key
        return A
if __name__ == "__main__":
    A = [1,5,6,3,2,5,8,0,1,2,5,8,9]
    InsertSort = INSERT_SORT()
    print(InsertSort.main_ascend(A))
    print(InsertSort.main_descend(A))


