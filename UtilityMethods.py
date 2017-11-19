import numpy as np
from Graph import *
from typing import Tuple, List


def node_neighbors(node: Tuple, all_nodes: List[Tuple]) -> List[Tuple]:
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []
    for dr in dirs:
        neighbor = tuple(np.add(node, dr))
        if neighbor in all_nodes:
            result.append(neighbor)
    return result


def draw_path(maze_char_ary: List[List[chr]], best_path: List[Tuple], begin_char: chr = 'A', end_char: chr = 'B',
              path_char: chr = '@') -> None:
    for step in best_path:
        if maze_char_ary[step[0]][step[1]] is not begin_char and maze_char_ary[step[0]][step[1]] is not end_char:
            maze_char_ary[step[0]][step[1]] = path_char

    for row in range(len(maze_char_ary)):
        for col in range(len(maze_char_ary[row])):
            print(maze_char_ary[row][col], end='')
        print()


def calculate_valid_nodes(character_maze: List[List[chr]], begin_char: chr = 'A', end_char: chr = 'B',
                          path_char: chr = '.') -> Tuple[List[Tuple], Tuple, Tuple]:
    valid_nodes = []
    begin = (-1, -1)
    end = (-1, -1)
    for row in range(len(character_maze)):
        for col in range(len(character_maze[row])):
            ch = character_maze[row][col]
            if ch == begin_char:
                valid_nodes.append((row, col))
                begin = (row, col)
            elif ch == end_char:
                valid_nodes.append((row, col))
                end = (row, col)
            elif ch == path_char:
                valid_nodes.append((row, col))
    if begin == (-1, -1):
        raise RuntimeError("Beginning char not found")
    if end == (-1, -1):
        raise RuntimeError("Ending char not found")
    if len(valid_nodes) == 0:
        raise RuntimeError("No valid path chars found")
    return valid_nodes, begin, end


def calculate_all_neighbors(all_nodes: List[Tuple]) -> Graph:
    neigh = {}
    for node in all_nodes:
        neigh[node] = node_neighbors(node, all_nodes)
    return Graph(neigh)
