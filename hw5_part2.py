'''
Author: Christina Elmore
RIN: 661542904
Section: 02
Assignment: HW 5 Part 2
Purpose: Gather data about a randomly walking turtle every 20 steps for 250 time units or until it falls of the board.
'''
import sys
import random

def move_turtle( row, col, dir, turn_prob ): #turns the turtle or makes it take a step, probability of turning is based on turn_prob
    if random.random() < turn_prob: #turn 90 degrees
        if dir == "right":
            dir = "down"             
        elif dir == "left":
            dir = "up"       
        elif dir == "up":
            dir = "right"
        elif dir == "down":
            dir = "left"        
        
    else:  #takes a step in curent direction                 
        if dir == "left":
            col = col - 1
        elif dir == "right":
            col = col + 1
        elif dir == "up":
            row = row - 1
        elif dir == "down":
            row = row + 1  
    return [row, col, dir]

def run_one_simulation( grid_count, turn_prob, turtle ): #run a full simulation of the turtle moving
    turtle_on = True
    i = 0
    while i < 250:
        i += 1
        turtle = move_turtle( turtle[0], turtle[1], turtle[2], turn_prob )
        if turtle[0] == -1:
            turtle_on = False
            break
        if turtle[0] == M:
            turtle_on = False
            break
        if turtle[1] == -1:
            turtle_on = False
            break
        if turtle[1] == N:
            turtle_on = False
            break
        grid_count[turtle[0]][turtle[1]] += 1
    return [i, turtle_on]

 
M = int(raw_input('Enter the integer number of rows => '))
print M
N = int(raw_input('Enter the integer number of cols => '))
print N
turn_prob = float(raw_input("Enter the turtle's turn probability (< 1.0) => "))
print turn_prob
sim_num = int(raw_input('Enter the number of simulations to run => '))
print sim_num

seed_value = 10*M + N
random.seed(seed_value)

grid_count = []
for i in range(M):
    grid_count.append( [0]*N )
    
#runs the simulation a given number of times and gathers information about time statistics
min_time = 250
max_time = 0
times = []
fell_off = []
j = 0
while j < sim_num:
    grid_count[M/2][N/2] = grid_count[M/2][N/2] +1
    dir_list = ['right', 'down', 'left', 'up']
    rand_index = random.randint(0,3)
    dir = dir_list[rand_index]
    turtle = [M/2, N/2, dir]
    sim = run_one_simulation( grid_count, turn_prob, turtle )
    times.append(sim[0])
    if sim[0] < min_time:
        min_time = sim[0]
    if sim[0] > max_time:
        max_time = sim[0]
    if sim[1] == False:
        fell_off.append(1)
    j += 1
avg_time = float(sum(times)) / len(times)
percent_fell_off = (float(len(fell_off)) / sim_num)*100

#prints statistics about the turtle walk simulations
print ''
print "Completed simulation."
print "Min time to end: %d." %(min_time)
print "Max time to end: %d." %(max_time)
print "Average time to end: %4.1f. " %(avg_time)
print "Percentage that ended when the turtle fell off is %4.1f." %(percent_fell_off)
print ''

#formats and prints the grid of counts
print "Grid of counts:"
x = 0
while x < M:
    y = 0
    row = []
    while y < N:
        string_int = "%4d" %(grid_count[x][y])
        row.append(string_int) 
        y += 1
    print ''.join(row)
    x += 1

#finds and prints the max count occurance
max_count = 0
x = 0
max_location = []
while x < M:
    y = 0
    while y < N:
        if grid_count[x][y] > max_count:
            max_count = grid_count[x][y]
            max_location.append([x,y])
        y += 1
    x += 1
max_percent = ((float(max_count)) / (sum(times)))*100
print "Max count occurs at (%d,%d) with percentage %.2f." %(max_location[-1][0], max_location[-1][1], max_percent-.001)
