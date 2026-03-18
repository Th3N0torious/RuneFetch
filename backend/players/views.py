import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def test_api(request):
    return Response({"message": "RuneFetch backend working"})


@api_view(['GET'])
def get_player(request, username):
    url = f"https://api.wiseoldman.net/v2/players/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        return Response({"error": "Player not found"}, status=404)

    return Response(response.json())