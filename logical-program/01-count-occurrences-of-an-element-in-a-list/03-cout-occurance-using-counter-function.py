from collections import Counter

# The counter method returns a dictionary with occurrences of all elements as a key-value pair, where the key is the element and the value is the number of times that element has occurred. 
data = [8, 6, 8, 10, 8, 20, 10, 8, 8]

output = Counter(data)

for key,value in output.items():
    print(f"Count of {key} is {value}")