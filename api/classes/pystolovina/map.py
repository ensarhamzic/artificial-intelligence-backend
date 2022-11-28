class Tile():
    def __init__(self, type, row, col):
        isRoad = False
        if type == "r":
            isRoad = True

        self.isRoad = isRoad
        self.row = row
        self.col = col


class UserPosition():
    def __init__(self, row, col):
        self.row = row
        self.col = col


class AiPosition():
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Map():
    def __init__(self, map, userPosition, aiPosition):
        self.userPosition = UserPosition(userPosition[0], userPosition[1])
        self.aiPosition = AiPosition(
            aiPosition[0], aiPosition[1])

        tilesMap = []
        for i in range(len(map)):
            mapRow = []
            for j in range(len(map[i])):
                tile = Tile(map[i][j], i, j)
                mapRow.append(tile)
            tilesMap.append(mapRow)

        self.tiles = tilesMap
