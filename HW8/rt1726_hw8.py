class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # returns None if not found
    def subtree_find(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value

    # assumes key not in tree
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                else:
                    curr = curr.right
            if (key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.size += 1

    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.subtree_delete(self.root, key)

    #assumes key is in tree + returns value assosiated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node


    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)

    def preorder(self):
        for node in self.subtree_preorder(self.root):
            yield node

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)


def create_chain_bst(n):
    resTree = BinarySearchTreeMap()
    if n == 0:
        return resTree
    print('n:', n)
    for i in range(n):
        resTree.subtree_insert(i + 1)
        print('size:', resTree.size)
    return resTree

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if low == high:
        bst.subtree_insert((low + high) // 2)
        return
    else:
        bst.subtree_insert((low + high) // 2)
        add_items(bst, low, (low + high) // 2 - 1)
        add_items(bst, (low + high) // 2 + 1, high)
    
def restore_bst(prefix_lst):
    curr_node, index = restore_bst_left(prefix_lst, 0, None)
    a = BinarySearchTreeMap()
    a.root = curr_node



def restore_bst_left(prefix_lst, pos, parent_data):
    if prefix_lst[pos + 1] < prefix_lst[pos]:
        LChild, index, parent_data = restore_bst_left(prefix_lst, pos + 1, prefix_lst[pos])
        item = BinarySearchTreeMap.Item(prefix_lst[pos])
        curr_node = BinarySearchTreeMap.Node(item)
        curr_node.left = LChild
        if parent_data is not None:
            if prefix_lst[index] > parent_data:                
                return curr_node, index
            else:
                item = BinarySearchTreeMap.Item(prefix_lst[index])
                RChild = BinarySearchTreeMap.Node(item)
                curr_node.right = RChild
                return curr_node, index + 1
        else:
            return curr_node, index
            
    else:
        item = BinarySearchTreeMap.Item(prefix_lst[pos])
        curr_node = BinarySearchTreeMap.Node(item)
        if prefix_lst[pos + 1] > parent_data:
            return curr_node, pos + 1
        else:
            item = BinarySearchTreeMap.Item(prefix_lst[pos + 1])
            RChild = BinarySearchTreeMap.Node(item)
            curr_node.right = RChild
            return curr_node, pos + 2

    

def restore_bst_right(prefix_lst, pos, parent_data):
    if prefix_lst[pos + 1] < prefix_lst[pos]:
        LChild, index = restore_bst_right(prefix_lst, pos + 1, prefix_lst[pos])
        item = BinarySearchTreeMap.Item(prefix_lst[pos])
        curr_node = BinarySearchTreeMap.Node(item)
        curr_node.left = LChild
        if parent_data is not None:
            if prefix_lst[index] > parent_data:                
                return curr_node, index
            else:
                item = BinarySearchTreeMap.Item(prefix_lst[index])
                RChild = BinarySearchTreeMap.Node(item)
                curr_node.right = RChild
                return curr_node, index + 1
        else:
            item = BinarySearchTreeMap.Item(prefix_lst[index])
            RChild = BinarySearchTreeMap.Node(item)
            curr_node.right = RChild
            return curr_node, index + 1
            
    else:
        item = BinarySearchTreeMap.Item(prefix_lst[pos])
        curr_node = BinarySearchTreeMap.Node(item)
        if prefix_lst[pos + 1] > parent_data:
            return curr_node, pos + 1
        else:
            item = BinarySearchTreeMap.Item(prefix_lst[pos + 1])
            RChild = BinarySearchTreeMap.Node(item)
            curr_node.right = RChild
            return curr_node, pos + 2

def find_min_abs_difference(bst):
    res = find_min_difference_helper(bst.root)
    return res[2]

def find_min_difference_helper(curr_root):

    if curr_root.left is None and curr_root.right is None:
        return curr_root.item.key, curr_root.item.key, None
    elif curr_root.left is None:
        res = find_min_difference_helper(curr_root.right)
        if res[2] is None or abs(res[0] - curr_root.item.key) < res[2]:
            diff = abs(res[0] - curr_root.item.key)
        else:
            diff = res[2]
        return curr_root.item.key, res[1], diff
    elif curr_root.right is None:
        res = find_min_difference_helper(curr_root.left)
        if res[2] is None or abs(res[1] - curr_root.item.key) < res[2]:
            diff = abs(res[1] - curr_root.item.key)
        else:
            diff = res[2]
        return res[0], curr_root.item.key, diff
    else:
        diff1 = 0
        diff2 = 0
        res1 = find_min_difference_helper(curr_root.left)
        res2 = find_min_difference_helper(curr_root.right)
        if res1[2] is None or abs(res1[0] - curr_root.item.key) < res1[2]:
            diff1 = abs(res1[0] - curr_root.item.key)
        else:
            diff1 = res1[2]
        if res2[2] is None or abs(res2[0] - curr_root.item.key) < res2[2]:
            diff2 = abs(res2[0] - curr_root.item.key)
        else:
            diff2 = res2[2]
        diff = min(abs(curr_root.item.key - res1[1]), abs(curr_root.item.key - res2[0]), diff1, diff2)
        return res1[0], res2[1], diff

'''
a = BinarySearchTreeMap()
item = BinarySearchTreeMap.Item(9)
n1 = BinarySearchTreeMap.Node(item)
a.root = n1
item = BinarySearchTreeMap.Item(7)
n1.left = BinarySearchTreeMap.Node(item)
item = BinarySearchTreeMap.Item(4)
n1.left.left = BinarySearchTreeMap.Node(item)
item = BinarySearchTreeMap.Item(1)
n1.left.left.left = BinarySearchTreeMap.Node(item)
item = BinarySearchTreeMap.Item(6)
n1.left.left.right = BinarySearchTreeMap.Node(item)
item = BinarySearchTreeMap.Item(20)
n1.right = BinarySearchTreeMap.Node(item)
item = BinarySearchTreeMap.Item(17)
n1.right.left = BinarySearchTreeMap.Node(item)
item = BinarySearchTreeMap.Item(25)
n1.right.right = BinarySearchTreeMap.Node(item)

print(find_min_difference(a))

a = create_complete_bst(7)
for i in a:
    print(i)
'''