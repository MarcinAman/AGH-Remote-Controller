import src.Backend.Parser
import src.Backend.Room
import src.GUI.View
import src.Backend.Communication


def get_facilities_from_rooms(rooms):
    return [x for y in rooms for x in y.facilities]


class Controller:
    def __init__(self, path):
        parsed = src.Backend.Parser.parse_yaml(path)
        self.rooms = [src.Backend.Room.Room(x) for x in parsed]

        self.app = src.GUI.View.Application(lambda x: src.Backend.Communication.send_communicate(x))
        self.app.create_labels(get_facilities_from_rooms(self.rooms))
        self.app.mainloop()
