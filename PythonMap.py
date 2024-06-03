#
#Authors: Lachlan Gill and Jacob Bartle
#Periods: 2 and 3
#This code takes the input of a current location in the building and a destination room number and outputs the quickest route there using coordinates via a grid of the school pathways
#Upper portion of code adapted from the A* Pathfinding algorithm from https://www.geeksforgeeks.org/a-search-algorithm/ accessed on Friday, 5/23/24
#

#Imported libraries and global variables here
import math
import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Define the source and destination from inputs x and y- elifs assign different room inputs to their coordinates
x = input('Please input your starting location. Capitalize the mod letter:  ')
if x == 'A103':
    src = [11, 10]
elif x =='A104':
    src = [11, 7]
elif x =='A105':
    src = [9, 4]
elif x =='A110':
    src = [6, 5]
elif x =='A111':
    src = [7, 5]
elif x =='A112':
    src = [8, 5]
elif x =='A113':
    src = [9, 5]
elif x =='A117':
    src = [8, 8]
elif x =='A118':
    src = [9, 8]
elif x =='A122':
    src = [11, 13]
elif x =='A123':
    src = [5, 13]
elif x =='A124':
    src = [5, 15]
elif x =='A127':
    src = [6, 16]
elif x =='A128':
    src = [9, 20]
elif x =='A133':
    src = [6, 24]
elif x =='A134':
    src = [8, 24]
elif x =='A135':
    src = [10, 24]
elif x =='A136':
    src = [12, 24]
elif x =='A138':
    src = [0, 0]
elif x =='A139':
    src = [0, 4]
elif x =='A140':
    src = [0, 6]
elif x =='A141':
    src = [0, 6]
elif x =='A143':
    src = [0, 1]
elif x =='A144':
    src = [1, 2]
elif x =='A145':
    src = [3, 2]
elif x =='A146':
    src = [5, 2]
elif x =='A147':
    src = [5, 5]
elif x =='A148' or x=='theater' or x=='theatre':
    src = [0, 8]
elif x =='A149':
    src = [5, 10]
elif x =='A150':
    src = [5, 14]
elif x =='A151':
    src = [5, 17]
elif x =='A152':
    src = [5, 19]
elif x =='A153':
    src = [5, 21]
elif x =='A155' or x=='robotics' or x=='rob' or x=='robot':
    src = [0, 23]
elif x =='A157' or x=='robotics' or x=='rob' or x=='robot':
    src = [0, 23]
elif x =='B103':
    src = [11, 29]
elif x =='B114' or x=='gym' or x=='Gym' or x=='gymnasium' or x=='Gymnasium':
    src = [2, 34]
elif x =='B116':
    src = [5, 33]
elif x =='B117':
    src = [4, 32]
elif x =='B137' or x=='tefft' or x=='Tefft' or x=='Tefft Library' or x=='tefft library' or x=='library':
    src = [14, 46]
elif x =='B141':
    src = [8, 41]
elif x =='B142':
    src = [10, 41]
elif x =='B143':
    src = [12, 41]
elif x =='B145':
    src = [16, 41]
elif x =='B146':
    src = [15, 45]
elif x =='B147':
    src = [15, 47]
elif x =='B148':
    src = [15, 49]
elif x =='Lobby' or x == 'lobby':
    src = [14, 36]
elif x =='Directors' or x=='directors' or x=='Director' or  x=='director' or x=='dir' or x=='Dir':
    src = [14, 32]
elif x =='Cafeteria' or x=='cafeteria' or x=='Cafe' or x=='cafe' or x=='Caf' or x=='caf':
    src = [4, 39]
elif x =='Copy' or x=='copy':
    src = [10, 31]
elif x =='Jr/Sr' or x=='jr/sr' or x=='JrSr' or x=='jrsr':
    src = [11, 13]
elif x =='A Bath' or x=='A bath' or x=='Abath' or x=='ABath' or x=='abath':
    src = [5, 7]
elif x =='B Bath' or x=='B bath' or x=='Bbath' or x=='BBath' or x=='bbath':
    src = [11, 36]
else:
    print("Sorry, I didn't get that. Please restart")
        
y = input('Please input your destination. Capitalize the mod letter: ')
if y == 'A103':
    dest = [11, 10]
elif y =='A104':
    dest = [11, 7]
elif y =='A105':
    dest = [9, 4]
elif y =='A110':
    dest = [6, 5]
elif y =='A111':
    dest = [7, 5]
elif y =='A112':
    dest = [8, 5]
elif y =='A113':
    dest = [9, 5]
elif y =='A117':
    dest = [8, 8]
elif y =='A118':
    dest = [9, 8]
elif y =='A122':
    dest = [11, 13]
elif y =='A123':
    dest = [5, 13]
elif y =='A124':
    dest = [5, 15]
elif y =='A127':
    dest = [6, 16]
elif y =='A128':
    dest = [9, 20]
elif y =='A133':
    dest = [6, 24]
elif y =='A134':
    dest = [8, 24]
elif y =='A135':
    dest = [10, 24]
elif y =='A136':
    dest = [12, 24]
elif y =='A138':
    dest = [0, 0]
elif y =='A139':
    dest = [0, 4]
elif y =='A140':
    dest = [0, 6]
elif y =='A141':
    dest = [0, 6]
elif y =='A143':
    dest = [0, 1]
elif y =='A144':
    dest = [1, 2]
elif y =='A145':
    dest = [3, 2]
elif y =='A146':
    dest = [5, 2]
elif y =='A147':
    dest = [5, 5]
elif y =='A148' or y=='theater' or y=='theatre':
    dest = [0, 8]
elif y =='A149':
    dest = [5, 10]
elif y =='A150':
    dest = [5, 14]
elif y =='A151':
    dest = [5, 17]
elif y =='A152':
    dest = [5, 19]
elif y =='A153':
    dest = [5, 21]
elif y =='A155' or y=='robotics' or y=='rob' or y=='robot':
    dest = [0, 23]
elif y =='A157' or y=='robotics' or y=='rob' or y=='robot':
    dest = [0, 23]
elif y =='B103':
    dest = [11, 29]
elif y =='B114' or y=='gym' or y=='Gym' or y=='gymnasium' or y=='Gymnasium':
    dest = [2, 34]
elif y =='B116':
    dest = [5, 33]
elif y =='B117':
    dest = [4, 32]
elif y =='B137' or y=='tefft' or y=='Tefft' or y=='Tefft Library' or y=='tefft library' or y=='library':
    dest = [14, 46]
elif y =='B141':
    dest = [8, 41]
elif y =='B142':
    dest = [10, 41]
elif y =='B143':
    dest = [12, 41]
elif y =='B145':
    dest = [16, 41]
elif y =='B146':
    dest = [15, 45]
elif y =='B147':
    dest = [15, 47]
elif y =='B148':
    dest = [15, 49]
elif y =='Lobby' or y == 'lobby':
    dest = [14, 36]
elif y =='Directors' or y=='directors' or y=='Director' or y=='director' or y=='dir' or y=='Dir':
    dest = [14, 32]
elif y =='Cafeteria' or y=='cafeteria' or y=='Cafe' or y=='cafe' or y=='Caf' or y=='caf':
    dest = [4, 39]
elif y =='Copy' or y=='copy':
    dest = [10, 31]
elif y =='Jr/Sr' or y=='jr/sr' or y=='JrSr' or y=='jrsr':
    dest = [11, 13]
elif y =='A Bath' or y=='A bath' or y=='Abath' or y=='ABath' or y=='abath':
    dest = [5, 7]
elif y =='B Bath' or y=='B bath' or y=='Bbath' or y=='BBath' or y=='bbath':
    dest = [11, 36]
else:
    print("Sorry, I didn't get that. Please restart")




# Define the Cell class
class Cell:
    def __init__(self):
        self.parent_i = 0  # Parent cell's row index
        self.parent_j = 0  # Parent cell's column index
        self.f = float('inf')  # Total cost of the cell (g + h)
        self.g = float('inf')  # Cost from start to this cell
        self.h = 0  # Heuristic cost from this cell to destination
 
# Define the size of the grid
ROW = 18
COL = 51
 
# Check if a cell is valid within the grid
def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)
 
# Check if a cell is unblocked
def is_unblocked(grid, row, col):
    return grid[row][col] == 1
 
# Check if a cell is the destination
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]
 
# Calculate the heuristic value of a cell (Euclidean distance to destination)
def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5
 
# Trace the path from source to destination
def trace_path(cell_details, dest):
    print("The Path is: ")
    path = []
    row = dest[0]
    col = dest[1]
 
    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col
 
    # Add the source cell to the path
    path.append((row, col))
    # Reverse the path to get the path from source to destination
    path.reverse()
 
    # Print the path
    for i in path:
        print("->", i, end=" ")
    print()
 
# Implement the A* search algorithm
def a_star_search(grid, src, dest):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return
 
    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or the destination is blocked")
        return
 
    # Check if already at the destination
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return
 
    # Initialize the closed list (visited cells)
    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    # Initialize the details of each cell
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]
 
    # Initialize the start cell details
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j
 
    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))
 
    # Initialize the flag for whether destination is found
    found_dest = False
 
    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)
 
        # Mark the cell as visited
        i = p[1]
        j = p[2]
        closed_list[i][j] = True
 
        # For each direction, check the successors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]
 
            # If the successor is valid, unblocked, and not visited
            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                # If the successor is the destination
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    print("The destination cell is found")
                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest)
                    found_dest = True
                    return
                else:
                    # Calculate the new f, g, and h values
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new
 
                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        # Update the cell details
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
 
    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")
 
def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
 
    

    # Run the A* search algorithm
    a_star_search(grid, src, dest)
 
if __name__ == "__main__":
    main()
