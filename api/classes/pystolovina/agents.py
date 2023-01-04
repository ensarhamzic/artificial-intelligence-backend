from copy import deepcopy
import time
import random

# these two below are used if the agent on turn is defeated on all of the leaves
# specific project description says that in that case the agents next move should be first move clockwise, starting from the top
numberOfLeaves = 0  # number of leaves in the tree
agentOnTurnLostTimes = 0  # number of times when agent on turn lost on the leaf


def isGameOver(map):
    counter = 0

    for ag in map.agents:
        if len(availableMoves(map, ag)) == 0:
            counter += 1

    if counter >= len(map.agents) - 1:
        return True
    else:
        return False


def bfs(node, neighborDict, visited, queue, playersCords):
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
                visited.append(nbr)
                queue.append(neighbor)
    return count

def evaluateMap(map):
    for ag in map.agents:
        if ag.id != map.agentTurnId:
            userPosition = ag
        else:
            aiPosition = ag

    tiles = map.tiles

    playersCords = [(userPosition.row, userPosition.col), (aiPosition.row, aiPosition.col)]

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
    userTiles = bfs(tiles[userPosition.row][userPosition.col], neighborDict, visited, queue, playersCords)
    visited = []
    queue = []
    aiTiles = bfs(tiles[aiPosition.row][aiPosition.col], neighborDict, visited, queue, playersCords)
    return aiTiles - userTiles


def evaluateMapN(map, playerId):

    tiles = map.tiles
    playersCords = []

    for ag in map.agents:
        playersCords.append((ag.row, ag.col))

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

    playerTiles = []
    for ag in map.agents:
        visited = []
        queue = []
        currentAgentScore = bfs(tiles[ag.row][ag.col], neighborDict, visited, queue, playersCords)
        playerTiles.append(currentAgentScore)

    score = playerTiles[playerId - 1] - \
        (sum(playerTiles) - playerTiles[playerId - 1]) / (len(playerTiles) - 1)

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

    def minimax(self, map, isMax, depth, startTime):
        global numberOfLeaves
        global agentOnTurnLostTimes
        # Base case - the game is over, so we return the value of the board
        if isGameOver(map) or depth == 0 or time.time() - startTime >= map.timeToThink:
            numberOfLeaves += 1
            if(len(availableMoves(map, next(agent for agent in map.agents if agent.id == map.agentTurnId))) == 0):
                agentOnTurnLostTimes += 1
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
            hypotheticalValue = self.minimax(
                newMap, not isMax, depth - 1, startTime)[0]
            if isMax == True and hypotheticalValue > bestValue:
                bestValue = hypotheticalValue
                bestMove = move
            if isMax == False and hypotheticalValue < bestValue:
                bestValue = hypotheticalValue
                bestMove = move
        return [bestValue, bestMove]

    def getAgentMove(self, map):
        global numberOfLeaves
        global agentOnTurnLostTimes
        numberOfLeaves = 0
        agentOnTurnLostTimes = 0
        startTime = time.time()

        data = self.minimax(map, True, map.maxDepth, startTime)
        if numberOfLeaves == agentOnTurnLostTimes:
            data[0] = -999
            avMvs = availableMoves(
                map, next(agent for agent in map.agents if agent.id == map.agentTurnId))
            if(len(avMvs) > 0):
                data[1] = avMvs[0]

        return data


class MinimaxABAgent(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def minimaxab(self, map, isMax, depth, alpha, beta, startTime):
        global numberOfLeaves
        global agentOnTurnLostTimes
        # Base case - the game is over, so we return the value of the board
        if isGameOver(map) or depth == 0 or time.time() - startTime >= map.timeToThink:
            numberOfLeaves += 1
            if(len(availableMoves(map, next(agent for agent in map.agents if agent.id == map.agentTurnId))) == 0):
                agentOnTurnLostTimes += 1
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
            hypotheticalValue = self.minimaxab(
                newMap, not isMax, depth - 1, alpha, beta, startTime)[0]
            if isMax == True and hypotheticalValue > bestValue:
                bestValue = hypotheticalValue
                bestMove = move
                alpha = max(alpha, bestValue)
            if isMax == False and hypotheticalValue < bestValue:
                bestValue = hypotheticalValue
                bestMove = move
                beta = min(beta, bestValue)
            if alpha > beta:
                break
        return [bestValue, bestMove, alpha, beta]

    def getAgentMove(self, map):
        global numberOfLeaves
        global agentOnTurnLostTimes
        numberOfLeaves = 0
        agentOnTurnLostTimes = 0
        startTime = time.time()

        data = self.minimaxab(map, True, map.maxDepth, -
                              float("Inf"), float("Inf"), startTime)

        # -float("Inf") and float["inf"] can not be returned as json, so some conversion must be done
        if data[2] < -1000:
            data[2] = -1000
        if data[3] > 1000:
            data[3] = 1000

        if numberOfLeaves == agentOnTurnLostTimes:
            data[0] = -999
            avMvs = availableMoves(
                map, next(agent for agent in map.agents if agent.id == map.agentTurnId))
            if(len(avMvs) > 0):
                data[1] = avMvs[0]
        return data


class ExpectimaxAgent(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def expectimax(self, map, isMax, depth, startTime):
        global numberOfLeaves
        global agentOnTurnLostTimes
        if isGameOver(map) or depth == 0 or time.time() - startTime >= map.timeToThink:
            numberOfLeaves += 1
            if(len(availableMoves(map, next(agent for agent in map.agents if agent.id == map.agentTurnId))) == 0):
                agentOnTurnLostTimes += 1
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
                score = self.expectimax(newMap, False, depth - 1, startTime)[0]
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
                result = self.expectimax(newMap, True, depth - 1, startTime)
                scores.append(result[0])
                moves.append(result[1])
            return [sum(scores) / len(scores), random.choice(moves)]

    def getAgentMove(self, map):
        global numberOfLeaves
        global agentOnTurnLostTimes
        numberOfLeaves = 0
        agentOnTurnLostTimes = 0
        startTime = time.time()

        data = self.expectimax(map, True, map.maxDepth, startTime)
        if numberOfLeaves == agentOnTurnLostTimes:
            data[0] = -999
            avMvs = availableMoves(
                map, next(agent for agent in map.agents if agent.id == map.agentTurnId))
            if(len(avMvs) > 0):
                data[1] = avMvs[0]

        return data


class MaxNAgent(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def maxn(self, map, depth, playerIndex, startTime):
        global numberOfLeaves
        global agentOnTurnLostTimes
        print(time.time() - startTime)
        if isGameOver(map) or depth == 0 or time.time() - startTime >= map.timeToThink:
            numberOfLeaves += 1
            if(len(availableMoves(map, next(agent for agent in map.agents if agent.id == map.agentTurnId))) == 0):
                agentOnTurnLostTimes += 1
            return [evaluateMapN(map, map.agentTurnId), None]

        bestMove = None
        bestValue = - \
            float("inf") if playerIndex == map.agentTurnId else float("inf")

        player = next(
            player for player in map.agents if player.id == playerIndex)

        availMoves = availableMoves(map, player)

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

            savedNextPlayerIndex = nextPlayerIndex
            playersWithoutMoves = 0
            while True:
                mvs = availableMoves(newMap, next(
                    player for player in newMap.agents if player.id == nextPlayerIndex))

                if len(mvs) > 0:

                    break

                playersWithoutMoves += 1
                if playersWithoutMoves == len(newMap.agents):
                    nextPlayerIndex = savedNextPlayerIndex
                    break

                nextPlayerIndex = (nextPlayerIndex +
                                   1) % (len(map.agents) + 1)
                if nextPlayerIndex == 0:
                    nextPlayerIndex = 1

            maxnData = self.maxn(
                newMap, depth - 1, nextPlayerIndex, startTime)
            hypotheticalValue = maxnData[0]

            if playerIndex == map.agentTurnId and hypotheticalValue > bestValue:
                bestValue = hypotheticalValue
                bestMove = move

            if playerIndex != map.agentTurnId and hypotheticalValue < bestValue:
                bestValue = hypotheticalValue
                bestMove = move

        return [bestValue, bestMove]

    def maxnAB(self, map, depth, playerIndex, alpha, beta, startTime):
        global numberOfLeaves
        global agentOnTurnLostTimes
        print(time.time() - startTime)
        if isGameOver(map) or depth == 0 or time.time() - startTime >= map.timeToThink:
            numberOfLeaves += 1
            if(len(availableMoves(map, next(agent for agent in map.agents if agent.id == map.agentTurnId))) == 0):
                agentOnTurnLostTimes += 1
            return [evaluateMapN(map, map.agentTurnId), None]

        bestMove = None
        bestValue = - \
            float("inf") if playerIndex == map.agentTurnId else float("inf")

        player = next(
            player for player in map.agents if player.id == playerIndex)
        availMoves = availableMoves(map, player)

        for move in availMoves:
            newMap = deepcopy(map)
            playerOnMove = next(
                agent for agent in newMap.agents if agent.id == playerIndex)
            makeMove(newMap, move, playerOnMove)

            nextPlayerIndex = (playerIndex + 1) % (len(map.agents) + 1)
            if nextPlayerIndex == 0:
                nextPlayerIndex = 1

            savedNextPlayerIndex = nextPlayerIndex
            playersWithoutMoves = 0
            while True:
                mvs = availableMoves(newMap, next(
                    player for player in newMap.agents if player.id == nextPlayerIndex))
                if len(mvs) > 0:
                    break
                playersWithoutMoves += 1
                if playersWithoutMoves == len(newMap.agents):
                    nextPlayerIndex = savedNextPlayerIndex
                    break
                nextPlayerIndex = (nextPlayerIndex +
                                   1) % (len(map.agents) + 1)
                if nextPlayerIndex == 0:
                    nextPlayerIndex = 1

            maxnData = self.maxnAB(newMap, depth - 1,
                                   nextPlayerIndex, alpha, beta, startTime)
            hypotheticalValue = maxnData[0]

            if playerIndex == map.agentTurnId:
                if hypotheticalValue > bestValue:
                    bestValue = hypotheticalValue
                    bestMove = move
                if hypotheticalValue >= beta:
                    return [bestValue, bestMove]
                alpha = max(alpha, bestValue)
            else:
                if hypotheticalValue < bestValue:
                    bestValue = hypotheticalValue
                    bestMove = move
                if hypotheticalValue <= alpha:
                    return [bestValue, bestMove]
                beta = min(beta, bestValue)

        return [bestValue, bestMove]

    def getAgentMove(self, map):
        global numberOfLeaves
        global agentOnTurnLostTimes
        numberOfLeaves = 0
        agentOnTurnLostTimes = 0
        startTime = time.time()

        data = self.maxnAB(map, map.maxDepth, map.agentTurnId, -
                           float("inf"), float("inf"), startTime)
        # data = self.maxn(map, map.maxDepth, map.agentTurnId, startTime)

        # -float("Inf") and float["inf"] can not be returned as json, so some conversion must be done
        if data[0] < -1000:
            data[0] = -1000
        if data[0] > 1000:
            data[0] = 1000

        if numberOfLeaves == agentOnTurnLostTimes:
            data[0] = -999
            avMvs = availableMoves(
                map, next(agent for agent in map.agents if agent.id == map.agentTurnId))
            if(len(avMvs) > 0):
                data[1] = avMvs[0]
        return data


class RandomAgent(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def getAgentMove(self, map):
        if isGameOver(map):
            return [0, None]
        for agent in map.agents:
            if agent.id == map.agentTurnId:
                player = agent
                break

        moves = availableMoves(map, player)

        if len(moves) == 0:
            return [0, None]

        return [0, random.choice(moves)]


class ManhattanDistanceAgent(Agent):
    def __init__(self, row, col):
        super().__init__(row, col)

    def manhattanDistance(self, player1, player2):
        distance = 0
        distance += abs(player1.row - player2.row)
        distance += abs(player1.col - player2.col)
        return distance

    def getAgentMove(self, map):
        if isGameOver(map):
            return [0, None]

        goalAgent = None
        studentAgent = next(
            (agent for agent in map.agents if agent.type == "student"), None)
        if studentAgent is not None and len(availableMoves(map, studentAgent)) != 0:
            goalAgent = studentAgent
        else:
            goalAgents = []
            for agent in map.agents:
                if agent.id != map.agentTurnId and len(availableMoves(map, agent)) != 0:
                    goalAgents.append(agent)

            goalAgent = random.choice(goalAgents)

        for agent in map.agents:
            if agent.id == map.agentTurnId:
                player = agent
                break

        moves = availableMoves(map, player)

        if len(moves) == 0:
            return [0, None]

        bestMove = moves[0]
        bestDistance = float("inf")
        for move in moves:
            newMap = deepcopy(map)
            playerOnMove = next(
                agent for agent in newMap.agents if agent.id == newMap.agentTurnId)
            makeMove(newMap, move, playerOnMove)

            distance = self.manhattanDistance(playerOnMove, goalAgent)

            if distance < bestDistance:
                bestDistance = distance
                bestMove = move

        return [0, bestMove]
