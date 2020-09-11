import socket
import argparse

# TODO: Uncomment this once HTTP request + opening files on server is done

# parser = argparse.ArgumentParser()
# parser.add_argument('host', type=str)
# parser.add_argument('port', type=int)
# parser.add_argument('filename', type=str)
# parser.add_argument('timeout', type=int, nargs='?', default=5)

# args = parser.parse_args()

# print(args.host)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client usually remote to server, but in this case its on the same machine
client_socket.connect((socket.gethostname(), 1337))


client_socket.send(bytes("Successfully Connected!", "utf-8"))

# TODO
# 1. Set up client_socket with argument values
# 2. Print file content when  HTTP response received, otherwise terminate after <-timeout>
