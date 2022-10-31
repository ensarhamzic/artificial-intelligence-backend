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
        finishPositions = map.finishPosition
        neighborDict = {}  # empty dictionary that we need to fill
        # key => (i, j) -> i - row, j - column
        # value => array of neighbors arranged like up, right, down, left
        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                neighbors = []
                # add upper tile if exists

                if i-1 >= 0:
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
        path = [(self.row, self.col)]

        def dfs(node):
            currNode = (node.row, node.col)
            if currNode not in visited:
                print("----", currNode)
                visited.add(currNode)
                neighbors = neighborDict[currNode]

                # Here, we make a set (which ignores duplicate values), and populate it with
                # prices of every neighbor. After that, we compare length of set to the number of unvisited neighbors,
                # and if they are the same it means that every neighbor has different price, but if
                # they are not the same, that means that at least 2 neighbor tiles have same price.
                # We need this information to decide which neighbors to give advantage to
                prices = set()
                counter = 0
                for neighbor in neighbors:
                    if (neighbor.row, neighbor.col) not in visited:
                        print("ADDED", neighbor.row, neighbor.col)
                        prices.add(neighbor.cost)
                        counter += 1
                if len(prices) == counter:
                    # sort neighbors ascending
                    neighborDict[currNode] = sorted(
                        neighbors, key=lambda tile: tile.cost)
                    for tile in neighborDict[currNode]:
                        print("COST", tile.cost)

                for neighbor in neighborDict[currNode]:
                    dfs(neighbor)

        dfs(tiles[self.row][self.col])
