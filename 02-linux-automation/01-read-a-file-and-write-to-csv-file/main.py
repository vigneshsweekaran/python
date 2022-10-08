import csv

with open('sample.txt', 'r') as input_file:
    data = [ line.strip() for line in input_file ]

with open('output.csv', 'w') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(data)
