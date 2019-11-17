
class Loan_applicant:
	# Constructor
	def __init__(self, name, age, no_children, employed, salary, no_missed_payments = None, no_credit_cards = None):
		self.name 				= 	name
		self.age  				= 	age
		self.no_children		=	no_children
		self.employed			= 	employed
		self.salary				= 	salary
		self.no_missed_payments	=	no_missed_payments
		self.no_credit_cards 	= 	no_credit_cards

	# Getters
	def get_age(self):
		return(self.age)

	def get_no_children(self):
		return(self.no_children)

	def get_employed(self):
		return(self.employed)

	def get_no_missed_payments(self):
		return(self.no_missed_payments)

	def get_no_credit_cards(self):
		return(self.no_credit_cards)

	# Setters
	def set_age(self, d):
		self.age = d

	def set_no_children(self, d):
		self.no_children = d

	def set_employed(self, d):
		self.employed = d
	def set_no_missed_payments(self, d):
		self.no_missed_payments = d

	def set_no_credit_cards(self, d):
		self.no_credit_cards = d


def main():
	# Create instance (i.e Object)
	employee_1 = Loan_applicant(name = "Joe", age = 25, no_children = 0, employed = False, salary = 0)

	print(employee_1.get_age())

if __name__ == '__main__':
	main()

	





