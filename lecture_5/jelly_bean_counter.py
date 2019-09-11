# This is your main function
# This is where you declare your variables and use your functions
def main():

	# Create a list of jelly beans
	jar_of_jelly_beans = ["red","blue","yellow","red","orange"]


	# Append
	jar_of_jelly_beans.append("PURPLE")
	count = 0
	for jelly_bean in jar_of_jelly_beans:

		count+=1

		print(count)
		# print(jelly_bean)

# Call your main function	
if __name__ == "__main__":
	main()