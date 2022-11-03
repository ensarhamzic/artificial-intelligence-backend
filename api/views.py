from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.classes.agents import *
from api.classes.map import Map


@api_view(['Post'])
def getPath(request):
    map = Map(request.data["map"], request.data["agentPosition"],
              request.data["finishPosition"])
    agent = request.data["agent"]

    if agent == 1:
        agent = Aki(map.agentPosition.row, map.agentPosition.col)
    elif agent == 2:
        agent = Jocke(map.agentPosition.row, map.agentPosition.col)

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
