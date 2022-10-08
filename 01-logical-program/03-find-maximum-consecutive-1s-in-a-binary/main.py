n = 5
binary_value = bin(n).replace("0b", "")
print(max(map(len,binary_value.split('0'))))