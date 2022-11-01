from itertools import count


class Agent():
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getAgentPath(self, map):
        pass


class Aki(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentPath(self, map):
        tiles = map.tiles
        finishPosition = map.finishPosition
        neighborDict = {}  # empty dictionary that we need to fill
        # key => (i, j) -> i - row, j - column
        # value => array of neighbors arranged like up, right, down, left
        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                neighbors = []
                # add upper tile if exists

                if i-1 >= 0:
                    tile = tiles[i-1][j]
                    neighbors.append(tiles[i-1][j])

                # add right tile if exists
                if j+1 < len(tiles[i]):
                    neighbors.append(tiles[i][j+1])

                # add down tile if exists
                if i+1 < len(tiles):
                    neighbors.append(tiles[i+1][j])

                # add left tile if exists
                if j-1 >= 0:
                    neighbors.append(tiles[i][j-1])

                neighborDict[(i, j)] = neighbors

        visited = set()  # Visited nodes are added here (set is used to prevent duplicates)
        path = []

        def dfs(node):
            currNode = (node.row, node.col)
            if currNode not in visited:
                path.append(node)
                visited.add(currNode)

                print("----", currNode)
                print()
                # neighbors = neighborDict[currNode]
                neighbors = neighborDict[currNode].copy()

                # variable side is used to give preference to sides.
                # we go through neighbors list (which is already sorted as north, east, south, west),
                # but we give those sides integer values to be able to sort them by that field easily
                side = 1
                for neighbor in neighbors:
                    neighbor.side = side
                    side += 1

                neighbors.sort(key=lambda tile: (tile.cost, tile.side))

                for neighbor in neighbors:
                    # condition to stop calling recursive method if finish is found
                    if (finishPosition.row, finishPosition.col) not in visited:
                        dfs(neighbor)

        dfs(tiles[self.row][self.col])
        return path
