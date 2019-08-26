import math
import random
import GraphvizInterface

class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self._key = key
        self._left = left
        self._right = right
        self._parent = parent

class BinarySearchTree:
    def __init__(self):
        self._size = 0
        self._root = None

    def insert(self,root,node):

        x = root
        if x is None:
            self._root = node
        else:
            if x._key < node._key:
                if x._right is None:
                   x._right = node
                   node._parent = x
                else:
                    self.insert(x._right,node)
            else:
                if x._left is None:
                    x._left = node
                    node._parent = x
                else:
                    self.insert(x._left,node)

    def search(self,root, k):
        if(root is None or k == root._key):
            return root
        else:
            if k < root._key :
                return self.search(root._left,k)
            else:
                return self.search(root._right,k)

    def minimum(self,root):
        if root._left is None:
            return root
        else:
            return self.minimum(root._left)

    def maximum(self,root):
        if root._right is None:
            return root
        else:
            return self.maximum(root._right)


    # Successor of a node x is the node with the smallest key greater than x:key
    # 1) If the right subtree of node x is nonempty, then the successor of x is just the leftmost node in x’s right subtree
    # 2) If the right subtree of node x is empty and x has a successor y, then y is the lowest ancestor of x whose left child is also an ancestor of x.
    #    Tofind y, we simply go up the tree from x until we encounter a node that is the left child of its parent
    def successor(self,node):
        x = node
        # 1) If the successor is in the right subtree
        if(x._right is not None):
            return self.minimum(x._right)
        # 2) If the right sub tree is empty i.e successor is an ancestor node in the tree
        y = x._parent
        while (y is not None and x == y._right):
            x = y
            y = y._parent
        return y

    # Reverse of Successor
    def predecessor(self,node):
        x = node
        if (x._left is not None):
            return self.maximum(x._left)
        y = x._parent
        while (y is not None and x == y._left):
            x = y
            y = y._parent
        return y

    def delete(self,root, node):
        z = node
        if z._left is None:
            self._transplant(root,z,z._right)
        elif z._right is None:
            self._transplant(root,z,z._left)
        else:
            y = self.minimum(z._right)
            if y._parent is not z:
                self._transplant(root, y, y._right)
                y._right = z._right
                y._right._parent = y
            self._transplant(root,z,y)
            y._left = z._left
            y._left._parent = y

    def _transplant(self,root,u,v):
        if u._parent is None:
            root = u
        elif u == u._parent._left:
            u._parent._left = v
        else:
            u._parent._right = v
        if v is not None:
            v._parent = u._parent

    def inorder(self,root):
        if root :
            self.inorder(root._left)
            print(root._key, end =" ")
            self.inorder(root._right)

    def preorder(self,root):
        if root :
            print(root._key, end =" ")
            self.preorder(root._left)
            self.preorder(root._right)

    def postorder(self,root):
        if root :
            self.preorder(root._left)
            self.preorder(root._right)
            print(root._key, end =" ")



def main():

    T = BinarySearchTree()
    root = Node(50)
    T.insert(None,root)
    T.insert(root, Node(30))
    T.insert(root, Node(20))
    T.insert(root, Node(40))
    T.insert(root, Node(60))
    T.insert(root, Node(10))
    T.insert(root, Node(70))
    T.insert(root, Node(35))
    T.insert(root, Node(65))
    T.insert(root, Node(55))
    T.insert(root, Node(41))
    T.insert(root, Node(25))
    T.insert(root, Node(75))
    T.insert(root, Node(51))
    T.insert(root, Node(56))
    T.insert(root, Node(80))

    # T.inorder(root)
    # T.preorder(root)
    graphViz = GraphvizInterface()
    graphViz.createGraphData(root)
    graphViz.generateGrap()


def buildTree():
    T = BinarySearchTree()

    listNum = [30,2,1,35,28,33,47,40,3,46,6,42,26,38,12,9,13,5,27,10]

    #listNum = random.sample(range(1,50),15)
    root = Node(listNum[0])
    T.insert(None, root)
    del listNum[0]
    for i in listNum:
        #print(i)
        T.insert(root,Node(i))

    graphViz = GraphvizInterface.GraphvizInterface()
    graphViz.createGraphData(root)
    graphViz.generateGrap()

    print("In order traversal :", end=" ")
    T.inorder(root)

    print("")
    print("Pre order traversal :", end=" ")
    T.preorder(root)

    print("")
    print("Post order traversal :", end=" ")
    T.postorder(root)

    result = T.search(root, 5)
    print("\nSearch : " + str(result._key if result is not None else "None"))

    result = T.minimum(root)
    print("Minimum : " + str(result._key if result is not None else "None"))

    result = T.maximum(root)
    print("Maximum : " + str(result._key if result is not None else "None"))

    result = T.successor(T.search(root,6))
    print("Successor of 6 : " + str(result._key if result is not None else "None"))

    result = T.successor(T.search(root,27))
    print("Successor of 27 : " + str(result._key if result is not None else "None"))

    result = T.successor(T.search(root, 47))
    print("Successor of 47 : " + str(result._key if result is not None else "None"))

    result = T.predecessor(T.search(root,6))
    print("Predecessor of 6 : " + str(result._key if result is not None else "None"))

    result = T.predecessor(T.search(root,28))
    print("Predecessor of 28 : " + str(result._key if result is not None else "None"))

    result = T.predecessor(T.search(root, 1))
    print("Predecessor of 1 : " + str(result._key if result is not None else "None"))

    T.delete(root,T.search(root, 6))
    graphViz.clearGraphData()
    graphViz.createGraphData(root)
    graphViz.generateGrap("BSTAfterDelete")

if __name__ == "__main__":
    buildTree()

