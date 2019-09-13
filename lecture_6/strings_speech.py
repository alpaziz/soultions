
# This is where you declare your variables and use your functions
def main():

	speech_1 = "Today we continue a never-ending journey to bridge the meaning of those words with the realities of our time.  For history tells us that while these truths may be self-evident, they’ve never been self-executing; that while freedom is a gift from God, it must be secured by His people here on Earth. The patriots of 1776 did not fight to replace the tyranny of a king with the privileges of a few or the rule of a mob.  They gave to us a republic, a government of, and by, and for the people, entrusting each generation to keep safe our founding creed. "
	speech_2 = "Every four years, we gather on these steps to carry out the orderly and peaceful transfer of power, and we are grateful to President Obama and First Lady Michelle Obama for their gracious aid throughout this transition. They have been magnificent."


	# Seperate on whitespace and save output
	speech_1_list = speech_1.split()
	speech_2_list = speech_2.split()

	# Print result
	print(speech_1_list)
	print(speech_2_list)

	common = list()

	# Iterate over each word
	for substring_1 in speech_1_list:
		for substring_2 in speech_2_list:
			if(substring_1 == substring_2):
				if(substring_1 not in common):
					common.append(substring_1)



	print(common)	
		

# Call your main function	
if __name__ == "__main__":
	main()	