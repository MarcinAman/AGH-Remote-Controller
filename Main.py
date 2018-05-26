import sys
import src.Backend.Controller

if __name__ == '__main__':
    controller = src.Backend.Controller.Controller(sys.path[0] + '/resources/conf.yaml')