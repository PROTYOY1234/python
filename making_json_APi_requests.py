import requests
req= requests.get("https://swapi.dev/api/people/2/")
person=req.json()
print(person)
print(f"Name is: {person['name']}")
print(f"Birth Year is : {person['birth_year']}")
