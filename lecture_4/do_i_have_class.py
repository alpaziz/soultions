# Create functions here
def class_today(day_of_week):
	if(day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Friday"):
		return("Yes :( it's " + day_of_week)
	else:
		return("It's "+day_of_week+" so Hell No! :D")


# This is your main function
# This is where you declare your variables and use your functions
def main():
	# Intial call
	# Have to use print statement
	print(class_today("Tuesday"))

	# Reuse
	print(class_today("Thursday"))

# Call your main function	
if __name__ == "__main__":
	main()