from AStarSearch import *
from UtilityMethods import *

file = 'Mazes/maze3.txt'
begin_char = 'A'
end_char = 'B'
wall_char = '#'
path_char = '.'

# open maze file
f = open(file, 'r')

# print original maze
print("~~~~~ ORIGINAL MAZE ~~~~~")
print(f.read() + '\n')

# return to start of file
f.seek(0)

# read lines from file and store in an array stripping newline characters
maze_str_ary = [x.strip() for x in f.readlines()]

# convert str ary to char ary
char_maze = [list(line) for line in maze_str_ary]

# calculate valid nodes, begin and end point
all_nodes, start, goal = calculate_valid_nodes(char_maze, begin_char, end_char, path_char)

# calculate coordinates of all valid neighbors of every valid node, store in Graph object
maze_graph = calculate_all_neighbors(all_nodes)

# run A* search
search_result = a_star_search(maze_graph, start, goal)

# reconstruct the path from A* results
path = reconstruct_path(search_result, start, goal)

# draw path
print("~~~~~ SOLVED MAZE ~~~~~")
draw_path(char_maze, path)
