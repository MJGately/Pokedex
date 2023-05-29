import os
import pokepy
import requests
import sys
import pokebase
import json


poke_name = ''
'''Take user input and call-back pokemon's pokedex entry'''
#function for taking user input and storing as a variable
def cmdline_input():
    poke_name = sys.argv[1]
    return poke_name
    
def user_input():
    poke_name = input("please enter a pokemon's name   ")
    return poke_name


#function for calling API and returning JSON data
def call_poke_api(poke_name):
    api_url = 'https://pokeapi.co/api/v2/pokemon/' + poke_name
    response = requests.get(api_url)
    response = json.dumps(response.json(), indent=4)
    return response

poke_name = user_input()
print(call_poke_api(poke_name))


#use user input to call api and return pokedex info




