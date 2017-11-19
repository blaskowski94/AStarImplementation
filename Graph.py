from typing import Dict, List, Tuple


class Graph:
    def __init__(self, edges: Dict[Tuple, List[Tuple]]) -> None:
        self.edges = edges

    def neighbors(self, index: Tuple) -> List[Tuple]:
        return self.edges[index]
