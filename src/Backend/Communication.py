import socket

UDP_IP = "255.255.255.255"
UDP_PORT = 2018


def send_communicate(msg):
    global UDP_IP,UDP_PORT

    sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sending_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    sending_socket.sendto(bytes(msg, "utf-8"), (UDP_IP, UDP_PORT))
