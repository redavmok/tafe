#Exercise 1: Write a function called chop that takes a list and 
# modifies it, removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and 
# returns a new list that contains all but the first and last elements.

letters = ['a', 'b', 'c', 'd', 'e']
# def chop(t):
#     del(t[0])
#     del(t[-1])
#     return None

# chop(letters)
# print(chop)

def middle(d):
    del(d[0])
    del(d[-1])
    return d
    
print(middle(letters))