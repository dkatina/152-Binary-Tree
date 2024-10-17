
class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, key):

        if self.root == None: #Check if I have a root
            self.root = TreeNode(key)# If not create new node to become root
        else:
            self.insert_recursive(self.root, key)# Else evalutate key against Root

    def insert_recursive(self, node, key):

        if key < node.key: #Check if key is smaller that current nodes key
            if node.left == None: #Checking if space occupied
                node.left = TreeNode(key) #If not fill that space
            else:
                self.insert_recursive(node.left, key) #Else, evaluate key against that Left Node
        
        elif key > node.key: #Check if the key is greater than Current Node
            if node.right == None: #Check if the space is occupied
                node.right = TreeNode(key) # If not, fill the space
            else:
                self.insert_recursive(node.right, key)# If so, evaluate key against the right Node

    def print_tree(self):
        if self.root == None:
            print("Tree Empty")
        else:
            self.print_recursive(self.root, 0)

    def print_recursive(self, node, depth):
        
        if node is None: #Base Case
            return None
        
        self.print_recursive(node.right, depth + 1)
        print("    "* depth + str(node.key))
        self.print_recursive(node.left, depth + 1)
    
    def search(self, key):
        if self.root == None:
            return False
        else:
            self.search_recursive(self.root, key)
    
    def search_recursive(self, node, key):

        if node == None: #Negative Base Case
            return False
        
        if node.key == key: #Positive Base Case
            return True
        elif key < node.key:
            return self.search_recursive(node.left, key)
        else:
            return self.search_recursive(node.right, key)
        
    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)

    def find_smallest(self, node):
        while node.left:
            node = node.left
        return node

    def delete_recursive(self, node, key):

        if node == None: #Negative base case, what we are trying to delete isnt here
            return
        
        if key < node.key: #The node I want to delete is to the left because its smaller
            node.left = self.delete_recursive(node.left, key)
        elif key > node.key: #The node I want to delete is to the right because its larger
            node.right = self.delete_recursive(node.right, key)
        else:# I have found the node I want to delete
            if node.left == None: #Does it have a left branch
                return node.right #If not we will return the node on the right
            elif node.right == None: #I know I have a single branch to the right
                return node.left
            
            #If we make it here I know that the target has two branches
            #find the smallest
            smallest = self.find_smallest(node.right)
            #use that nodes value to replace the target
            node.key = smallest.key
            #go back and remove the smallest from its previos position
            node.right = self.delete_recursive(node.right, smallest.key)
            
        return node




tree = BinaryTree()

tree.insert(40)
tree.insert(50)
tree.insert(45)
tree.insert(30)
tree.insert(35)
tree.insert(20)

tree.print_tree()

tree.delete(30)
print("~"*50)

tree.print_tree()
