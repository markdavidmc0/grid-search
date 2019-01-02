#!/usr/bin/env python


class GridSearch:
    """shortest path finder for objective in grid, given obstacles"""

    def __init__(self, n: int, grid: list):
        self.all_nodes = []
        self.n = n
        self.grid = grid
        self.master_path = []
        self.queue = {0: (0, 0)}

    def search(self) -> int:
        """ Find length of shortest path to objective if any in n x n grid

        :return: shortest path to 9 (objective)
        """
        # crete node list
        for x in range(self.n):
            for y in range(self.n):
                if not self.grid[y][x] == 0:
                    self.all_nodes.append((x, y))
        # recursively create paths
        i = 0
        paths = [[(0, 0)]]
        while i < self.n * self.n:
            paths = self.generate_paths(paths)
            if isinstance(paths, int):
                return paths
            i += 1

        return -1

    def generate_paths(self, paths: list) -> list or int:
        """ Follow paths from starting block towards objectives

        :return: shortest path to 9 (objective)
        """
        path_count = 0
        new_paths = {}
        # follow each path in the paths list
        for path in paths:
            # find neighbours from last position in each path
            neighbours = self.neighbours(path[-1])
            for neighbour in neighbours:
                if neighbour in self.queue.values():
                    continue  # if neighbour in queue, go to next neighbour
                # find grid value of neighbour
                grid_value = self.grid[neighbour[1]][neighbour[0]]
                if grid_value == 1:
                    new_paths[path_count] = path.copy()
                    new_paths[path_count].append(neighbour)  # add path to dict
                    self.queue[path_count + 1] = neighbour  # add neighbour to queue
                    path_count += 1  # increase count of number of paths
                if grid_value == 9:
                    return len(path)

        # roll dict out into list of paths
        paths_store = [new_paths[key] for key in new_paths]

        return paths_store

    def neighbours(self, node: list) -> list:
        """ Find all valid neighbours to a node

        :param node: x-y coordinate of node
        :return: list of x-y coordinates corresponding to neighbour grid locations
        """
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        neighbours = []
        for direction in dirs:
            neighbour = (node[0] + direction[0], node[1] + direction[1])
            if neighbour in self.all_nodes:
                neighbours.append(neighbour)
        return neighbours
