class Tile():
    def __init__(self, type, row, col):
        price = 0
        if type == "r":
            price = 2
        elif type == "g":
            price = 3
        elif type == "m":
            price = 5
        elif type == "d":
            price = 7
        elif type == "w":
            price = 500
        elif type == "s":
            price = 1000

        self.type = type # TODO: Ne moram ni da cuvam ovaj tip
        self.cost = price
        self.row = row
        self.col = col


class AgentPosition():
    def __init__(self, row, col):
        self.row = row
        self.col = col


class FinishPosition():
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Map():
    def __init__(self, map, agentPosition, finishPosition):
        self.agentPosition = AgentPosition(agentPosition[0], agentPosition[1])
        self.finishPosition = FinishPosition(
            finishPosition[0], finishPosition[1])

        tilesMap = []
        for i in range(len(map)):
            mapRow = []
            for j in range(len(map[i])):
                tile = Tile(map[i][j], i, j)
                mapRow.append(tile)
            tilesMap.append(mapRow)

        self.tiles = tilesMap
