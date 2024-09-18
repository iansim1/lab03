# Answer Problems 3, 5, and 5 here
from pokemon_api import *

name = get_pokemon_name(132)
attack = get_pokemon_attack("ditto")
defense = get_pokemon_defense("ditto")
types = get_pokemon_num_types("ditto")
type1  = get_pokemon_type1("ditto")
type2 = get_pokemon_type2("ditto")

print(f"{name} | {attack} | {defense} | {types} | {type1} | {type2}")