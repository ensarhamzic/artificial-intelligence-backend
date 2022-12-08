from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.classes.pytanja.agents import *
from api.classes.pytanja.map import Map as PytanjaMap
from api.classes.pystolovina.agents import *
from api.classes.pystolovina.map import Map as PyStolovinaMap


@api_view(['Post'])
def getPath(request):
    map = PytanjaMap(request.data["map"], request.data["agentPosition"],
                     request.data["finishPosition"])
    agent = request.data["agent"]

    if agent == 1:
        agent = Aki(map.agentPosition.row, map.agentPosition.col)
    elif agent == 2:
        agent = Jocke(map.agentPosition.row, map.agentPosition.col)
    elif agent == 3:
        agent = Draza(map.agentPosition.row, map.agentPosition.col)
    elif agent == 4:
        agent = Bole(map.agentPosition.row, map.agentPosition.col)

    path = agent.getAgentPath(map)

    tiles = []
    price = 0
    for tile in path:
        tiles.append({
            "row": tile.row,
            "col": tile.col,
            "cost": tile.cost
        })
        price += tile.cost

    data = {
        "tiles": tiles,
        "price": price
    }

    return Response(data)


@api_view(['Post'])
def getMove(request):
    rawMap = request.data["map"]
    agents = request.data["agents"]
    agentTurnId = request.data["agentTurnId"]
    maxDepth = request.data["maxDepth"]
    timeToThink = request.data["timeToThink"]

    map = PyStolovinaMap(
        rawMap, agents, agentTurnId, maxDepth, timeToThink)

    agentOnTurn = None

    # if agent algorithm is not valid,
    # algorithm can't be run (for example, if there are more than 2 agents
    # and algorithm is minimax, it can't be done because minimax is just for 2 players)
    agentAlgorithmValid = True
    for ag in map.agents:
        if ag.id == agentTurnId:
            agentOnTurn = ag
            break

    if agentOnTurn.type == "student":
        if agentOnTurn.tag == 1:
            if len(agents) != 2:
                agentAlgorithmValid = False
            agent = MinimaxAgent(agentOnTurn.row, agentOnTurn.col)
    # TODO: add other agents

    if not agentAlgorithmValid:
        return Response({"error": "Invalid agent algorithm"}, status=status.HTTP_400_BAD_REQUEST)

    move = agent.getAgentMove(map)
    print(move)
    return Response(move)
