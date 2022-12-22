from collections import deque

# Take the full instruction line and return an array with the three important numbers
def read_instructions(line):
    arr = line.split()
    instructions = [int(arr[1]), int(arr[3]), int(arr[5])]
    return instructions


# Read and store input by line
data = open("Documents\\GitHub\\AdventOfCode_2022\\Inputs\\day5.txt", 'r')
lines = data.readlines()

# Intitialize
stacks = [deque([]) for i in range(9)]
i = 0

# Line by line assign any non blank character for the box to a queue according to the column it is in 
while lines[i+1] !='\n':
    for j in range(9):
        if lines[i][1+(j*4)] != ' ':
            stacks[j].append(lines[i][1+(j*4)])
    i+=1

i+=2

# For the number of moves, add the box from the starting point to destination and remove from starting point
while i < len(lines):
    instructions = read_instructions(lines[i])
    for j in range(instructions[0]):
        stacks[instructions[2] - 1].appendleft(stacks[instructions[1] - 1][0]) 
        stacks[instructions[1] - 1].popleft()
    i+=1

print("Crates on top of stack: ", end = '')
for i in range(9):
    print(stacks[i][0], end = '')