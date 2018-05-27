import src.Backend.Parser
import src.Backend.Room
import src.GUI.View
import src.Backend.Communication
import src.Backend.SpeechRecognition as sr
from difflib import SequenceMatcher


def similar(a, b):
    """
    Function returns a similarity ratio which is between 0 and 1

    :param a:
    :param b:
    :return:
    """
    return SequenceMatcher(None, a, b).ratio()


def get_facilities_from_rooms(rooms):
    """
    Converting lists of Room to list of facilities in those rooms
    :param rooms: container with Room objects
    :return: list with facilities
    """
    return [x for y in rooms for x in y.facilities]


def get_command_string(facility):
    yield "wlacz " + facility.description.lower()
    yield "wylacz " + facility.description.lower()


def get_difference_with_commands(facilities, value):
    """
    Simple mapping with command in polish, similarity ratio and name of facility
    :param facilities: container with facilities
    :param value: value to be compared with every facility
    :return: list of tuples
    """
    return [(y, similar(value, y), x.name) for x in facilities for y in get_command_string(x)]


class Controller:
    def __init__(self, path):
        parsed = src.Backend.Parser.parse_yaml(path)
        self.rooms = [src.Backend.Room.Room(x) for x in parsed]

        self.app = src.GUI.View.Application(
            lambda x: src.Backend.Communication.send_communicate(x), lambda: self.voice_handler())
        self.app.create_labels(get_facilities_from_rooms(self.rooms))
        self.app.mainloop()

    def voice_handler(self):
        """
        Main voice handler

        It calls elements of Communication to get user's voice in text
        then tries to match it with the command

        if it is not possible (ratio is below 80%) an error is displayed
        :return:
        """
        try:
            response = sr.get_text_from_speech()
        except IOError:
            raise IOError("Speech recognition not possible")
        except ConnectionError:
            raise ConnectionError("API not available")

        difference_list = get_difference_with_commands(
            get_facilities_from_rooms(self.rooms),
            response
        )

        difference_list = sorted(difference_list, key=lambda key: key[1])

        if difference_list[-1][1] > 0.80:
            if difference_list[-1][0].startswith("wlacz"):
                src.Backend.Communication.send_communicate("0N "+difference_list[-1][2])
            else:
                src.Backend.Communication.send_communicate("OFF "+difference_list[-1][2])
        else:
            self.app.render_error_popup("Blad!","Nie udalo sie rozpoznac komendy \n otrzymano:"+response)
