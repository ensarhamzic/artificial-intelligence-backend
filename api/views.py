from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.classes.agents import Aki
from api.classes.map import Map


@api_view(['Post'])
def getPath(request):
    map = Map(request.data["map"], request.data["agentPosition"],
              request.data["finishPosition"])
    agent = request.data["agent"]

    if agent == 1:
        aki = Aki(map.agentPosition.row, map.agentPosition.col)
        path = aki.getAgentPath(map)

    # for i in range(len(map.tiles)):
    #     for j in range(len(map.tiles[i])):
    #         print(map.tiles[i][j].cost)

    #     print()
    #     print()

    return Response("c")
