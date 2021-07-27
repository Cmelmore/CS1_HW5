'''
Author: Christina Elmore
RIN: 661542904
Section: 02
Assignment: HW 5 Part 1
Purpose: Report the progress of a randomly walking turtle every 20 steps for 250 time units or until it falls of the board.
'''
import sys
import random

def move_turtle( row, col, dir, turn_prob ): 
    if random.random() < turn_prob: #turn 90 degrees
        if dir == "right":
            dir = "down"             
        elif dir == "left":
            dir = "up"       
        elif dir == "up":
            dir = "right"
        elif dir == "down":
            dir = "left"        
        
    else:  # take a step in current direction
        if dir == "left":
            col = col - 1
        elif dir == "right":
            col = col + 1
        elif dir == "up":
            row = row - 1
        elif dir == "down":
            row = row + 1  
    return [row, col, dir]

M = int(raw_input('Enter the integer number of rows => '))
print M
N = int(raw_input('Enter the integer number of cols => '))
print N
turn_prob = float(raw_input("Enter the turtle's turn probability (< 1.0) => "))
print turn_prob

seed_value = 10*M + N
random.seed(seed_value)

dir_list = ['right', 'down', 'left', 'up']
rand_index = random.randint(0,3)
dir = dir_list[rand_index]
print "Initial direction:", dir

turtle = [M/2, N/2, dir]
i = 0
while i < 250:
    i += 1
    turtle = move_turtle( turtle[0], turtle[1], turtle[2], turn_prob )
 
    if turtle[0] == -1:
        print "After %d time steps the turtle fell off the top in column %d." %(i, turtle[1])
        sys.exit()
    if turtle[0] == M:
        print "After %d time steps the turtle fell off the bottom in column %d." %(i, turtle[1])
        sys.exit()
    if turtle[1] == -1:
        print "After %d time steps the turtle fell off the left in row %d." %(i, turtle[0])
        sys.exit()
    if turtle[0] == N:
        print "After %d time steps the turtle fell off the right in row %d." %(i, turtle[0])
        sys.exit()
    if i  / 20 * 20 == i:
        print "Time step %d: position (%d,%d) direction %s." %(i, turtle[0], turtle[1], turtle[2])

if i == 250:
    print "After %d time steps the turtle ended at position (%d,%d) and direction %s." %(i, turtle[0], turtle[1], turtle[2])