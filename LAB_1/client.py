import socket
import argparse
import sockethelp

#----------------------------------------Client Definitions----------------------------------------
Host = socket.gethostname()     # Sets the current computer name as hostname
Port = 1337                     # low number ports are usually reserved, use a nice high number (4 digits) https://docs.python.org/3.5/howto/sockets.html
BufferSize = 1024               # MAX of 1024 bytes for the buffer
EncodeFormat = "utf-8"          # Message encoder format
Timeout = 5                     # Set timeout to 1 second so accept() will become (somewhat nonblocking)
#--------------------------------------------------------------------------------------------------

def interface():
    # TODO: Uncomment this once HTTP request + opening files on server is done

    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    parser.add_argument('port', type=int)
    parser.add_argument('filename', type=str)
    parser.add_argument('timeout', type=int, nargs='?', default=5)
    args = parser.parse_args()
    print(args.host)
    return args

def client(Host, Port, Filename, Timeout):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((Host, Port))
        print("Connection: OK")        

        sockethelp.write(client_socket, Filename)
        print("Request message sent.")

        ServerMessage = sockethelp.read(client_socket)
        print("Server HTTP Response: ", ServerMessage)
        
        client_socket.close()
        print("Socket Closed.")

    except Exception as ErrorMessage:
        print("- ERROR: ", ErrorMessage)

    # TODO
    # 1. Set up client_socket with argument values
    # 2. Print file content when  HTTP response received, otherwise terminate after <-timeout>

if __name__ == "__main__":
    # Input = interface()
    # client(Input.host, Input.port, Input.filename, Input.timeout)
    client(Host, Port, "pic.jpg", Timeout)