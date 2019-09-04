# Create functions here
def list_function(a,b):
  
  # Merge or concatenate both input lists
  merged = a+b

  # Print length of result list
  print(len(merged))

  # Print min
  print(min(merged))

  # Print max
  print(max(merged))

  print("\nUnsorted: \n", merged)

  # Sort list
  merged.sort()

  print("\nSorted: \n")
  return(merged)


# This is your main function
# This is where you declare your variables and use your functions
def main():
	# Intial call
	# Have to use print statement
	print(list_function([1,10,-20], [20,10,-40]))

	# Reuse
	print(list_function([100,10,-20,1,3], [1,-1,200,-200]))
	

# Call your main function	
if __name__ == "__main__":
	main()