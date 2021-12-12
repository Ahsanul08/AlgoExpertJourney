# iterative solution (bfs manner)

def invertBinaryTree(tree):
       # Write your code here.
       queue = [tree]
	while queue:
		node = queue.pop(0)
		if node is None:
			continue
		node.left, node.right = node.right, node.left
		
		queue.append(node.left)
		queue.append(node.right)
	 return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# recursive solution

def invertBinaryTree(tree):
    # Write your code here.
	if tree is None:
		return
	
	tree.left, tree.right = tree.right, tree.left
	tree.left = invertBinaryTree(tree.left)
	tree.right = invertBinaryTree(tree.right)
	
	return tree

