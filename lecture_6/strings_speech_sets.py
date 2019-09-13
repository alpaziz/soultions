# Declare function here
def find_common(string_1, string_2):
	# Seperate on whitespace and save output
	speech_1_list = string_1.split()
	speech_2_list = string_2.split()

	# Converts lists to sets
	speech_1_set = set(speech_1_list)
	speech_2_set = set(speech_2_list)

	# Save common
	common = speech_1_set.intersection(speech_2_set)

	return(common)


# This is where you declare your variables and use your functions
def main():

	speech_1  = "Today we continue a never-ending journey to bridge"
	speech_2 = "Every four years, we gather on these steps to carry out the orderly and peaceful transfer of power, and we are grateful to President Obama and First Lady Michelle Obama for their gracious aid throughout this transition. They have been magnificent."

	print(find_common(speech_1, speech_2))

# Call your main function	
if __name__ == "__main__":
	main()	