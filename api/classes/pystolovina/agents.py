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

    # for every agent in map.agents, check if there is a road tile in the 8 tiles around it and if any agent is on that tile
    # counter = 0
    # for ag in map.agents:
    #     if ag.row - 1 >= 0:
    #         if map.tiles[ag.row - 1][ag.col].isRoad and not any(
    #                 agent.row == ag.row - 1 and agent.col == ag.col for agent in map.agents):
    #             counter += 1
    #         if ag.col - 1 >= 0:
    #             if map.tiles[ag.row - 1][ag.col - 1].isRoad and not any(
    #                     agent.row == ag.row - 1 and agent.col == ag.col - 1 for agent in map.agents):
    #                 counter += 1
    #         if ag.col + 1 < len(map.tiles[0]):
    #             if map.tiles[ag.row - 1][ag.col + 1].isRoad and not any(
    #                     agent.row == ag.row - 1 and agent.col == ag.col + 1 for agent in map.agents):
    #                 counter += 1

    #     if ag.col - 1 >= 0:
    #         if map.tiles[ag.row][ag.col - 1].isRoad and not any(
    #                 agent.row == ag.row and agent.col == ag.col - 1 for agent in map.agents):
    #             counter += 1
    #     if ag.col + 1 < len(map.tiles[0]):
    #         if map.tiles[ag.row][ag.col + 1].isRoad and not any(
    #                 agent.row == ag.row and agent.col == ag.col + 1 for agent in map.agents):
    #             counter += 1

    #     if ag.row + 1 < len(map.tiles):
    #         if map.tiles[ag.row + 1][ag.col].isRoad and not any(
    #                 agent.row == ag.row + 1 and agent.col == ag.col for agent in map.agents):
    #             counter += 1
    #         if ag.col - 1 >= 0:
    #             if map.tiles[ag.row + 1][ag.col - 1].isRoad and not any(
    #                     agent.row == ag.row + 1 and agent.col == ag.col - 1 for agent in map.agents):
    #                 counter += 1
    #         if ag.col + 1 < len(map.tiles[0]):
    #             if map.tiles[ag.row + 1][ag.col + 1].isRoad and not any(
    #                     agent.row == ag.row + 1 and agent.col == ag.col + 1 for agent in map.agents):
    #                 counter += 1

    # if counter == 0:
    #     return True
    # else:
    #     return False

    # for ag in map.agents:
    #     if ag.id != map.agentTurnId:
    #         userRow = ag.row
    #         userCol = ag.col
    #     else:
    #         aiRow = ag.row
    #         aiCol = ag.col

    # userGameOver = True
    # aiGameOver = True

    # if (userRow - 1 >= 0):
    #     if map.tiles[userRow - 1][userCol].isRoad and (userRow - 1 != aiRow or userCol != aiCol):
    #         userGameOver = False
    #     if (userCol - 1 >= 0):
    #         if (map.tiles[userRow - 1][userCol - 1].isRoad and (userRow - 1 != aiRow or userCol - 1 != aiCol)):
    #             userGameOver = False
    #     if (userCol + 1 < len(map.tiles[0])):
    #         if map.tiles[userRow - 1][userCol + 1].isRoad and (userRow - 1 != aiRow or userCol + 1 != aiCol):
    #             userGameOver = False

    # if userCol - 1 >= 0:
    #     if map.tiles[userRow][userCol - 1].isRoad and (userRow != aiRow or userCol - 1 != aiCol):
    #         userGameOver = False
    # if userCol + 1 < len(map.tiles[0]):
    #     if map.tiles[userRow][userCol + 1].isRoad and (userRow != aiRow or userCol + 1 != aiCol):
    #         userGameOver = False

    # if (userRow + 1 < len(map.tiles)):
    #     if map.tiles[userRow + 1][userCol].isRoad and (userRow + 1 != aiRow or userCol != aiCol):
    #         userGameOver = False
    #     if (userCol - 1 >= 0):
    #         if map.tiles[userRow + 1][userCol - 1].isRoad and (userRow + 1 != aiRow or userCol - 1 != aiCol):
    #             userGameOver = False
    #     if (userCol + 1 < len(map.tiles[0])):
    #         if map.tiles[userRow + 1][userCol + 1].isRoad and (userRow + 1 != aiRow or userCol + 1 != aiCol):
    #             userGameOver = False

    # if (aiRow - 1 >= 0):
    #     if map.tiles[aiRow - 1][aiCol].isRoad and (aiRow - 1 != userRow or aiCol != userCol):
    #         aiGameOver = False
    #     if (aiCol - 1 >= 0):
    #         if (map.tiles[aiRow - 1][aiCol - 1].isRoad and (aiRow - 1 != userRow or aiCol - 1 != userCol)):
    #             aiGameOver = False
    #     if (aiCol + 1 < len(map.tiles[0])):
    #         if map.tiles[aiRow - 1][aiCol + 1].isRoad and (aiRow - 1 != userRow or aiCol + 1 != userCol):
    #             aiGameOver = False

    # if aiCol - 1 >= 0:
    #     if map.tiles[aiRow][aiCol - 1].isRoad and (aiRow != userRow or aiCol - 1 != userCol):
    #         aiGameOver = False

    # if aiCol + 1 < len(map.tiles[0]):
    #     if map.tiles[aiRow][aiCol + 1].isRoad and (aiRow != userRow or aiCol + 1 != userCol):
    #         aiGameOver = False

    # if (aiRow + 1 < len(map.tiles)):
    #     if map.tiles[aiRow + 1][aiCol].isRoad and (aiRow + 1 != userRow or aiCol != userCol):
    #         aiGameOver = False
    #     if (aiCol - 1 >= 0):
    #         if map.tiles[aiRow + 1][aiCol - 1].isRoad and (aiRow + 1 != userRow or aiCol - 1 != userCol):
    #             aiGameOver = False
    #     if (aiCol + 1 < len(map.tiles[0])):
    #         if map.tiles[aiRow + 1][aiCol + 1].isRoad and (aiRow + 1 != userRow or aiCol + 1 != userCol):
    #             aiGameOver = False

    # return userGameOver or aiGameOver

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
    print(aiTiles - userTiles)
    return aiTiles - userTiles

# TODO: POKUSAJ BOLJE EVALUACIONE FUNKCIJE, KOJA UZIMA NAJDUZU PUTANJU KOJOM AI MOZE DA SE KRECE, I NAJDUZU PUTANJU KOJOM USER MOZE DA SE KRECE, I ONDA IZRAZAVA RAZLIKU U BROJU POLJA KOJA SU NA TAKVIM PUTANJAMA
# def evaluateMap(map):
#     for ag in map.agents:
#         if ag.id != map.agentTurnId:
#             userPosition = ag
#         else:
#             aiPosition = ag

#     tiles = map.tiles

#     userCords = (userPosition.row, userPosition.col)
#     aiCords = (aiPosition.row, aiPosition.col)

#     neighborDict = {}  # empty dictionary that we need to fill
#     # key => (i, j) -> i - row, j - column
#     # value => array of neighbors without tiles with holes
#     for i in range(len(tiles)):
#         for j in range(len(tiles[i])):
#             neighbors = []

#             if i-1 >= 0:
#                 if tiles[i-1][j].isRoad and (i-1, j) != userCords and (i-1, j) != aiCords:
#                     neighbors.append(tiles[i-1][j])
#                 if j-1 >= 0:
#                     if tiles[i - 1][j - 1].isRoad and (i-1, j - 1) != userCords and (i-1, j - 1) != aiCords:
#                         neighbors.append(tiles[i - 1][j - 1])
#                 if j + 1 < len(tiles[0]):
#                     if tiles[i - 1][j + 1].isRoad and (i-1, j + 1) != userCords and (i-1, j + 1) != aiCords:
#                         neighbors.append(tiles[i - 1][j + 1])

#             if j - 1 >= 0:
#                 if tiles[i][j - 1].isRoad and (i, j - 1) != userCords and (i, j - 1) != aiCords:
#                     neighbors.append(tiles[i][j - 1])
#             if j + 1 < len(tiles[0]):
#                 if tiles[i][j + 1].isRoad and (i, j + 1) != userCords and (i, j + 1) != aiCords:
#                     neighbors.append(tiles[i][j + 1])

#             if i+1 < len(tiles):
#                 if tiles[i + 1][j].isRoad and (i+1, j) != userCords and (i+1, j) != aiCords:
#                     neighbors.append(tiles[i + 1][j])
#                 if j - 1 >= 0:
#                     if tiles[i + 1][j - 1].isRoad and (i+1, j - 1) != userCords and (i+1, j - 1) != aiCords:
#                         neighbors.append(tiles[i + 1][j - 1])
#                 if j + 1 < len(tiles[0]):
#                     if tiles[i + 1][j + 1].isRoad and (i+1, j + 1) != userCords and (i+1, j + 1) != aiCords:
#                         neighbors.append(tiles[i + 1][j + 1])

#             neighborDict[(i, j)] = neighbors

    # Create a list to keep track of the longest path found so far
    # longest_path = []

    # # Define a recursive function to explore each node and its neighbors
    # def explore(node, path, visited):
    #     global longest_path
    #     nodePosition = (node.row, node.col)
    #     # Add the current node to the path
    #     path.append(node)

    #     # Mark the current node as visited
    #     visited.add(nodePosition)

    #     # If the current node is a leaf node, update the longest path
    #     if len(neighborDict[nodePosition]) == 0:
    #         if len(path) > len(longest_path):
    #             longest_path = path

    #     # Otherwise, explore each of the node's unvisited neighbors
    #     else:
    #         for neighbor in neighborDict[nodePosition]:
    #             if neighbor not in visited:
    #                 explore(neighbor, path, visited)

    #     # Remove the current node from the path and mark it as unvisited
    #     path.pop()
    #     visited.remove(nodePosition)

    # def explore(node, path, visited):
    #     longestPath = []
    #     stack = []
    #     stack.append((node, path, visited))

    #     while stack:
    #         node, path, visited = stack.pop()
    #         nodePosition = (node.row, node.col)

    #         # Add the current node to the path
    #         path.append(node)

    #         # Mark the current node as visited
    #         visited.add(nodePosition)

    #         # If the current node is a leaf node, update tshe longest path
    #         if len(neighborDict[nodePosition]) == 0:
    #             if len(path) > len(longestPath):
    #                 longestPath = path

    #         # Otherwise, explore each of the node's unvisited neighbors
    #         else:
    #             for neighbor in neighborDict[nodePosition]:
    #                 if (neighbor.row, neighbor.col) not in visited:
    #                     print(node.row, node.col)
    #                     stack.append((neighbor, path, visited.copy()))

    #         # Remove the current node from the path and mark it as unvisited
    #         path.pop()
    #         # visited.remove(nodePosition)

    #     return longestPath

    # # Start the depth-first search at the source node
    # aiLongestPath = len(
    #     explore(tiles[aiPosition.row][aiPosition.col], [], set()))

    # userLongestPath = len(explore(
    #     tiles[userPosition.row][userPosition.col], [], set()))

    # return aiLongestPath - userLongestPath


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
    # print("___________________________")
    # for agent in map.agents:
    #     if agent.id != player.id:
    #         print("Player " + str(agent.id) + " is at " +
    #               str(agent.row) + " " + str(agent.col))
    # print("Player " + str(player.id) + " moved from " +
    #       str(player.row) + " " + str(player.col))

    # -------------------------------------------------

    map.tiles[player.row][player.col].isRoad = False
    player.row = move[0]
    player.col = move[1]

    # -------------------------------------------------

    # print("Player " + str(player.id) + " moved to " +
    #       str(player.row) + " " + str(player.col))
    # for row in map.tiles:
    #     for tile in row:
    #         if tile.isRoad:
    #             print("1", end=" ")
    #         else:
    #             print("0", end=" ")
    #     print("")
    # print("___________________________")


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
                return [[evaluateMap(map) for player in map.agents], [None for player in map.agents]]
            bestMoves = [None] * len(map.agents)
            bestValues = [float("Inf") if playerIndex != map.agents[i].id else -float("Inf")
                          for i in range(len(map.agents))]

            print("Best values", bestValues)

            print("INDEX", playerIndex)
            player = next(
                player for player in map.agents if player.id == playerIndex)

            for move in availableMoves(map, player):
                newMap = deepcopy(map)
                makeMove(newMap, move, player)
                nextPlayerIndex = (playerIndex + 1) % (len(map.agents) + 1)
                if nextPlayerIndex == 0:
                    nextPlayerIndex = 1
                hypotheticalValues = maxn(
                    newMap, depth - 1, nextPlayerIndex)[0]
                # if any(val > bestValues[playerIndex - 1] if playerIndex - 1 == i else val < bestValues[i] for i, val in enumerate(hypotheticalValues)):
                for i in range(len(hypotheticalValues)):
                    val = hypotheticalValues[i]
                    print("VAL", val, "BEST", bestValues[i], "I", i)
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
