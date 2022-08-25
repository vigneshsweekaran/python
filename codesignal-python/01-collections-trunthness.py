xs = [()] # It is not empty, inside the list we have the empty tuple in first index

res = [False] * 2 # Returns [False, False] If we multiply the list, it will repeat that items multiple items in list

if xs: # This condition evaluates to True, since we have empty tuple inside the list
    res[0] = True

if xs[0]: # This condition evaluates to False, since the tuple is empty.
    res[1] = True

print (res)

# Output:
# [True, False]
