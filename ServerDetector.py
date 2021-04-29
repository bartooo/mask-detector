import socket
import threading
import multiprocessing
import cv2
import pickle
import struct
import imutils
import errno
from datetime import datetime
from DataPacker import DataPacker
from ConnectionExceptions import WrongPortException, validate_port
from typing import Any


class ServerDetector:
    """Server detector represents server (working in LAN) which dowloads
    image from camera and sends it to connected host
    """

    def __init__(self, serv_addr: str, serv_port: int):
        """ServerDetector constructor.

        Args:
            serv_addr (str): address of server (0.0.0.0 accepts every connection)
            serv_port (int): 4-digit integer representing port
        """
        validate_port(serv_port)
        # address on which server listen
        self.serv_addr = serv_addr
        self.serv_port = serv_port
        # server name representing for connections
        self.serv_official_name = socket.gethostname()
        # creating socket with internet adress family, connection as socket stream
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # reusing address will let server to start continuosly on same port
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # binding socket to address of server
        self.server_socket.bind((self.serv_addr, self.serv_port))

    def handle_client(self, conn: socket, addr: Any) -> None:
        """Function handles connected client by sending him image from camera.

        Args:
            conn (socket): socket of client
            addr (Any): address of client
        """
        print(f"[SERVER] {addr} connected.")
        try:
            # take camera
            vid = cv2.VideoCapture(0)
            while True:
                # get frame
                img, frame = vid.read()
                # resize frame
                frame = imutils.resize(frame, width=480)
                # create data to send
                data_to_send = DataPacker(frame, f'{datetime.now().strftime("%H:%M:%S")}', 50)
                # pickle frame, pack and send
                pickled_to_send = pickle.dumps(data_to_send)
                message = struct.pack("Q", len(pickled_to_send)) + pickled_to_send
                conn.sendall(message)

        except socket.error as e:
            # if someone disconnected
            if e.errno != errno.EPIPE:
                print(f"[SERVER] UNEXPECTED ERROR WHILE SENDING TO: {addr}!")
            else:
                print(f"[SERVER] BROKEN PIPE WHILE CONNECTION TO: {addr}!")

        finally:
            print(f"[SERVER] EXCEPTIONAL CLOSING CONNECTION TO: {addr}")
            conn.close()

    def listen(self) -> None:
        """Function starts server listening."""
        # strating listening
        self.server_socket.listen()
        print(f"[SERVER] Listening on {self.serv_official_name}:{self.serv_port}...")
        while True:
            # wait for connection to server
            conn, addr = self.server_socket.accept()
            # if someone already is connected to server, allow noone
            if threading.active_count() - 1 == 1:
                print(
                    f"[SERVER] CLOSING CONNECTION FROM {addr} | CAUSE: SERVER IS OCCUPIED"
                )
                conn.close()
            else:
                # start new thread of sending camera
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                print(f"[SERVER] ACIVE CONNECTIONS={threading.activeCount() - 1}")


if __name__ == "__main__":
    serverDetector = ServerDetector("0.0.0.0", 8006)
    serverDetector.listen()
