data = [8, 6, 8, 10, 8, 20, 10, 8, 8]
duplicates_removed = set(data)
output = {}

for i in duplicates_removed:
    print(f"Count of {i} is {data.count(i)}")