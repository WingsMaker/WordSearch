import random             # for random.choice function
from pprint import pprint # better print layout

def writeln():
    print("=====================================================================")


# Define Player variables
def Player_Add(player_id):
    return {'player_id': player_id, 'player_name': '', 'time_played': 0, 'player_pokemon': {}, 'gyms_visited': [] }

# Creates a player and some player id.
Player_One = Player_Add(1)
Player_One['player_name'] = "sg_dsi7_student_19"

pprint(Player_One)
writeln

# There were 10 different Pokemon Go - gym locations websites already know.
gym_locations = ['amazon.com', 'ebay.com', 'github.com', 'linkedin.com', 'netflix.com', 'quora.com', 'reddit.com', 'sporcle.com', 'stackoverflow.com', 'twitter.com']
# more sites for testing:
# https://www.pogomap.info/gym/alien-musician-mural/90600296
# https://niantic.helpshift.com/a/pokemon-go/?p=web
print('The existing gym locations are :\n', gym_locations )
writeln

# Select 2 different gym location
gym1 = random.choice(gym_locations)
gym2 = gym1
while (gym1 == gym2):
    gym2 = random.choice(gym_locations)
print(gym1, gym2)
writeln

# add 2 location to that players
Player_One['gyms_visited'].append(gym1)
Player_One['gyms_visited'].append(gym2)
print('gyms loc site visited by this player:\n', Player_One['gyms_visited'])
writeln

# The Pokemon object structue
def PokeAdd( name):
    return {'Name': name, 'Type': '', 'Total': '', 'HP': '', 'Attack': '', 'Defense': '', 'SpecialAttack': '', 'SpecialDefense': '', 'Speed': ''}

# Create 3 different Pokemons
Pokemon_charmander = PokeAdd( "Charmander" )
Pokemon_squirtle = PokeAdd( "Squirtle" )
Pokemon_bulbasaur = PokeAdd( "Bulbasaur" )

PokemonID = [1, 2, 3]
PokemonInfo = [ Pokemon_charmander, Pokemon_squirtle, Pokemon_bulbasaur]
PokeDex=dict(zip(PokemonID, PokemonInfo))

pprint(PokeDex)

Player_Two = Player_Add(2)
Player_Two['player_name'] = "sg_dsi7_student_9"
Player_Two['gyms_visited'].append('alcatraz')
Player_Two['gyms_visited'].append('pacific_beach')
print('gyms loc site visited by this player:\n', Player_Two['gyms_visited'])

pprint(Player_Two)

Player_One['player_pokemon'] = { 2: Pokemon_squirtle}
pprint(Player_One)

Player_Two['player_pokemon'] = { 1: Pokemon_charmander, 2: Pokemon_bulbasaur}
pprint(Player_Two)

"""
6. What gyms have players visited?
### 6.1
Write a for-loop that:

Iterates through the pokemon_gyms list of gym locations you defined before.
For each gym, iterate through each player in the players dictionary with a second, internal for-loop.
If the player has visited the gym, print out "[player] has visited [gym location].", filling in [player] and [gym location] with the current player's name and current gym location.
"""





