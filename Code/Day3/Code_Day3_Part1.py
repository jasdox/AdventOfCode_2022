# Read and store input by line
data = open("Documents\GitHub\AdventOfCode_2022\Inputs\day3.txt", 'r')
lines = data.readlines()
lines = [item.strip() for item in lines]

# Initialize
shared = []
priority = {}
sum = 0

# Populate priority dictionary with scores (1-52) and characters iterating through alphabet 
for i, j in zip(list(range(97, 123)) + list(range(65, 91)), range(52)):
    priority[chr(i)] = j + 1

# Split each line at the midpoint into two sets 
for i in range(len(lines)):
    mid = int(len(lines[i])/2)
    sacks = [set(lines[i][:mid]), set(lines[i][mid:])]
    lines[i] = sacks

# Populate the list of shared characters by the overlap in sets of each line 
for i in range(len(lines)):
    shared.append(lines[i][0] & lines[i][1])

# Caclulate sum of shared characters by dictionary reference 
for i in range(len(shared)):
    sum += priority[shared[i].pop()]

print("The sum of priorities is", sum)
