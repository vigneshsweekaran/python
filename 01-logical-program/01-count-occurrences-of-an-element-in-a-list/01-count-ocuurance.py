# We keep a counter that keeps on increasing if the required element is found in the list.

def count_occurence(list, x):
    counter = 0
    for element in list:
        if element == x:
            counter = counter+1
    return counter


data = [8, 6, 8, 10, 8, 20, 10, 8, 8]
FIND_OCCURANCE=8
OUTPUT = count_occurence(data, FIND_OCCURANCE)
print(f"{FIND_OCCURANCE} has occurred {OUTPUT} times")
