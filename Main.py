import sys

import src.Backend.Parser
import src.Backend.Room

if __name__ == '__main__':
    parsed = src.Backend.Parser.parse_yaml(sys.path[0] + '/resources/conf.yaml')
    for room in parsed:
        src.Backend.Room.Room(room)