# Create functions here
def is_even(input_number):
	if(input_number % 2 == 0):
		return("\nYes "+ str(input_number) + " is an even number")
	else:
		return("\nNo " + str(input_number) + " is not an even number")


# This is your main function
# This is where you declare your variables and use your functions
def main():
	# Intial call
	# Have to use print statement
	pcrint(is_even(1))

	# Reuse
	print(is_even(200))

# Call your main function	
if __name__ == "__main__":
	main()