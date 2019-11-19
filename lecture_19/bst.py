class Node:
	def __init__(self, data):
		self.data 		= data
		self.left_node 	= None
		self.right_node = None

	# Insert 
	def node_insert(self, d):
		# Compare the input data to the data in the current node
		if(self.data > d):
			# If the current Node doesn't have a left Node we create one with the input data
			# BASE CASE_1
			if(self.left_node == None):
				self.left_node = Node(data = d)
				return(True)

			# If the current Node has a left Node we call our recursive node_insert
			else:
				return(self.left_node.node_insert(d))
		else:
			# BASE CASE_1
			if(self.right_node == None):
				self.right_node = Node(data = d)
				return(True)
			else:
				return(self.right_node.node_insert(d))


	# Find 
	def node_find(self, d):
		# We've found the data
		##BASE CASE
		if(self.data == d):
			return(True)
		# Compare the input data to the data in the current node
		elif(self.data > d):
			if(self.left_node):
				return(self.left_node.node_find(d))
			else:
				return(False)

		else:
			if(self.right_node):
				return(self.right_node.node_find(d))
			else:
				return(False)


	# Traversal
	def node_preorder(self):
		if(self):
			print(str(self.data))
			if(self.left_node):
				self.left_node.node_preorder()
			if(self.right_node):
				self.right_node.node_preorder()




class Tree:
	def __init__(self, root = None):
		self.root = root

	# Insert
	def tree_insert(self, d):

		if (self.root):
			# If there is a tree (i.e the tree is not empy)
			## You are using the Node insert method
			return(self.root.node_insert(d))
		else:
			# if there isn't a tree (i.e you have an empty tree). Insert at root
			self.root = Node(data = d)


	def tree_find(self, d):
		# If there is a tree (i.e the tree is not empy)
		if (self.root):
			return(self.root.node_find(d))
		else:
			# Data not present
			return(False)


	# Traversal
	def tree_preorder(self):
		print("Traversing:")
		self.root.node_preorder()


def main():
	bst_1 = Tree()


	bst_1.tree_insert(d = 10)

	bst_1.tree_insert(d = 15)

	# print(bst_1.tree_find(d = 1000))

	# bst_1.tree_preorder()

	bst_1.tree_insert(d = 100)

	bst_1.tree_insert(d = 1)

	bst_1.tree_preorder()





if __name__ == '__main__':
	main()