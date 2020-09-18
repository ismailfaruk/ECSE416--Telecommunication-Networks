import socket
import argparse
import sockethelp
import os
import time
from PIL import Image

#----------------------------------------Client Constant Definitions----------------------------------------
DEFAULT_TIMEOUT = 5             # Default timeout for client to wait for a response
ENCODE_FORMAT = "utf-8"         # Message encoder format
#--------------------------------------------------------------------------------------------------

def interface():

    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    parser.add_argument('port', type=int)
    parser.add_argument('filename', type=str)
    parser.add_argument('timeout', type=int, nargs='?', default=DEFAULT_TIMEOUT)
    args = parser.parse_args()
    return args

def client(host, port, filename, timeout = DEFAULT_TIMEOUT):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(timeout)
    client_socket.connect((host, port))
    print("Connection: OK")

    request_message = f"GET /{filename} HTTP/1.1"
    sockethelp.write_http_header(client_socket, request_message)
    print("Request message sent.")

    # Print HTTP Header
    server_message = sockethelp.read_http_header(client_socket)

    print("Server HTTP Response: ", server_message)

    # Create dictionary that holds header information
    # Example : {'Content-Type': 'text/plain', 'Content-Length': '1024'}
    response_headers = dict([header.split(': ') for header in server_message.splitlines()[1:]]) 
    
    # Handle HTTP Body if response headers exist (Should maybe instead check for 404)
    if response_headers:

        # the response is decoded to get the file content
        file_content = sockethelp.read_http_body(client_socket, int(response_headers['Content-Length']))
        
        # Handle what to do with file_content based on content type.
        content_type = response_headers['Content-Type']
        if content_type == "text/plain":
            file_content = file_content.decode(ENCODE_FORMAT)
            print(file_content)
        elif content_type == "image/jpeg":
            epoch = time.time()
            tempImage = f"tempImage{epoch}.jpg"          # epic time is added to temp file to avoid duplicate names
            with open(tempImage, "wb") as temp:
                temp.write(file_content)
            im = Image.open(tempImage)
            im.show()
            
            # removes tempImage file
            os.remove(tempImage)
            
    client_socket.close()
    print("\nSocket Closed.")



if __name__ == "__main__":
    client_params = interface()
    
    try:
        client(client_params.host, client_params.port, client_params.filename, client_params.timeout)
    except Exception as error_message:
        print("- ERROR: ", error_message)