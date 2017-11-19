import MyPriorityQueue
from Graph import *
from typing import Tuple, Dict, List


def heuristic(a: Tuple, b: Tuple) -> int:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph: Graph, begin: Tuple, end: Tuple) -> Dict[Tuple, Tuple or None]:
    frontier = MyPriorityQueue.PriorityQueue()
    frontier.put(begin, 0)
    came_from = {begin: None}
    cost_so_far = {begin: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            break

        for nxt in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost + heuristic(end, nxt)
                frontier.put(nxt, priority)
                came_from[nxt] = current

    return came_from


def reconstruct_path(came_from: Dict[Tuple, Tuple], begin: Tuple, end: Tuple) -> List[Tuple]:
    current = end
    best_path = []
    while current != begin:
        best_path.append(current)
        current = came_from[current]
    best_path.reverse()
    return best_path


