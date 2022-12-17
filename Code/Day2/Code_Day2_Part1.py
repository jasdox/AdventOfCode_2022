# Read in input by lines
data = open("Documents\GitHub\AdventOfCode_2022\Inputs\day2.txt", 'r')
lines = data.readlines()

# Initialize
score = 0

for i in range(len(lines)):
# Give 1 point for rock, 2 for paper, 3 for scissors
    if lines[i][2] == 'X':
        score += 1
    elif lines[i][2] == 'Y':
        score += 2
    elif lines[i][2] == 'Z':
        score += 3

# If opponent plays rock, X ties and Y wins
    if lines[i][0] == 'A':
        if lines[i][2] == 'X':
            score += 3
        elif lines[i][2] == 'Y':
            score += 6

# If opponent plays paper, Y ties and Z wins
    elif lines[i][0] == 'B':
        if lines[i][2] == 'Y':
            score += 3
        elif lines[i][2] == 'Z':
            score += 6

# If opponent plays scissors, X wins and Z ties
    elif lines[i][0] == 'C':
        if lines[i][2] == 'X':
            score += 6
        elif lines[i][2] == 'Z':
            score += 3

print("The score is ", score)    
        

