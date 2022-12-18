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

# Assign every three lines to temporary array as sets to find common character and populate shared array
arr_temp = []
for i in range(len(lines)):
    arr_temp.append(set(lines[i]))
    if (i + 1) % 3 == 0:
        shared.append(arr_temp[0] & arr_temp[1] & arr_temp[2])
        arr_temp = []

# Caclulate sum of shared characters by dictionary reference 
for i in range(len(shared)):
    sum += priority[shared[i].pop()]

print("The sum of priorities is", sum)
