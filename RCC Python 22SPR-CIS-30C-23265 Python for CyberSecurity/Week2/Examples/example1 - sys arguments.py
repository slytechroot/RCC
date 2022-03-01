#Example 1

import sys
print("This is the name of the script: \n", sys.argv[0])
print("\nThe number of arguments is: \n", len(sys.argv))
print("\nThe arguments are: \n", str(sys.argv))

#we don't have these arguments yet, so these lines will cause errors
#print("The first argument is ", sys.argv[1])
#print("The second argument is ", sys.argv[2])

