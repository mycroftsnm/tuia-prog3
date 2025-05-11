from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
from .heuristicas import distancia_manhattan

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = True
        
        frontier = PriorityQueueFrontier()
        frontier.add(node, 0)

        while not frontier.is_empty():
            node = frontier.pop()
            for action, new_state in grid.get_neighbours(node.state).items():
                if new_state in explored and explored[new_state] <= node.cost + grid.get_cost(new_state) :
                    continue
                neighbour = Node("",
                            new_state,
                            node.cost + grid.get_cost(new_state),
                            node,
                            action)
                explored[new_state] = neighbour.cost
                if new_state == grid.end:
                    return Solution(node, explored)
                frontier.add(neighbour, distancia_manhattan(new_state, grid.end))


        return NoSolution(explored)
    

