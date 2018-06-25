'''
Given a positive integer n (<1000000 digits in total), print the smallest palindrome larger than n.
Number should be displayed without leading zeros.
'''

n = int(input("enter a number: ")) # get the input from the user

def nextPalindrome(n): # check for the next palindrome
    revPalindrome = 0 # initiate the reverse value of the input number to zero
    while n: # start the while loop
        revPalindrome= (revPalindrome * 10) + (n % 10) # Condition for palindrome
        n = n // 10
    return revPalindrome # Return the reverse of the input number

if n == nextPalindrome(n): # check both Input number and the Inverse for equality
    print("Input Number is Palindrome")
else: # if not then the input number is incremented using which the next Plaindrome could be found
    while True:
        n += 1
        if n == nextPalindrome(n):
            print("Smallest Palindrome Larger than input value: %s" %n)
            break	
