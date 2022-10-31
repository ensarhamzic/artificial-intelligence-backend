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
                    neighbors.append(tiles[i-1][j].cost)

                # add right tile if exists
                if j+1 < len(tiles[i]):
                    neighbors.append(tiles[i][j+1].cost)

                # add down tile if exists
                if i+1 < len(tiles):
                    neighbors.append(tiles[i+1][j].cost)

                # add left tile if exists
                if j-1 >= 0:
                    neighbors.append(tiles[i][j-1].cost)

                neighborDict[(i, j)] = neighbors

        for keys, values in neighborDict.items():
            print(keys)
            print(values)

        visited = set()  # Set to keep track of visited nodes.
        path = [(self.row, self.col)]

        # def dfs(visited, graph, node):
        #     if node not in visited:
        #         print (node)
        #         visited.add(node)
        #         for neighbour in graph[node]:
        #             dfs(visited, graph, neighbour)
