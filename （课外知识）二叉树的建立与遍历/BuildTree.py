"""
__author__='marseille'
datetime:2020/11/20

"""
class TreeStruct:
    def __init__(self,data = None,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
    def getLeft(self):
        self.left = TreeStruct()
        return self.left
    def getRight(self):
        self.right = TreeStruct()
        return self.right
b = TreeStruct(data=1)
c = TreeStruct(data=2)
a = TreeStruct(left = b,right = c)
print(a.right.data)
print(a.left.data)
print("[[[[[[[[[[[[[[[[")
class TreeNode:
    def __init__(self,data = None,left :object= None ,right:object= None):
        self.data = data
        self.left = left
        self.right = right
class TraverseTree:
    def __init__(self):
        self.Arr = []
    def preOrder(self,root):
        if root:
            self.Arr.append(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            self.Arr.append(root.data)
            self.inOrder(root.right)
    def postOrder(self,root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            self.Arr.append(root.data)
    def clearArr(self):
        return self.Arr.clear() # Arr[:] = []
    def printArr(self):
        return print(self.Arr)
class BuildTree:
    def preBuild(self,Arr,index):
        if index < len(Arr) and Arr[index]:
            treeNode = TreeNode()
            treeNode.data = Arr[index]
            treeNode.left = self.preBuild(Arr,2 * index + 1)
            treeNode.right = self.preBuild(Arr,2 * index + 2)
            return treeNode
    def inBuild(self,Arr,index):
        if index < len(Arr) and Arr[index]:
            treeNode = TreeNode()
            treeNode.left = self.inBuild(Arr,2 * index + 1)
            treeNode.data = Arr[index]
            treeNode.right = self.inBuild(Arr,2 * index + 2)
            return treeNode
    def postBuild(self,Arr,index):
        if index < len(Arr) and Arr[index]:
            treeNode = TreeNode()
            treeNode.left = self.postBuild(Arr,2 * index + 1)
            treeNode.right = self.postBuild(Arr,2 * index + 2)
            treeNode.data = Arr[index]
            return treeNode
class BuildTreeByOrder:
    def __init__(self,preOrderArr = None):
        self.preOrderArr = preOrderArr
        self.inOrderArr = None
        self.postOrderArr = None
        self.InOrderIndex = -1
        self.InOrderCur = -1

        self.PostOrderIndex = -1

        # 给出前序的一个数组 前序（中序，后序）建立一颗二叉树 都可以实现
        # 给出中序的一个数组 中序(前序，后序)建立一棵二叉树 我觉得都无法实现
        # 给出后序的一个数组 后序(前序，中序)建立一棵二叉树 我觉得都无法实现
    def buildByPreOrder(self,root,Arr):
        if Arr:
            data = Arr.pop(0)
            if data:
                root.data = data
                self.buildByPreOrder(root.getLeft(),Arr)
                self.buildByPreOrder(root.getRight(),Arr)
            else:
                root = data  # None
    def buildByInOrder(self,root,Arr):
        self.InOrderIndex = self.InOrderIndex + 1
        if Arr[self.InOrderIndex]:
            dataIndex = self.InOrderIndex
            self.buildByInOrder(root.getLeft(),Arr)
            root.data = Arr[dataIndex]
            self.buildByInOrder(root.getRight(),Arr)
        else:
            root = None

    def buildByPostOrder(self,root,Arr):
        self.PostOrderIndex = self.PostOrderIndex + 1
        if Arr[self.PostOrderIndex]:
            dataIndex = self.PostOrderIndex
            self.buildByPostOrder(root.getLeft(),Arr)
            self.buildByPostOrder(root.getRight(),Arr)
            root.data = Arr[dataIndex]
        else:
            root = None
root = TreeNode()
left2 = TreeNode()
right3 = TreeNode()
left4 = TreeNode()
right5 = TreeNode()
left6 = TreeNode()
right7 = TreeNode()

root.left = left2
root.right = right3
root.data = 1

left2.left = left4
left2.right = right5
left2.data = 2

right3.left = left6
right3.right = right7
right3.data = 3

left4.data = 4
right5.data = 5

left6.data = 6
right7.data = 7

traverseTree = TraverseTree()
traverseTree.preOrder(root)
traverseTree.printArr()

traverseTree.clearArr()
traverseTree.inOrder(root)
traverseTree.printArr()

traverseTree.clearArr()
traverseTree.postOrder(root)
traverseTree.printArr()
"""
[1, 2, 4, 5, 3, 6, 7]
[4, 2, 5, 1, 6, 3, 7]
[4, 5, 2, 6, 7, 3, 1]
"""
traverseTree.clearArr()

Arr = [1,2,3,4,5,6,7,None,None,None,None,None,None,None,None]
buildTree = BuildTree()
root = buildTree.postBuild(Arr,0)

traverseTree.preOrder(root)
traverseTree.printArr()
traverseTree.clearArr()

traverseTree.inOrder(root)
traverseTree.printArr()
traverseTree.clearArr()

traverseTree.postOrder(root)
traverseTree.printArr()
traverseTree.clearArr()

print("---------------")
print("---------------")
Arr = [1, 2, 4, None, None, 5, None, None, 3, 6, None, None, 7, None, None]
root = TreeStruct(left = TreeStruct(),right = TreeStruct())
buildTreeByOrder = BuildTreeByOrder()
buildTreeByOrder.buildByPreOrder(root,Arr)
traverseTree.postOrder(root)
traverseTree.printArr()
traverseTree.clearArr()

print("---------------")
print("---------------")
Arr = [1, 2, 4, None, None, 5, None, None, 3, 6, None, None, 7, None, None]
root = TreeStruct(left = TreeStruct(),right = TreeStruct())
buildTreeByOrder = BuildTreeByOrder()
buildTreeByOrder.buildByInOrder(root,Arr)
traverseTree.postOrder(root)
traverseTree.printArr()
traverseTree.clearArr()
