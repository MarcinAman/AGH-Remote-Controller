import src.Backend.Facility as Facility


class Room:
    def __init__(self, room):
        self.name = room[0]
        self.facilities = self.__parse_facilities(room[1])

    def __parse_facilities(self, facilities):
        return [Facility.Facility(k,v) for k,v in facilities.items()]

