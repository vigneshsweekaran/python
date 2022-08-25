# program to find, whether he suqare output lies within the range

def check(x,y,l,r):
    if l < x ** y <= r:
        print(True)
    if x ** y > l and x ** y <= r:
        print(True)
    if x ** y in range(l+1, r+1):
        print(True)

check(2,3,4,10)