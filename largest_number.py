# A function that returns the largest number in a list of integers taken

# if len of a == 1 it will return a to its 1st postion
# if a[0] is bigger than recursive(a[1:]) it will recursively call the function 
# print statemens prints out the largest number in the 2 lists 
def recursive(a):
    if len(a) == 1:
        return a[0]
    else:
        return a[0] if a[0] > recursive(a[1:]) else recursive(a[1:])

print(recursive([1, 4, 5, 3,]))
print(recursive([3, 1, 6, 8, 2, 4, 5]))

# w3 schools/Applied Recursion 
# Stackoverflow "Recursive functions"



