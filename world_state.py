class WorldState:
    def __init__(self, current_room_index, inventory, room_map) -> None:
        self.current_room_index = current_room_index
        self.inventory = inventory 
        self.room_map = room_map
  
    def print_current_room(self):
        current_room = self.room_map[self.current_room_index]
        output = "> " + current_room["name"] + "\n\n" + current_room["desc"] + "\n\n"  
        if "items" in current_room and len(current_room["items"]) > 0:
            output += "Items:"
            for i in range(0,len(current_room["items"]),1):
                if i !=0 :
                    output += ","
                output += " " + current_room["items"][i]
            output += "\n\n" 
        output += "Exits:"
        for k,v in current_room["exits"].items():
            output += " " + k
        output += "\n"
        print(output)
