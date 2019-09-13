# Declare function here
def string_explorer(string_1):
	# Display length of string
	print(len(string_1))

	# Display First 2 characters
	print("\n"+string_1[0]+string_1[1]+"\n")

	# Seperate string based on white spaces
	print(string_1.split())

	# Find a specific substring (i.e word)
	print(string_1.find("AU"))

	# Count occurences of a substring
	return(string_1.count("AU")) 

# This is where you declare your variables and use your functions
def main():

	temp_string = "GW, AU Eagles are rockstars in 2020 ! AU Football for LIFE"

	print(string_explorer(temp_string))


# Call your main function	
if __name__ == "__main__":
	main()	