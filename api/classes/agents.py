class Agent():
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getAgentPath(self, map):
        pass


def isAdjacent(el1, el2):
    if (el1[0] == el2[0] and abs(el1[1] - el2[1]) == 1) or (el1[1] == el2[1] and abs(el1[0] - el2[0]) == 1):
        return True
    return False


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
                if len(path) > 1:
                    # if current tile is NOT adjacent to the last one in path, go back till it is
                    while not isAdjacent((path[-1].row, path[-1].col), currNode):
                        path.pop()

                path.append(node)
                visited.add(currNode)

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


class Jocke(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentPath(self, map):
        print("HERE")
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

        # visited = set()  # Visited nodes are added here (set is used to prevent duplicates)
        # path = []

        # def dfs(node):
        #     currNode = (node.row, node.col)
        #     if currNode not in visited:
        #         if len(path) > 1:
        #             # if current tile is NOT adjacent to the last one in path, go back till it is
        #             while not isAdjacent((path[-1].row, path[-1].col), currNode):
        #                 path.pop()

        #         path.append(node)
        #         visited.add(currNode)

        #         # neighbors = neighborDict[currNode]
        #         neighbors = neighborDict[currNode].copy()

        #         # variable side is used to give preference to sides.
        #         # we go through neighbors list (which is already sorted as north, east, south, west),
        #         # but we give those sides integer values to be able to sort them by that field easily
        #         side = 1
        #         for neighbor in neighbors:
        #             neighbor.side = side
        #             side += 1

        #         neighbors.sort(key=lambda tile: (tile.cost, tile.side))

        #         for neighbor in neighbors:
        #             # condition to stop calling recursive method if finish is found
        #             if (finishPosition.row, finishPosition.col) not in visited:
        #                 dfs(neighbor)

        # dfs(tiles[self.row][self.col])
        # return path

        visited = set()  # Visited nodes are added here (set is used to prevent duplicates)
        path = []
        queue = []

        def bfs(node):
            print("BFS")
            currNode = (node.row, node.col)
            visited.add(currNode)
            queue.append(node)

            while queue:
                s = queue.pop(0)
                path.append(s)
                currNode = (s.row, s.col)

                # TODO: IZBACI SVE IZ PATHA AKO TR CVOR NIJE SUSEDNI (SLICNO KAO U DFS)
                print(s.row, s.col)
                print()
                neighbors = neighborDict[currNode].copy()

                # TODO: dodaj neighborsima side isto kao u dfs
                # TODO: dodaj prosecnu cenu neposecenih suseda za svaki od neighborova
                # TODO: sortiraj neighbors prema prosecnoj ceni i strani slicno kao dfs

                for neighbor in neighbors:
                    if (neighbor.row, neighbor.col) not in visited:
                        visited.add((neighbor.row, neighbor.col))
                        queue.append(neighbor)

        bfs(tiles[self.row][self.col])
        return path
