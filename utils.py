import re

def validate_game_map(game_map):
    num_of_rooms = len(game_map)
    if num_of_rooms == 0:
        return False
    for item in game_map:
        room = item
        room_fields = room.keys()
        if "name" not in room_fields or "desc" not in room_fields or "exits" not in room_fields:
            return False
        if not isinstance(room["name"],str) or not isinstance(room["desc"],str) or not isinstance(room["exits"],dict):
            return False
        for k,v in room["exits"].items():
            if not isinstance(k,str):
                return False
            if not isinstance(v, int):
                return False
            if v < 0 or v >= num_of_rooms:
                return False
    return True


def sanitize_string(input_str):
    # remove white spaces
    pattern = re.compile(r'\s+')
    input_str = re.sub(pattern, ' ', input_str)
    # remove capitalisation
    pattern = re.compile(r'[A-Z]')
    input_str = re.sub(pattern, lambda letter : letter.group(0).lower(), input_str)
    input_str = input_str.lstrip()
    input_str = input_str.rstrip()
    return input_str

def sanitize_user_input(input_value):
    input_value = sanitize_string(input_value)
    return input_value.split(" ")
