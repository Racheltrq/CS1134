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
################################################################


#q2-------------------------------------------------------------
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
#q2--------------------------------------------------------------


#q4--------------------------------------------------------------

    def iterative_inorder(self):
        cursor = self.root

        while cursor is not None:

            if cursor.left is None:
                yield (cursor.data)
                cursor = cursor.right

            else:
                sub = cursor.left
                while sub.right is not None and sub.right != cursor:
                    sub = sub.right
                if sub.right is None:

                    sub.right = cursor
                    cursor = cursor.left
                else:
                    sub.right = None
                    yield (cursor.data)
                    cursor = cursor.right
    

#q4---------------------------------------------------------------



#q1-------------------------------------------------
class EmptyTree(Exception):
    pass

def min_and_max(bin_tree):
    if bin_tree.root is None:
        raise EmptyTree('The tree is empty.')
    sub_tree = bin_tree.root
    root = bin_tree.root.data
    lst = [root, root]
    subtree_min_and_max_bin(sub_tree, lst)
    res = (lst[0], lst[1])
    return res


def subtree_min_and_max_bin(sub_tree, lst):
    if sub_tree is None:
        return lst
    else:
        subtree_min_and_max_bin(sub_tree.left, lst)
        subtree_min_and_max_bin(sub_tree.right,lst)
        if sub_tree.data > lst[1]:
            lst[1] = sub_tree.data
        elif sub_tree.data < lst[0]:
            lst[0] = sub_tree.data
        print(lst)
#q1-------------------------------------------------


#q3--------------------------------------------------------------------------
def is_height_balanced(bin_tree):
    for i in bin_tree:
        print(i, end=' ')
    print()
    res = (0, True)
    res = is_height_balanced_helper(bin_tree.root, res)
    return res[1]

def is_height_balanced_helper(curr_root, res):
    print(curr_root.data)
    if ((curr_root.left is None) and (curr_root.right is None)):
        return 1, True
    else:
        if (curr_root.right is None):
            left_height, balance = is_height_balanced_helper(curr_root.left, res)
            print(curr_root.data, left_height)
            if left_height > 1 or balance is False:
                print(1 + left_height, False)
                return (1 + left_height, False)

            else:
                print(1 + left_height, True)
                return (1 + left_height, True)

        elif (curr_root.left is None):
            right_height,  = is_height_balanced_helper(curr_root.right, res)
            print(curr_root.data, right_height)
            if right_height > 1 or balance is False:
                print(1 + right_height, False)
                return (1 + right_height, False)
            print(1 + right_height, True)
            return (1 + right_height, True)
        else:
            left_height, balance1 = is_height_balanced_helper(curr_root.left, res)
            right_height, balance2 = is_height_balanced_helper(curr_root.right, res)
            print(curr_root.data, left_height, right_height, balance1, balance2)

            if -1 > (left_height - right_height) or (left_height - right_height) > 1 or balance1 is False or balance2 is False:
                balance = False
                print('l-r:', left_height-right_height, balance)
                #if curr_root.parent is not None:
                    
                return (1 + max(left_height, right_height), balance)
            else:
                print(1 + max(left_height, right_height), True)
                return (1 + max(left_height, right_height), True)

#q3--------------------------------------------------------------------------------------------------------------------


#q5-------------------------------------------------------------------
def create_expression_tree(prefix_exp_str):
    lst = prefix_exp_str.split(' ')
    root, pos = create_expression_tree_helper(lst, 0)
    a = LinkedBinaryTree(root)
    return a

def create_expression_tree_helper(prefix_exp, pos):
    nData = prefix_exp[pos]
    pos += 1
    if(prefix_exp[pos] in "+-*/"):
        nLeft = create_expression_tree_helper(prefix_exp, pos);
        lChild = nLeft[0]
        pos = nLeft[1]
    else :
        lChild = LinkedBinaryTree.Node(int(prefix_exp[pos]));
        pos += 1

    if(prefix_exp[pos] in "+-*/"):
        nRight = create_expression_tree_helper(prefix_exp, pos);
        rChild = nRight[0]
        pos = nRight[1]
    else :
        rChild = LinkedBinaryTree.Node(int(prefix_exp[pos]));
        pos += 1

    return (LinkedBinaryTree.Node(nData, lChild, rChild), pos);



def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    lst = []
    for i in tree.postorder():

        lst.append(str(i.data))
    print(lst)
    return ' '.join(lst)
#q5----------------------------------------------------------------------




'''
a = LinkedBinaryTree()

p1 = LinkedBinaryTree.Node(1)
p2 = LinkedBinaryTree.Node(6)
p3 = LinkedBinaryTree.Node(2, p1, p2)
p4 = LinkedBinaryTree.Node(4)
p5 = LinkedBinaryTree.Node(5, p3, p4)
a.root = p5
for i in a:
    print(i, end=' ')
print()

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
(a.iterative_inorder())

'''