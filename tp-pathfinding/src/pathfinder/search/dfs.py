from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

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

        frontier = StackFrontier()
        frontier.add(node)

        while not frontier.is_empty():
            node = frontier.remove()

            for action, new_state in grid.get_neighbours(node.state).items():
                if new_state in explored:
                    continue
                neighbour = Node("",
                            new_state,
                            node.cost + grid.get_cost(new_state),
                            node,
                            action)
                explored[new_state] = True
                if new_state == grid.end:
                    return Solution(neighbour, explored)
                frontier.add(neighbour)

        return NoSolution(explored)
