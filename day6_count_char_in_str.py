# function to count specific char in str

if __name__=="__main__":
	mystr = input("Please enter your string:")
	mychar = input("Enter character to count:")
	print(f"{mychar} occurs {mystr.count(mychar)} times")
