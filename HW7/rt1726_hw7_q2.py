class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def subtree_count(self, curr_root):
        if(curr_root is None):
            return 0
        else:
            left_count = self.subtree_count(curr_root.left)
            right_count = self.subtree_count(curr_root.right)
            return left_count + right_count + 1

    def height(self):
        if(self.is_empty()):
            raise Exception("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, curr_root):
        if((curr_root.left is None) and (curr_root.right is None)):
            return 0
        elif(curr_root.right is None):
            return 1 + self.subtree_height(curr_root.left)
        elif(curr_root.left is None):
            return 1 + self.subtree_height(curr_root.right)
        else:
            left_height = self.subtree_height(curr_root.left)
            right_height = self.subtree_height(curr_root.right)
            return 1 + max(left_height, right_height)

    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            return
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if (curr_root is None):
            return
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if (curr_root is None):
            return
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root

    def __iter__(self):
        for node in self.postorder():
            yield node.data


    def leaves_list(self):
        lst = []
        if self.root is None:
            return lst
        for i in self.leaves_generator(self.root):
            lst.append(i)
        return lst


        

    def leaves_generator(self, subtree):

        print(subtree.data)
        if(subtree.left is None) and (subtree.right is None):
            yield subtree.data
        elif(subtree.right is None):
            yield from self.leaves_generator(subtree.left)
        elif(subtree.left is None):
            yield from self.leaves_generator(subtree.right)
        else:
            yield from self.leaves_generator(subtree.left)
            yield from self.leaves_generator(subtree.right)


'''
a = LinkedBinaryTree()

p1 = LinkedBinaryTree.Node(5)
p2 = LinkedBinaryTree.Node(1)
p3 = LinkedBinaryTree.Node(9, p1, p2)
p4 = LinkedBinaryTree.Node(2, p3)
p5 = LinkedBinaryTree.Node(8)
p6 = LinkedBinaryTree.Node(4)
p7 = LinkedBinaryTree.Node(7, p5, p6)
p8 = LinkedBinaryTree.Node(3, p4, p7)
a.root = p8
for i in a:
    print(i, end=' ')
print()

print(a.leaves_list())
'''