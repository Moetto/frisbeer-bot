import requests

api_url = "https://ranta.org/frisbeer/API/"
# api_url = "http://localhost:8000/API/"
players = "players"
games = "games"
content_type = {'content-type': 'application/json' }


class APIError(Exception):
    pass


class API:
    @staticmethod
    def get_players():
        response = requests.get(api_url + players, headers=content_type)
        if not response.ok:
            raise APIError("Error in response")
        try:
            return response.json()
        except ValueError as e:
            raise APIError(e)

    @staticmethod
    def create_game(name="asd"):
        response = requests.post(api_url + games, headers=content_type, data={})

