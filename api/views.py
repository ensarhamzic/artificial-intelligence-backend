from rest_framework.response import Response
from rest_framework.decorators import api_view
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
    print(request.data)
    map = PyStolovinaMap(request.data["map"], request.data["userPosition"],
                         request.data["aiPosition"])

    agent = MinimaxAgent(map.aiPosition.row, map.aiPosition.col)
    move = agent.getAgentMove(map)

    return Response(move)
