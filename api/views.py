from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['Post'])
def getPath(request):
    person = {'name': 'Ensar', 'age': 21}
    return Response(request.data)
