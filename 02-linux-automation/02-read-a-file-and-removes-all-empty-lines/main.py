with open('sample.txt', 'r') as input_file:
    data = [ line.strip() for line in input_file if not line.isspace()]

print(len(data))

# No new lines in output file
with open('output1.txt', 'w') as output_file:
    output_file.writelines(data)

# New lines in output file
with open('output2.txt', 'w') as output_file:
    for line in data:
        output_file.write(line+"\n")