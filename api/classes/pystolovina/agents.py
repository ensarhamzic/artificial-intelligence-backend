from copy import deepcopy


def isGameOver(map):  # TODO: MNOGO LOS KOD, MORA DA SE OPTIMIZUJE
    userRow = map.userPosition.row
    userCol = map.userPosition.col

    aiRow = map.aiPosition.row
    aiCol = map.aiPosition.col

    userGameOver = True
    aiGameOver = True

    if(userRow - 1 >= 0):
        if map.tiles[userRow - 1][userCol].isRoad and (userRow - 1 != aiRow or userCol != aiCol):
            # print("U3")
            userGameOver = False
        if(userCol - 1 >= 0):
            if (map.tiles[userRow - 1][userCol - 1].isRoad and (userRow - 1 != aiRow or userCol - 1 != aiCol)):
                # print("U1")
                userGameOver = False
        if(userCol + 1 < len(map.tiles[0])):
            if map.tiles[userRow - 1][userCol + 1].isRoad and (userRow - 1 != aiRow or userCol + 1 != aiCol):
                # print("U4")
                userGameOver = False

    if userCol - 1 >= 0:
        if map.tiles[userRow][userCol - 1].isRoad and (userRow != aiRow or userCol - 1 != aiCol):
            # print("U2")
            userGameOver = False
    if userCol + 1 < len(map.tiles[0]):
        if map.tiles[userRow][userCol + 1].isRoad and (userRow != aiRow or userCol + 1 != aiCol):
            # print("U5")
            userGameOver = False

    if(userRow + 1 < len(map.tiles)):
        if map.tiles[userRow + 1][userCol].isRoad and (userRow + 1 != aiRow or userCol != aiCol):
            # print("U7")
            userGameOver = False
        if(userCol - 1 >= 0):
            if map.tiles[userRow + 1][userCol - 1].isRoad and (userRow + 1 != aiRow or userCol - 1 != aiCol):
                # print("U6")
                userGameOver = False
        if(userCol + 1 < len(map.tiles[0])):
            if map.tiles[userRow + 1][userCol + 1].isRoad and (userRow + 1 != aiRow or userCol + 1 != aiCol):
                # print("U8")
                userGameOver = False

    if(aiRow - 1 >= 0):
        if map.tiles[aiRow - 1][aiCol].isRoad and (aiRow - 1 != userRow or aiCol != userCol):
            # print("A3")
            aiGameOver = False
        if(aiCol - 1 >= 0):
            if (map.tiles[aiRow - 1][aiCol - 1].isRoad and (aiRow - 1 != userRow or aiCol - 1 != userCol)):
                # print("A1")
                aiGameOver = False
        if(aiCol + 1 < len(map.tiles[0])):
            if map.tiles[aiRow - 1][aiCol + 1].isRoad and (aiRow - 1 != userRow or aiCol + 1 != userCol):
                # print("A4")
                aiGameOver = False

    if aiCol - 1 >= 0:
        if map.tiles[aiRow][aiCol - 1].isRoad and (aiRow != userRow or aiCol - 1 != userCol):
            # print("A2")
            aiGameOver = False

    if aiCol + 1 < len(map.tiles[0]):
        if map.tiles[aiRow][aiCol + 1].isRoad and (aiRow != userRow or aiCol + 1 != userCol):
            # print("A5")
            aiGameOver = False

    if(aiRow + 1 < len(map.tiles)):
        if map.tiles[aiRow + 1][aiCol].isRoad and (aiRow + 1 != userRow or aiCol != userCol):
            # print("A7")
            aiGameOver = False
        if(aiCol - 1 >= 0):
            if map.tiles[aiRow + 1][aiCol - 1].isRoad and (aiRow + 1 != userRow or aiCol - 1 != userCol):
                # print("A6")
                aiGameOver = False
        if(aiCol + 1 < len(map.tiles[0])):
            if map.tiles[aiRow + 1][aiCol + 1].isRoad and (aiRow + 1 != userRow or aiCol + 1 != userCol):
                # print("A8")
                aiGameOver = False

    # print("USER", userGameOver, "AI", aiGameOver)
    return userGameOver or aiGameOver


def evaluateMap(map):
    userPosition = map.userPosition
    aiPosition = map.aiPosition

    tiles = map.tiles

    userCords = (userPosition.row, userPosition.col)
    aiCords = (aiPosition.row, aiPosition.col)

    neighborDict = {}  # empty dictionary that we need to fill
    # key => (i, j) -> i - row, j - column
    # value => array of neighbors without tiles with holes
    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            neighbors = []

            if i-1 >= 0:
                if tiles[i-1][j].isRoad and (i-1, j) != userCords and (i-1, j) != aiCords:
                    neighbors.append(tiles[i-1][j])
                if j-1 >= 0:
                    if tiles[i - 1][j - 1].isRoad and (i-1, j - 1) != userCords and (i-1, j - 1) != aiCords:
                        neighbors.append(tiles[i - 1][j - 1])
                if j + 1 < len(tiles[0]):
                    if tiles[i - 1][j + 1].isRoad and (i-1, j + 1) != userCords and (i-1, j + 1) != aiCords:
                        neighbors.append(tiles[i - 1][j + 1])

            if j - 1 >= 0:
                if tiles[i][j - 1].isRoad and (i, j - 1) != userCords and (i, j - 1) != aiCords:
                    neighbors.append(tiles[i][j - 1])
            if j + 1 < len(tiles[0]):
                if tiles[i][j + 1].isRoad and (i, j + 1) != userCords and (i, j + 1) != aiCords:
                    neighbors.append(tiles[i][j + 1])

            if i+1 < len(tiles):
                if tiles[i + 1][j].isRoad and (i+1, j) != userCords and (i+1, j) != aiCords:
                    neighbors.append(tiles[i + 1][j])
                if j - 1 >= 0:
                    if tiles[i + 1][j - 1].isRoad and (i+1, j - 1) != userCords and (i+1, j - 1) != aiCords:
                        neighbors.append(tiles[i + 1][j - 1])
                if j + 1 < len(tiles[0]):
                    if tiles[i + 1][j + 1].isRoad and (i+1, j + 1) != userCords and (i+1, j + 1) != aiCords:
                        neighbors.append(tiles[i + 1][j + 1])

            # if tile has more than one adjacent tiles (it is not one-way tile where player loses)
            if len(neighbors) > 0:
                neighborDict[(i, j)] = neighbors

    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue

    def bfs(node):
        visited.append((node.row, node.col))
        queue.append(node)
        count = 0

        while queue:
            s = queue.pop(0)
            neighbors = []
            if (s.row, s.col) in neighborDict:
                neighbors = neighborDict[(s.row, s.col)]
            for neighbor in neighbors:
                nbr = (neighbor.row, neighbor.col)
                if nbr not in visited and nbr != aiCords and nbr != userCords:
                    count += 1
                    visited.append((neighbor.row, neighbor.col))
                    queue.append(neighbor)
        return count

    userTiles = bfs(tiles[userPosition.row][userPosition.col])
    visited = []
    queue = []
    aiTiles = bfs(tiles[aiPosition.row][aiPosition.col])
    # print("AITILES", aiTiles, "USERTILES", userTiles)

    # print("_____________________")
    # print("USER:", map.userPosition.row, map.userPosition.col)
    # print("AI:", map.aiPosition.row, map.aiPosition.col)
    # for i in range(len(map.tiles)):
    #     row = ""
    #     for j in range(len(map.tiles[i])):
    #         if map.tiles[i][j].isRoad:
    #             row += "r "
    #         else:
    #             row += "h "
    #     print(row)
    # print("AI TILES:", aiTiles)
    # print("USER TILES:", userTiles)
    # print("_____________________")

    return aiTiles - userTiles


def availableMoves(map, player):
    # returns list of moves sorted like: North, NorthEast, East, SouthEast, South, SouthWest, West, NorthWest
    moves = []
    tiles = map.tiles
    userPosition = map.userPosition
    aiPosition = map.aiPosition

    if player.row - 1 >= 0:
        if tiles[player.row - 1][player.col].isRoad:
            agentOnTile = False
            if((userPosition.row == player.row - 1 and userPosition.col == player.col) or (aiPosition.row == player.row - 1 and aiPosition.col == player.col)):
                agentOnTile = True
            if not agentOnTile:
                moves.append((player.row - 1, player.col))

    if player.row - 1 >= 0 and player.col + 1 < len(tiles[0]):
        if tiles[player.row - 1][player.col + 1].isRoad:
            agentOnTile = False
            if((userPosition.row == player.row - 1 and userPosition.col == player.col + 1) or (aiPosition.row == player.row - 1 and aiPosition.col == player.col + 1)):
                agentOnTile = True
            if not agentOnTile:
                moves.append((player.row - 1, player.col + 1))

    if player.col + 1 < len(tiles[0]):
        if tiles[player.row][player.col + 1].isRoad:
            agentOnTile = False
            if((userPosition.row == player.row and userPosition.col == player.col + 1) or (aiPosition.row == player.row and aiPosition.col == player.col + 1)):
                agentOnTile = True
            if not agentOnTile:
                moves.append((player.row, player.col + 1))

    if player.row + 1 < len(tiles) and player.col + 1 < len(tiles[0]):
        if tiles[player.row + 1][player.col + 1].isRoad:
            agentOnTile = False
            if((userPosition.row == player.row + 1 and userPosition.col == player.col + 1) or (aiPosition.row == player.row + 1 and aiPosition.col == player.col + 1)):
                agentOnTile = True
            if not agentOnTile:
                moves.append((player.row + 1, player.col + 1))

    if player.row + 1 < len(tiles):
        if tiles[player.row + 1][player.col].isRoad:
            agentOnTile = False
            if((userPosition.row == player.row + 1 and userPosition.col == player.col) or (aiPosition.row == player.row + 1 and aiPosition.col == player.col)):
                agentOnTile = True
            if not agentOnTile:
                moves.append((player.row + 1, player.col))

    if player.row + 1 < len(tiles) and player.col - 1 >= 0:
        if tiles[player.row + 1][player.col - 1].isRoad:
            agentOnTile = False
            if((userPosition.row == player.row + 1 and userPosition.col == player.col - 1) or (aiPosition.row == player.row + 1 and aiPosition.col == player.col - 1)):
                agentOnTile = True
            if not agentOnTile:
                moves.append((player.row + 1, player.col - 1))

    if player.col - 1 >= 0:
        if tiles[player.row][player.col - 1].isRoad:
            agentOnTile = False
            if((userPosition.row == player.row and userPosition.col == player.col - 1) or (aiPosition.row == player.row and aiPosition.col == player.col - 1)):
                agentOnTile = True
            if not agentOnTile:
                moves.append((player.row, player.col - 1))

    if player.row - 1 >= 0 and player.col - 1 >= 0:
        if tiles[player.row - 1][player.col - 1].isRoad:
            agentOnTile = False
            if((userPosition.row == player.row - 1 and userPosition.col == player.col - 1) or (aiPosition.row == player.row - 1 and aiPosition.col == player.col - 1)):
                agentOnTile = True
            if not agentOnTile:
                moves.append((player.row - 1, player.col - 1))

    return moves


def makeMove(map, move, player):
    print("MAKEMOVESTART", player.row, player.col, "MOVE:", move)
    map.tiles[player.row][player.col].isRoad = False

    print("_____________________")
    print("USER:", map.userPosition.row, map.userPosition.col)
    print("AI:", map.aiPosition.row, map.aiPosition.col)
    for i in range(len(map.tiles)):
        row = ""
        for j in range(len(map.tiles[i])):
            if map.tiles[i][j].isRoad:
                row += "r "
            else:
                row += "h "
        print(row)
    # print("AI TILES:", aiTiles)
    # print("USER TILES:", userTiles)
    player.row = move[0]
    player.col = move[1]
    print("USER:", map.userPosition.row, map.userPosition.col)
    print("AI:", map.aiPosition.row, map.aiPosition.col)
    print("MAKEMOVEEND", player.row, player.col, "MOVE:", move)
    print("_____________________")
    print("")
    print("")
    print("")


class Agent():
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getAgentMove(self, map):
        pass


class MinimaxAgent(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentMove(self, map):
        def minimax(map, isMax, depth):
            # print("MINIMAX")
            # Base case - the game is over, so we return the value of the board
            if isGameOver(map) or depth == 0:
                return [evaluateMap(map), ""]
            # print("RUNNING")
            bestMove = ""
            if isMax == True:
                bestValue = -float("Inf")
            else:
                bestValue = float("Inf")

            player = None
            if isMax:
                player = map.aiPosition
            else:
                player = map.userPosition

            for move in availableMoves(map, player):
                newMap = deepcopy(map)
                playerOnMove = None
                if isMax:
                    playerOnMove = newMap.aiPosition
                else:
                    playerOnMove = newMap.userPosition
                print("")
                print("")
                print("")
                print("PRE POTEZA")
                print("ISMAX:", isMax)
                print("MOVE", move)
                print("USER:", newMap.userPosition.row, newMap.userPosition.col)
                print("AI:", newMap.aiPosition.row, newMap.aiPosition.col)
                if(newMap.tiles[playerOnMove.row][playerOnMove.col].isRoad == False):
                    print("NE ZNAM STO OVO SE DESILO")
                for i in range(len(newMap.tiles)):
                    row = ""
                    for j in range(len(newMap.tiles[i])):
                        if newMap.tiles[i][j].isRoad:
                            row += "r "
                        else:
                            row += "h "
                    print(row)
                # print("AI TILES:", aiTiles)
                # print("USER TILES:", userTiles)
                print("MAKE MOVE BEFORE", playerOnMove.row,
                      playerOnMove.col, "MOVE:", move)
                makeMove(newMap, move, playerOnMove)
                print("MAKE MOVE AFTER", playerOnMove.row,
                      playerOnMove.col, "MOVE:", move)
                print("")
                print("")
                print("")

                hypotheticalValue = minimax(newMap, not isMax, depth - 1)[0]
                if isMax == True and hypotheticalValue > bestValue:
                    bestValue = hypotheticalValue
                    bestMove = move
                if isMax == False and hypotheticalValue < bestValue:
                    bestValue = hypotheticalValue
                    bestMove = move
            return [bestValue, bestMove]

        return minimax(map, True, 4)
