# This is your main function
# This is where you declare your variables and use your functions
def main():
	temp_dict ={"A":1, "B":2, "C":3}

	for key in temp_dict:
		print("\nkey:"+key)

		print("\nvalue:"+str(temp_dict[key]))

# Call your main function	
if __name__ == "__main__":
	main()