# This is your main function
# This is where you declare your variables and use your functions
def main():
	
	jelly_beans = ['red', 'yellow', 'purple', 'orange']

	count = 0

	while (count != (len(jelly_beans))):
		print(jelly_beans[count])
		count = count +1

# Call your main function	
if __name__ == "__main__":
	main()