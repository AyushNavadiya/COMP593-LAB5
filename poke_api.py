'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests
from sys import argv
import json

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    name = str(pokemon_name)
    name = name.strip().lower()

    # TODO: Build a clean URL and use it to send a GET request
    url = f'https://pokeapi.co/api/v2/pokemon/' + name
    response_msg = requests.get(url)

    print(f'Getting information for {pokemon_name}...', end="")

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if response_msg.ok:
        print('success')
        response = response_msg.json()
        return response
    else:
        print("failure")
        print(f"Response code: {response_msg.status_code} ({response_msg.reason})")

    # TODO: If the GET request failed, print the error reason and return None

    return

if __name__ == '__main__':
    main()