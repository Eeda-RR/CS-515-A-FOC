from utils import sanitize_string

def get_matched_exit(user_input_exit, current_room_exits):
	if user_input_exit in current_room_exits:
		return user_input_exit
	filtered_exits = list(filter(lambda word: sanitize_string(word).startswith(user_input_exit), current_room_exits))
	if len(filtered_exits) == 1:
		return filtered_exits[0]
	elif len(filtered_exits) > 1:
		output_str = "Did you want to go "
		for i in range(0,len(filtered_exits),1):
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


def execute_look(user_input, world_state):
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

	
def execute_user_input(user_input, world_state):
	verb = user_input[0]
	verbs = ["go", "look", "inventory","get"]
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
