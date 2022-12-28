from copy import deepcopy
import time
import random

# TODO: NAPRAVITI DA AKO JE PORAZ NEIZBEZAN VRACA SLEDECI KORAK U REDOSLEDU DEFINISANOM U PROJEKTU (GORE, GORE-DESNO, DESNO ...)


# TODO: MNOGO LOS KOD, MORA DA SE OPTIMIZUJE
# TODO: Za sad radi samo za 2 igraca, mora da se napravi i za vise igraca
def isGameOver(map):
    counter = 0

    for ag in map.agents:
        if len(availableMoves(map, ag)) == 0:
            counter += 1

    if counter >= len(map.agents) - 1:
        return True
    else:
        return False

# TODO: MNOGO LOS KOD, MORA DA SE OPTIMIZUJE


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
    print("SCORE", aiTiles - userTiles)
    return aiTiles - userTiles


def evaluateMapN(map, playerId):
    tiles = map.tiles
    playersCords = set()

    for ag in map.agents:
        playersCords.add((ag.row, ag.col))

    neighborDict = {}  # empty dictionary that we need to fill
    # key => (i, j) -> i - row, j - column
    # value => array of neighbors without tiles with holes
    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            neighbors = []

            if i-1 >= 0:
                if tiles[i-1][j].isRoad and (i-1, j) not in playersCords:
                    neighbors.append(tiles[i-1][j])
                if j-1 >= 0:
                    if tiles[i - 1][j - 1].isRoad and (i-1, j - 1) not in playersCords:
                        neighbors.append(tiles[i - 1][j - 1])
                if j + 1 < len(tiles[0]):
                    if tiles[i - 1][j + 1].isRoad and (i-1, j + 1) not in playersCords:
                        neighbors.append(tiles[i - 1][j + 1])

            if j - 1 >= 0:
                if tiles[i][j - 1].isRoad and (i, j - 1) not in playersCords:
                    neighbors.append(tiles[i][j - 1])
            if j + 1 < len(tiles[0]):
                if tiles[i][j + 1].isRoad and (i, j + 1) not in playersCords:
                    neighbors.append(tiles[i][j + 1])

            if i+1 < len(tiles):
                if tiles[i + 1][j].isRoad and (i+1, j) not in playersCords:
                    neighbors.append(tiles[i + 1][j])
                if j - 1 >= 0:
                    if tiles[i + 1][j - 1].isRoad and (i+1, j - 1) not in playersCords:
                        neighbors.append(tiles[i + 1][j - 1])
                if j + 1 < len(tiles[0]):
                    if tiles[i + 1][j + 1].isRoad and (i+1, j + 1) not in playersCords:
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
                if nbr not in visited and nbr not in playersCords:
                    count += 1
                    visited.append((neighbor.row, neighbor.col))
                    queue.append(neighbor)
        return count

    playerTiles = []
    for ag in map.agents:
        visited = []
        queue = []
        playerTiles.append(bfs(tiles[ag.row][ag.col]))

    score = playerTiles[playerId - 1] - \
        (sum(playerTiles) - playerTiles[playerId - 1]) / (len(playerTiles) - 1)

    # updatedPlayerTiles = deepcopy(playerTiles)
    # currentPlayerTiles = updatedPlayerTiles[playerId - 1]
    # del updatedPlayerTiles[playerId - 1]
    # score = currentPlayerTiles - max(updatedPlayerTiles)
    print("SCORE", score)
    return score


def availableMoves(map, player):
    # returns list of moves sorted like: North, NorthEast, East, SouthEast, South, SouthWest, West, NorthWest
    moves = []
    tiles = map.tiles

    if player.row - 1 >= 0:
        if tiles[player.row - 1][player.col].isRoad:
            agentOnTile = any(map.agents[i].row == player.row -
                              1 and map.agents[i].col == player.col for i in range(len(map.agents)))
            if not agentOnTile:
                moves.append((player.row - 1, player.col))

    if player.row - 1 >= 0 and player.col + 1 < len(tiles[0]):
        if tiles[player.row - 1][player.col + 1].isRoad:
            agentOnTile = any(map.agents[i].row == player.row - 1 and map.agents[i].col ==
                              player.col + 1 for i in range(len(map.agents)))
            if not agentOnTile:
                moves.append((player.row - 1, player.col + 1))

    if player.col + 1 < len(tiles[0]):
        if tiles[player.row][player.col + 1].isRoad:
            agentOnTile = any(map.agents[i].row == player.row and map.agents[i].col ==
                              player.col + 1 for i in range(len(map.agents)))
            if not agentOnTile:
                moves.append((player.row, player.col + 1))

    if player.row + 1 < len(tiles) and player.col + 1 < len(tiles[0]):
        if tiles[player.row + 1][player.col + 1].isRoad:
            agentOnTile = any(map.agents[i].row == player.row + 1 and map.agents[i].col ==
                              player.col + 1 for i in range(len(map.agents)))
            if not agentOnTile:
                moves.append((player.row + 1, player.col + 1))

    if player.row + 1 < len(tiles):
        if tiles[player.row + 1][player.col].isRoad:
            agentOnTile = any(map.agents[i].row == player.row +
                              1 and map.agents[i].col == player.col for i in range(len(map.agents)))
            if not agentOnTile:
                moves.append((player.row + 1, player.col))

    if player.row + 1 < len(tiles) and player.col - 1 >= 0:
        if tiles[player.row + 1][player.col - 1].isRoad:
            agentOnTile = any(map.agents[i].row == player.row + 1 and map.agents[i].col ==
                              player.col - 1 for i in range(len(map.agents)))
            if not agentOnTile:
                moves.append((player.row + 1, player.col - 1))

    if player.col - 1 >= 0:
        if tiles[player.row][player.col - 1].isRoad:
            agentOnTile = any(map.agents[i].row == player.row and map.agents[i].col ==
                              player.col - 1 for i in range(len(map.agents)))
            if not agentOnTile:
                moves.append((player.row, player.col - 1))

    if player.row - 1 >= 0 and player.col - 1 >= 0:
        if tiles[player.row - 1][player.col - 1].isRoad:
            agentOnTile = any(map.agents[i].row == player.row - 1 and map.agents[i].col ==
                              player.col - 1 for i in range(len(map.agents)))
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
        startTime = time.time()

        def minimax(map, isMax, depth):
            # Base case - the game is over, so we return the value of the board
            if isGameOver(map) or depth == 0 or time.time() - startTime >= map.timeToThink:
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

            for move in availableMoves(map, player):
                newMap = deepcopy(map)

                playerOnMove = None
                for agent in newMap.agents:
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

        return minimax(map, True, map.maxDepth)


class MinimaxABAgent(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentMove(self, map):
        startTime = time.time()

        def minimaxab(map, isMax, depth, alpha, beta):
            # Base case - the game is over, so we return the value of the board
            if isGameOver(map) or depth == 0 or time.time() - startTime >= map.timeToThink:
                return [evaluateMap(map), None, alpha, beta]
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

            for move in availableMoves(map, player):
                newMap = deepcopy(map)

                playerOnMove = None
                for agent in newMap.agents:
                    if isMax:
                        if agent.id == newMap.agentTurnId:
                            playerOnMove = agent
                            break
                    else:
                        if agent.id != newMap.agentTurnId:
                            playerOnMove = agent
                            break

                makeMove(newMap, move, playerOnMove)
                hypotheticalValue = minimaxab(
                    newMap, not isMax, depth - 1, alpha, beta)[0]
                if isMax == True and hypotheticalValue > bestValue:
                    bestValue = hypotheticalValue
                    bestMove = move
                    alpha = max(alpha, bestValue)
                if isMax == False and hypotheticalValue < bestValue:
                    bestValue = hypotheticalValue
                    bestMove = move
                    beta = min(beta, bestValue)
                if alpha > beta:
                    print("AAA")
                    break
            return [bestValue, bestMove, alpha, beta]

        data = minimaxab(map, True, map.maxDepth, -float("Inf"), float("Inf"))

        # -float("Inf") and float["inf"] can not be returned as json, so some conversion must be done
        if data[2] < -1000:
            data[2] = -1000
        if data[3] > 1000:
            data[3] = 1000

        return data


class ExpectimaxAgent(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentMove(self, map):
        startTime = time.time()

        def expectimax(map, isMax, depth):
            if isGameOver(map) or depth == 0 or time.time() - startTime >= map.timeToThink:
                return [evaluateMap(map), None]

            for agent in map.agents:
                if isMax:
                    if agent.id == map.agentTurnId:
                        player = agent
                        break
                else:
                    if agent.id != map.agentTurnId:
                        player = agent
                        break

            if isMax:
                bestScore = -float("Inf")
                bestMove = None
                for move in availableMoves(map, player):
                    newMap = deepcopy(map)

                    playerOnMove = None
                    for agent in newMap.agents:
                        if agent.id == newMap.agentTurnId:
                            playerOnMove = agent
                            break

                    makeMove(newMap, move, playerOnMove)
                    score = expectimax(newMap, False, depth - 1)[0]
                    if (score > bestScore):
                        bestScore = score
                        bestMove = move
                return [bestScore, bestMove]
            else:
                scores = []
                moves = []
                for move in availableMoves(map, player):
                    newMap = deepcopy(map)

                    playerOnMove = None
                    for agent in newMap.agents:
                        if agent.id != newMap.agentTurnId:
                            playerOnMove = agent
                            break

                    makeMove(newMap, move, playerOnMove)
                    result = expectimax(newMap, True, depth - 1)
                    scores.append(result[0])
                    moves.append(result[1])
                return [sum(scores) / len(scores), random.choice(moves)]

        return expectimax(map, True, map.maxDepth)


class MaxNAgent(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentMove(self, map):
        startTime = time.time()

        def maxn(map, depth, playerIndex):
            # Base case - the game is over, so we return the value of the board
            if isGameOver(map) or depth == 0 or time.time() - startTime >= map.timeToThink:
                return [[evaluateMapN(map, player.id) for player in map.agents], [None for player in map.agents]]
            bestMoves = [None] * len(map.agents)
            bestValues = [float("Inf") if playerIndex != map.agents[i].id else -float("Inf")
                          for i in range(len(map.agents))]

            # print("Best moves", bestMoves)
            # print("Best values", bestValues)

            # print("INDEX", playerIndex)
            player = next(
                player for player in map.agents if player.id == playerIndex)

            availMoves = availableMoves(map, player)
            # print("PLAYER", player.id, "AVAIL MOVES", availMoves)

            for move in availMoves:
                newMap = deepcopy(map)

                playerOnMove = None
                for agent in newMap.agents:
                    if agent.id == playerIndex:
                        playerOnMove = agent
                        break

                makeMove(newMap, move, playerOnMove)
                nextPlayerIndex = (playerIndex + 1) % (len(map.agents) + 1)
                if nextPlayerIndex == 0:
                    nextPlayerIndex = 1
                print("NEXT PLAYER", nextPlayerIndex)
                hypotheticalValues = maxn(
                    newMap, depth - 1, nextPlayerIndex)[0]
                print("HYPOTHETICAL VALUES", hypotheticalValues)
                # if any(val > bestValues[playerIndex - 1] if playerIndex - 1 == i else val < bestValues[i] for i, val in enumerate(hypotheticalValues)):
                for i in range(len(hypotheticalValues)):
                    val = hypotheticalValues[i]
                    # print("VAL", val, "BEST", bestValues[i], "I", i)
                    if (playerIndex - 1 == i and val > bestValues[playerIndex - 1]) or (playerIndex - 1 != i and val < bestValues[i]):
                        bestValues = hypotheticalValues
                        bestMoves[playerIndex - 1] = move
            return [bestValues, bestMoves]

        data = maxn(map, map.maxDepth, map.agentTurnId)
        value = data[0][map.agentTurnId - 1]
        move = data[1][map.agentTurnId - 1]

        # -float("Inf") and float["inf"] can not be returned as json, so some conversion must be done
        if value < -1000:
            value = -1000
        if value > 1000:
            value = 1000
        return [value, move]


class RandomAgent(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentMove(self, map):
        for agent in map.agents:
            if agent.id == map.agentTurnId:
                player = agent
                break

        moves = availableMoves(map, player)

        if len(moves) == 0:
            return [0, None]

        return [0, random.choice(moves)]
