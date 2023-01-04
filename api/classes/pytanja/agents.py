from copy import deepcopy


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


def getNeighborsDict(tiles):
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

    return neighborDict


def dfs(node, path, visited, finishPosition, neighborDict):
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
                dfs(neighbor, path, visited, finishPosition, neighborDict)


class Aki(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentPath(self, map):
        tiles = map.tiles
        finishPosition = map.finishPosition
        neighborDict = getNeighborsDict(tiles)

        visited = set()  # Visited nodes are added here (set is used to prevent duplicates)
        path = []

        dfs(tiles[self.row][self.col], path,
            visited, finishPosition, neighborDict)
        return path


class Jocke(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentPath(self, map):
        tiles = map.tiles
        finishPosition = map.finishPosition
        neighborDict = getNeighborsDict(tiles)

        visited = set()  # Visited nodes are added here (set is used to prevent duplicates)
        queue = []  # every element of queue is path

        startTile = tiles[self.row][self.col]
        queue.append([startTile])
        visited.add((startTile.row, startTile.col))
        while queue:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            currNode = (node.row, node.col)

            side = 1
            neighbors = neighborDict[currNode].copy()
            # for every neighbor, we give it preference with side and with average cost of all neighbors
            for neighbor in neighbors:
                neighbor.side = side
                side += 1
                price = 0
                count = 0
                innerNode = (neighbor.row, neighbor.col)
                innerNeighbors = neighborDict[innerNode].copy()
                for innerNeighbor in innerNeighbors:
                    price += innerNeighbor.cost
                    count += 1
                if price == 0:
                    neighbor.averageCost = 0
                else:
                    neighbor.averageCost = price / count

            neighbors.sort(key=lambda tile: (tile.averageCost, tile.side))

            for nbr in neighbors:
                nbrNode = (nbr.row, nbr.col)
                if nbrNode not in visited:
                    newPath = list(path)
                    newPath.append(nbr)
                    queue.append(newPath)
                    visited.add(nbrNode)
                    # path found
                    if nbrNode[0] == finishPosition.row and nbrNode[1] == finishPosition.col:
                        return newPath


class Draza(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentPath(self, map):
        tiles = map.tiles
        finishPosition = map.finishPosition
        neighborDict = getNeighborsDict(tiles)

        startTile = tiles[self.row][self.col]
        paths = [
            {
                "path": [startTile],
                "price": startTile.cost
            }
        ]

        while paths:
            # get the smallest path from the queue
            path = paths.pop(0)
            # get the last node from the path
            node = path["path"][-1]

            # dynamic programming
            # we get rid of all paths that are longer
            filteredPaths = []
            for dict in paths:
                tempNode = dict["path"][-1]
                if node != tempNode:
                    filteredPaths.append(dict)

            paths = filteredPaths

            currNode = (node.row, node.col)
            # path found
            if currNode[0] == finishPosition.row and currNode[1] == finishPosition.col:
                return path["path"]

            neighbors = neighborDict[currNode]

            # for every neighbor, if it is NOT in current path, add it to path
            for neighbor in neighbors:
                pathCoordinates = []
                for p in path["path"]:
                    pathCoordinates.append((p.row, p.col))
                if (neighbor.row, neighbor.col) not in pathCoordinates:
                    newPath = deepcopy(path)
                    newPath["path"].append(neighbor)
                    newPath["price"] += neighbor.cost
                    paths.append(newPath)

            paths.sort(key=lambda d: (d['price'], len(d['path'])))


class Bole(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentPath(self, map):
        tiles = map.tiles
        finishPosition = map.finishPosition
        neighborDict = getNeighborsDict(tiles)

        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                dx = abs(finishPosition.row - i)
                dy = abs(finishPosition.col - j)
                tiles[i][j].heuristics = 2 * (dx + dy)

        startTile = tiles[self.row][self.col]
        paths = [
            {
                "path": [startTile],
                "price": startTile.cost,
                "heuristics": startTile.heuristics
            }
        ]

        while paths:
            # get the smallest path from the queue
            path = paths.pop(0)
            # get the last node from the path
            node = path["path"][-1]

            # dynamic programming
            # we get rid of all paths that are longer
            filteredPaths = []
            for dict in paths:
                tempNode = dict["path"][-1]
                if node != tempNode:
                    filteredPaths.append(dict)

            paths = filteredPaths

            currNode = (node.row, node.col)
            # path found
            if currNode[0] == finishPosition.row and currNode[1] == finishPosition.col:
                return path["path"]

            neighbors = neighborDict[currNode]

            # for every neighbor, if it is NOT in current path, add it to path
            for neighbor in neighbors:
                pathCoordinates = []
                for p in path["path"]:
                    pathCoordinates.append((p.row, p.col))
                if (neighbor.row, neighbor.col) not in pathCoordinates:
                    newPath = deepcopy(path)
                    newPath["path"].append(neighbor)
                    newPath["price"] += neighbor.cost
                    newPath["heuristics"] = neighbor.heuristics
                    paths.append(newPath)

            paths.sort(key=lambda d: (
                d['price'] + d['heuristics'], len(d['path'])))
