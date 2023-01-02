class Tile():
    def __init__(self, type, row, col):
        isRoad = False
        if type == "r":
            isRoad = True

        self.isRoad = isRoad
        self.row = row
        self.col = col


class Agent():
    def __init__(self, id, row, col, type, tag):
        self.id = id
        self.row = row
        self.col = col
        self.type = type
        self.tag = tag


class Map():
    def __init__(self, map, agents, agentTurnId):
        ags = []
        for ag in agents:
            ags.append(Agent(ag["id"], ag["row"],
                       ag["col"], ag["type"], ag["tag"]))
        self.agents = ags
        self.agentTurnId = agentTurnId
        self.maxDepth = next((ag["maxDepth"]
                             for ag in agents if ag["id"] == agentTurnId), None)
        self.timeToThink = next(
            (ag["timeToThink"] for ag in agents if ag["id"] == agentTurnId), None)

        print("maxDepth", self.maxDepth)
        print("timeToThink", self.timeToThink)

        tilesMap = []
        for i in range(len(map)):
            mapRow = []
            for j in range(len(map[i])):
                tile = Tile(map[i][j], i, j)
                mapRow.append(tile)
            tilesMap.append(mapRow)

        self.tiles = tilesMap
