from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

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

        frontier = QueueFrontier()
        frontier.add(node)
        
        while True:
            node = frontier.remove()
            explored[node.state] = True

            if node.state == grid.end:
                return Solution(node, explored)

            for action, new_state in grid.get_neighbours(node.state).items():
                if new_state not in explored:
                    neighbour = Node("",
                                new_state,
                                node.cost + grid.get_cost(new_state),
                                node,
                                action)
                    frontier.add(neighbour)

        return NoSolution(explored)
