import requests
import json
token ='cdb9d62b6aa724acbebbd67a03774303'

#response=requests.post(' https://pokemonbattle.me:5000/trainers/reg', json={
#  "trainer_token": token,
#  "email":'povarartem@gmail.com',
#  "password": "Ratchet231998"
#}, headers = {'Content-type':'application/json'})
#print(response.text)

#response_confirm=requests.post(' https://pokemonbattle.me:5000/trainers/confirm_email', json={
#   "trainer_token":token
#    }, headers={'Content-type':'application/json'})
#if response_confirm.status_code==200:
#    print('ok')
#else:
#    print('not ok')

response=requests.post(' https://pokemonbattle.me:5000/pokemons',
headers={'Content-type':'application/json','trainer_token':token},
json={
  "name": "King of pokemons",
  "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
print(response.text)

pokemon_id=response.json()['id']

response_change=requests.put(' https://pokemonbattle.me:5000/pokemons',
headers={'Content-type':'application/json','trainer_token':token},
json={
    "pokemon_id": pokemon_id,
   "name": "Pokemon King",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
print(response_change.text)

pokemon_id1=response_change.json()['id']

response_catch=requests.post(' https://pokemonbattle.me:5000/trainers/add_pokeball',
headers={'Content-type':'application/json','trainer_token':token},
json={
    "pokemon_id": pokemon_id1
})
print(response_catch.text)
#response=requests.post(' https://pokemonbattle.me:5000/pokemons/kill',
#headers={'Content-type':'application/json','trainer_token':token},
#json={
#    "pokemon_id": "3289"
#})
#print(response.text)