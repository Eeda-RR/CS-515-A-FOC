from utils import sanitize_string
import re

def get_matched_exit(user_input_exit, current_room_exits):
	if user_input_exit in current_room_exits:
		return user_input_exit
	filtered_exits = list(filter(lambda word: sanitize_string(word).startswith(user_input_exit), current_room_exits))
	if len(filtered_exits) == 1:
		return filtered_exits[0]
	elif len(filtered_exits) > 1:
		output_str = "Did you want to go "
		for i in range(0,len(filtered_exits),1):
			if i != 0:
                output_str += " or"
			output_str += " " + filtered_exits[i]
		output_str += "?"
		print(output_str)
		return 0
	return -1

def execute_go(user_input, world_state):
	n = len(user_input)
	if n == 1:
		print("Sorry, you need to 'go' somewhere.")
		return world_state
	
	user_input_exit = user_input[1]
	current_room_exits = world_state.room_map[world_state.current_room_index]["exits"]
	directions_abbr = {"ne": "northeast", "nw": "northwest", "se": "southeast", "sw": "southwest", "n": "north", "e": "east", "w":"west", "s" : "south"}
	if user_input_exit in directions_abbr:
		user_input_exit = directions_abbr[user_input_exit]
	
	matched_exit = get_matched_exit(user_input_exit, current_room_exits)
	if matched_exit == 0:
		return world_state
	elif matched_exit == -1:
		print("There's no way to go " + user_input_exit + ".")
		return world_state
	else:
		user_input_exit = matched_exit
	
	exit_room_index = current_room_exits[user_input_exit]
	print("You go " + user_input_exit + ".\n")
	world_state.current_room_index = exit_room_index
	world_state.print_current_room()
	return world_state


def execute_inventory(user_input, world_state):
	if len(world_state.inventory) == 0:
		print("You're not carrying anything.")
		return world_state
	print("Inventory:")
	for i in range(0,len(world_state.inventory),1):
		print("  " + world_state.inventory[i])
	return world_state



def execute_look(user_input, world_state):
	world_state.print_current_room()
	return world_state




def get_matched_item(user_input_item, current_room_items):
    if user_input_item in current_room_items:
        return user_input_item
    filtered_items = list(filter(lambda word: re.search(user_input_item, sanitize_string(word)), current_room_items))
    if len(filtered_items) == 1:
        return filtered_items[0]
    elif len(filtered_items) > 1:
        output_str = "Did you want to get"
        for i in range(0,len(filtered_items),1):
            if i == 0:
                output_str += " the"
            elif i == len(filtered_items) - 1:
                output_str += " or the"
            else:
                output_str += ","
            output_str += " " + filtered_items[i]
        output_str += "?"
        print(output_str)
        return 0
    else:
        return -1

def execute_get(user_input, world_state):
    n = len(user_input)
    if n == 1:
        print("Sorry, you need to 'get' something.")
        return world_state

    user_input_item = user_input[1]
    if "items" not in world_state.room_map[world_state.current_room_index] : 
        current_room_items = []
    else :
        current_room_items = world_state.room_map[world_state.current_room_index]["items"]
    matched_item = get_matched_item(user_input_item, current_room_items)

    if matched_item == 0:
        return world_state
    elif matched_item == -1:
        print("There's no " + user_input_item + " anywhere.")
        return world_state
    else:
        user_input_item = matched_item
  
    print("You pick up the " + user_input_item + ".")
    world_state.room_map[world_state.current_room_index]["items"].remove(user_input_item)
    world_state.inventory.insert(0, user_input_item)
    return world_state


def execute_quit(user_input, world_state):
    print("Goodbye!")
    return -1

def get_matched_inv(user_input_item, current_inv):
    if user_input_item in current_inv:
        return user_input_item
    filtered_items = list(filter(lambda word: re.search(user_input_item, sanitize_string(word)), current_inv))
    if len(filtered_items) == 1:
        return filtered_items[0]
    elif len(filtered_items) > 1:
        output_str = "Did you want to drop"
        for i in range(0,len(filtered_items),1):
            if i == 0:
                output_str += " the"
            elif i == len(filtered_items) - 1:
                output_str += " or the"
            else:
                output_str += ","
            output_str += " " + filtered_items[i]
        output_str += "?"
        print(output_str)
        return 0
    else:
        return -1

def execute_drop(user_input, world_state):
    n = len(user_input)
    if n == 1:
        print("Sorry, you need to 'drop' something.")
        return world_state
  
    user_input_item = user_input[1]
    current_inv = world_state.inventory
    matched_inv = get_matched_inv(user_input_item, current_inv)

    if matched_inv == 0:
        return world_state
    elif matched_inv == -1:
        print("There's no " + user_input_item + " anywhere.")
        return world_state
    else:
        user_input_item = matched_inv
  
    print("You drop the " + user_input_item + ".")
    world_state.room_map[world_state.current_room_index]["items"].append(user_input_item)
    world_state.inventory.remove(user_input_item)
    return world_state


def execute_help(verbs, world_state):
    output = "You can run the following commands:"
    verbs_list = list(verbs.keys())
    for i in range(0,len(verbs_list),1):
        output += "\n  " + verbs_list[i]
        if verbs[verbs_list[i]] == 1:
            output += " ..."
    print(output)
    return world_state


	
def execute_user_input(user_input, world_state):
	verb = user_input[0]
	verbs = {"go" : 1, "get" : 1, "look" : 0, "inventory" : 0, "quit" : 0, "help" : 0}
	if verb in verbs:
		verb_found = verb
	
	if verb_found == "go":
		return execute_go(user_input, world_state)
	elif verb_found == "look":
		return execute_look(user_input, world_state)
	elif verb_found == "inventory":
		return execute_inventory(user_input, world_state)
	elif verb_found == "get":
		return execute_get(user_input, world_state)
	elif verb_found == "quit":
		return execute_quit(user_input, world_state)
	elif verb_found == "help":
		return execute_help(verbs, world_state)
	
