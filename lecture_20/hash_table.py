# slot class
class Slot:
    def __init__(self, data):
    	self.data = data

class Hash_table:
	def __init__(self):
		self.slot_dict = dict()

	# Insert
	def insert(self, d):
		key            = hash(d)
		new_slot 	   = Slot(data = d)
		self.slot_dict[key] = new_slot 

	def retrieve(self,d):
		if(len(self.slot_dict) == 0):
			return(False)
		else:
			key  = hash(d)
			if(key in self.slot_dict.keys()):
				retrieved_slot = self.slot_dict[key]
				return(True)
			else:
				return(False)


def main():
	temp = Hash_table()
	temp.insert(d = "ALP")
	# print(temp.get_slot_dict())

	# print(temp.retrieve(d = "Alp"))
	print(temp.retrieve(d = "ALP"))

	print(temp.retrieve(d = "EDIOT"))

if __name__ == '__main__':
	main()