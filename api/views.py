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

    for key, value in request.data.items():
        print(key, value)

    map = PyStolovinaMap(rawMap, agents, agentTurnId)

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
        if agentOnTurn.tag == 2:
            if len(agents) != 2:
                agentAlgorithmValid = False
            agent = MinimaxABAgent(agentOnTurn.row, agentOnTurn.col)
        if agentOnTurn.tag == 3:
            if len(agents) != 2:
                agentAlgorithmValid = False
            agent = ExpectimaxAgent(agentOnTurn.row, agentOnTurn.col)
        if agentOnTurn.tag == 4:
            agent = MaxNAgent(agentOnTurn.row, agentOnTurn.col)

    elif agentOnTurn.type == "teacher":
        if agentOnTurn.tag == 1:
            agent = ManhattanDistanceAgent(agentOnTurn.row, agentOnTurn.col)
        if agentOnTurn.tag == 2:
            agent = RandomAgent(agentOnTurn.row, agentOnTurn.col)
        if agentOnTurn.tag == 3:
            if len(agents) != 2:
                agentAlgorithmValid = False
            agent = MinimaxABAgent(agentOnTurn.row, agentOnTurn.col)
        if agentOnTurn.tag == 4:
            agent = MaxNAgent(agentOnTurn.row, agentOnTurn.col)

    if not agentAlgorithmValid:
        return Response({"error": "Invalid agent algorithm"}, status=status.HTTP_400_BAD_REQUEST)

    move = agent.getAgentMove(map)

    return Response(move)
