class Node:
	# constructor
	def __init__(self, data, next_node=None):
		self.next_node = next_node
		self.data 	   = data

	# Getters and setters
	def get_next_node(self):
		return(self.next_node)

	def set_next_node(self, n):
		self.next_node = n

	def get_data(self):
		return(self.data)

	def set_data(self, d):
		self.data = d


class Linked_List:
	# constructor
	def __init__(self, head=None):
		self.head = head
		self.size = 0

	# Getters and setters
	def get_head(self):
		return(self.head)

	def set_head(self, h):
		self.head = h

	def get_size(self):
		return(self.size)

	def set_size(self, s):
		self.size = s

	# Addition
	def add(self, input_data):
		# Create new Node
		new_node  = Node(data = input_data, next_node = self.head)

		# Set the root to our new Node
		self.head = new_node

		# Incremenet size as we added a new node
		self.size +=1

	# Remove
	def remove(self, input_data):
		current_node = self.get_head()
		previous = None

		# iterate
		while (current_node):
			if (current_node.get_data() == input_data):
				if(previous):
					previous.set_next_node(current_node.get_next_node())
				else:
					self.head = current_node.get_next_node()
				#Decrement size i.e since we removed a node
				self.size -= 1
				return (True)

			# Move to next node if data was not found
			else:
				previous 		= current_node
				current_node 	= current_node.next_node
		# Data was not found
		return(False)

	# find
	def find(self, input_data):
		current_node = self.get_head()

		# iterate
		while (current_node):
			if (current_node.get_data() == input_data):
				return (current_node.get_data())

			# Move to next node if data was not found
			else:
				current_node 	= current_node.next_node
		# Data was not found
		return(False)

def main():
	my_list = Linked_List()

	my_list.add(input_data= 10)
	my_list.add(input_data= 100)


	print(my_list.find(input_data=10))


if __name__ == '__main__':
	main()