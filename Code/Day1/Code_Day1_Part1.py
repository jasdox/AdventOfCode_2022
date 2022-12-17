data = open("Documents\Advent_Of_Code_2022\Inputs\day1_part1.txt", 'r')
data = data.read()
lines = data.split("\n")

counter = 0
elfs = [0 for i in range(lines.count(''))]

for i in range(len(lines)):
    if lines[i] == '':
        counter += 1
    else:
        elfs[counter] += int(lines[i]) 

max = 0
for i in range(len(elfs)):
    if elfs[i] > max:
        max = elfs[i]

print(max)