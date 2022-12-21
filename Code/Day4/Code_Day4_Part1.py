# Read and store input by line
data = open("Documents\\GitHub\\AdventOfCode_2022\\Inputs\\day4.txt", 'r')
lines = data.readlines()
lines = [item.strip() for item in lines]

# Initialize 
counter = 0

# Split the pairs and ranges into lists and change to integer
for i in range(len(lines)):
    lines[i] = lines[i].split(',')
    lines[i][0] = lines[i][0].split('-')
    lines[i][1] = lines[i][1].split('-')
    for j in range(2):
        lines[i][0][j] = int(lines[i][0][j])
        lines[i][1][j] = int(lines[i][1][j])

# Check if first range fits within second or vice versa and add to counter 
for i in range(len(lines)):
    a1, a2, b1, b2 = lines[i][0][0], lines[i][0][1], lines [i][1][0], lines[i][1][1]
    if (a1 in range(b1, b2+1) and a2 in range(b1, b2+1)) or (b1 in range(a1, a2+1) and b2 in range(a1, a2+1)):
        counter += 1

print("Number fully contained:", counter)

