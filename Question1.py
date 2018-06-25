#Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.

n = int(input("Enter a Number:")) # get the number from the user
print("Prime Numbers are:")
while (n): # initiate the while loop
	if n % 2 != 0:
		print("{0}".format(n))
	n -= 1 # decrement after each iteration