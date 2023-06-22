import requests
pokemon=input("Which Pokemon Do You Want To Find?")
pokemon=pokemon.lower()
url=f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
req=requests.get(url)
data=req.json()
print(f"Name is :{data['name']}")
print("Abilities: ")
for ability in data['abilities']:
    print(ability['ability']['name'])
