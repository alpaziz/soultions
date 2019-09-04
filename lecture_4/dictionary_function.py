# Create functions here
def dictionary_func(dict_1, dict_2):
	#Compare the lengths
	# and save larger dictionary
	if(len(dict_1)>len(dict_2)):
		larger_dict = dict_1
	else:
		larger_dict = dict_2

	# print out all th keys
	print("\nValues of larger dictionary are:" + str(larger_dict.keys()))
	print("\nValues of larger dictionary are:" + str(larger_dict.values()))

	# merge them with update method
	dict_1.update(dict_2)
	return(dict_1)

# This is your main function
# This is where you declare your variables and use your functions
def main():
	# Intial call
	# Have to use print statement
	merged_dict = dictionary_func({'x':200,'y':100,'z':20,'f':1,'g':0, 'AU':1, 'GWU':2},
						  {'a':20,'b':-100,'c':200,'d':10,'e':3}	
						)

	print("\nThe merged dictionary is:\n")
	print(merged_dict)

	# Delete a key:value pair
	del merged_dict['d']

	print("\nResult after removing:\n")
	print(merged_dict)
	

# Call your main function	
if __name__ == "__main__":
	main()