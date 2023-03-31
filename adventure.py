import sys
import json 

from utils import validate_game_map, sanitize_user_input
from world_state import WorldState
from execute_verb import execute_user_input

def main():
	fileName = sys.argv[1]
	f = open(fileName, "r")
	content = f.read()
	game_map = json.loads(content)
	if not validate_game_map(game_map):
		print("Provided mapfile is not valid")
		return
	
	world_state = WorldState(0, [], game_map)
	world_state.print_current_room()
	
	while True:
		action = input("What would you like to do? ")
		action = sanitize_user_input(action)
		action_output = execute_user_input(action, world_state)
		if action_output != -1:
			world_state = action_output


if __name__=="__main__":
	main()
