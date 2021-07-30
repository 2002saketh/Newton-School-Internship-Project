// Write a recursive solution to print even numbers from 0 to X (x will be provided as an input) (any
language)
# Python3 program to implement
# the above approach

# Function to print all the
# even numbers from 0 to X
def Even(X):
	
	# Base case
	if (X < 0):
		return

	# Recurrence relation
	if (X % 2 == 0):
		Even(X- 2)
	else:
		Even(X- 1)

	# Check if X is even
	if (X % 2 == 0):
		print(X, end = " ")

if __name__ == '__main__':
    print("Enter starting range:") 
    x=int(input())
     
    print("Even numbers:")
 
    # Print all the
    # even numbers
    Even(x)
    print()
 
