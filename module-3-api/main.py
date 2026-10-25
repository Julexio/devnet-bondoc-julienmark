import random
import requests


POKEMON_LIST = ["charizard", "pikachu", "squirtle", "bulbasaur", "eevee"]
secret_pokemon = random.choice(POKEMON_LIST).lower()
url = f"https://pokeapi.co/api/v2/pokemon/{secret_pokemon}"


tugon = requests.get(url)

if tugon.status_code == 200:
    data = tugon.json()

    print("Laki (Height):", data["height"])
    print("Bigat (Weight):", data["weight"])

    attempts = 3
    while attempts > 0:
        guess = input("Guess the pokemon: ").strip().lower()

        if guess == secret_pokemon:
            print("Tama! You guessed it!")
            break
        else:
            attempts -= 1
            print(f"Mali! Remaining attempts: {attempts}")

    if attempts == 0:
        print(f"Game over! The secret pokemon was {secret_pokemon}.")
else:
    print("Hindi makuha ang data sa PokéAPI.")
