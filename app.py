import requests


while True:
    profile = input("Enter your chess.com username: ")

    API_URL= "https://api.chess.com/pub/player/"+profile

    response = requests.get(API_URL, headers={"User-Agent": "karmadebjit2@gmail.com"})

    print(response.json())