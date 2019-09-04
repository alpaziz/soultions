# Create functions here
def hello_world(your_name):
	return("\nHello "+  your_name + " how are you?")

# This is your main function
# This is where you declare your variables and use your functions
def main():
	# Intial call
	# Have to use print statement
	print(hello_world("Prof. Alp"))

	# Reuse
	print(hello_world("President Trump"))

# Call your main function	
if __name__ == "__main__":
	main()