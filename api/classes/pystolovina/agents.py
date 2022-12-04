from copy import deepcopy

# TODO: Implementirati tajmer u algoritmima
# TODO: Implementirati dinamicku max dubinu dobijenu od klinta


# TODO: MNOGO LOS KOD, MORA DA SE OPTIMIZUJE
# TODO: Za sad radi samo za 2 igraca, mora da se napravi i za vise igraca
def isGameOver(map):
    for ag in map.agents:
        if ag.id != map.agentTurnId:
            userRow = ag.row
            userCol = ag.col
        else:
            aiRow = ag.row
            aiCol = ag.col

    userGameOver = True
    aiGameOver = True

    if(userRow - 1 >= 0):
        if map.tiles[userRow - 1][userCol].isRoad and (userRow - 1 != aiRow or userCol != aiCol):
            userGameOver = False
        if(userCol - 1 >= 0):
            if (map.tiles[userRow - 1][userCol - 1].isRoad and (userRow - 1 != aiRow or userCol - 1 != aiCol)):
                userGameOver = False
        if(userCol + 1 < len(map.tiles[0])):
            if map.tiles[userRow - 1][userCol + 1].isRoad and (userRow - 1 != aiRow or userCol + 1 != aiCol):
                userGameOver = False

    if userCol - 1 >= 0:
        if map.tiles[userRow][userCol - 1].isRoad and (userRow != aiRow or userCol - 1 != aiCol):
            userGameOver = False
    if userCol + 1 < len(map.tiles[0]):
        if map.tiles[userRow][userCol + 1].isRoad and (userRow != aiRow or userCol + 1 != aiCol):
            userGameOver = False

    if(userRow + 1 < len(map.tiles)):
        if map.tiles[userRow + 1][userCol].isRoad and (userRow + 1 != aiRow or userCol != aiCol):
            userGameOver = False
        if(userCol - 1 >= 0):
            if map.tiles[userRow + 1][userCol - 1].isRoad and (userRow + 1 != aiRow or userCol - 1 != aiCol):
                userGameOver = False
        if(userCol + 1 < len(map.tiles[0])):
            if map.tiles[userRow + 1][userCol + 1].isRoad and (userRow + 1 != aiRow or userCol + 1 != aiCol):
                userGameOver = False

    if(aiRow - 1 >= 0):
        if map.tiles[aiRow - 1][aiCol].isRoad and (aiRow - 1 != userRow or aiCol != userCol):
            aiGameOver = False
        if(aiCol - 1 >= 0):
            if (map.tiles[aiRow - 1][aiCol - 1].isRoad and (aiRow - 1 != userRow or aiCol - 1 != userCol)):
                aiGameOver = False
        if(aiCol + 1 < len(map.tiles[0])):
            if map.tiles[aiRow - 1][aiCol + 1].isRoad and (aiRow - 1 != userRow or aiCol + 1 != userCol):
                aiGameOver = False

    if aiCol - 1 >= 0:
        if map.tiles[aiRow][aiCol - 1].isRoad and (aiRow != userRow or aiCol - 1 != userCol):
            aiGameOver = False

    if aiCol + 1 < len(map.tiles[0]):
        if map.tiles[aiRow][aiCol + 1].isRoad and (aiRow != userRow or aiCol + 1 != userCol):
            aiGameOver = False

    if(aiRow + 1 < len(map.tiles)):
        if map.tiles[aiRow + 1][aiCol].isRoad and (aiRow + 1 != userRow or aiCol != userCol):
            aiGameOver = False
        if(aiCol - 1 >= 0):
            if map.tiles[aiRow + 1][aiCol - 1].isRoad and (aiRow + 1 != userRow or aiCol - 1 != userCol):
                aiGameOver = False
        if(aiCol + 1 < len(map.tiles[0])):
            if map.tiles[aiRow + 1][aiCol + 1].isRoad and (aiRow + 1 != userRow or aiCol + 1 != userCol):
                aiGameOver = False

    return userGameOver or aiGameOver

# TODO: Radi samo za 2 igraca, mora da se napravi i za vise igraca


def evaluateMap(map):
    for ag in map.agents:
        if ag.id != map.agentTurnId:
            userPosition = ag
        else:
            aiPosition = ag

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

    return aiTiles - userTiles

# TODO: Radi samo za 2 igraca, mora da se napravi i za vise igraca
# TODO: Mora da se optimizuje


def availableMoves(map, player):
    # returns list of moves sorted like: North, NorthEast, East, SouthEast, South, SouthWest, West, NorthWest
    moves = []
    tiles = map.tiles

    for ag in map.agents:
        if ag.id != map.agentTurnId:
            userPosition = ag
        else:
            aiPosition = ag

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
    map.tiles[player.row][player.col].isRoad = False
    player.row = move[0]
    player.col = move[1]


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

            # Base case - the game is over, so we return the value of the board
            if isGameOver(map) or depth == 0:
                return [evaluateMap(map), None]
            bestMove = None
            if isMax == True:
                bestValue = -float("Inf")
            else:
                bestValue = float("Inf")

            player = None
            for agent in map.agents:
                if isMax:
                    if agent.id == map.agentTurnId:
                        player = agent
                        break
                else:
                    if agent.id != map.agentTurnId:
                        player = agent
                        break
            print("PLAYER", (player.row, player.col))

            for move in availableMoves(map, player):
                newMap = deepcopy(map)

                playerOnMove = None
                for agent in newMap.agents:  # TODO: Moze mozda da se optimizuje, jer uvek ima samo 2 igraca jer je minimax
                    if isMax:
                        if agent.id == newMap.agentTurnId:
                            playerOnMove = agent
                            break
                    else:
                        if agent.id != newMap.agentTurnId:
                            playerOnMove = agent
                            break

                makeMove(newMap, move, playerOnMove)
                hypotheticalValue = minimax(newMap, not isMax, depth - 1)[0]
                if isMax == True and hypotheticalValue > bestValue:
                    bestValue = hypotheticalValue
                    bestMove = move
                if isMax == False and hypotheticalValue < bestValue:
                    bestValue = hypotheticalValue
                    bestMove = move
            return [bestValue, bestMove]

        return minimax(map, True, 5)
