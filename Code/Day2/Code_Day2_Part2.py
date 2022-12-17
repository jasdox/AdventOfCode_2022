# Read in input by lines
data = open("Documents\GitHub\AdventOfCode_2022\Inputs\day2.txt", 'r')
lines = data.readlines()

# Initialize
score = 0

for i in range(len(lines)):
# Give 3 points for tie, 6 points for win
    if lines[i][2] == 'Y':
        score += 3
    elif lines[i][2] == 'Z':
        score += 6

# If opponent plays rock, loss is scissors, tie is rock, win is paper, give points accordingly 
    if lines[i][0] == 'A':
        if lines[i][2] == 'X':
            score += 3
        elif lines[i][2] == 'Y':
            score += 1
        elif lines[i][2] == 'Z':
            score += 2

# If opponent plays paper, loss is rock, tie is paper, win is scissors, give points accordingly 
    elif lines[i][0] == 'B':
        if lines[i][2] == 'X':
            score += 1
        elif lines[i][2] == 'Y':
            score += 2
        elif lines[i][2] == 'Z':
            score += 3

# If opponent plays scissors, loss is paper, tie is scissors, win is rock, give points accordingly 
    elif lines[i][0] == 'C':
        if lines[i][2] == 'X':
            score += 2
        elif lines[i][2] == 'Y':
            score += 3
        elif lines[i][2] == 'Z':
            score += 1

print("The score is ", score)    
        

