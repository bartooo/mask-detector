import socket
import cv2
import pickle
import struct
import sys
from DetectorExceptions.ConnectionExceptions import WrongPortException, validate_port
from DataPacker.DataPacker import DataPacker


class HostClient:
    """Class represents single host-client, which connects to given server
    and gets from it data.
    """

    def __init__(self, serv_name: str, serv_port: int) -> None:
        """Constructor of HostClient

        Args:
            serv_name (str): name or ip of server
            serv_port (int): port of server to connect
        """
        validate_port(serv_port)
        self.server_name = serv_name
        self.server_port = serv_port
        # size of payload
        self.payload_size = struct.calcsize("Q")
        # creating client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connecting to server
        self.connect()

    def connect(self):
        """Function connects to server"""
        self.client_socket.connect((self.server_name, self.server_port))

    def start(self):
        """Function starts connection to server and downloads data from it"""
        data = b""
        while True:
            # while loop to get size of receiving data
            while len(data) < self.payload_size:
                packet = self.client_socket.recv(4 * 1024)  # 4KB
                if not packet:
                    break
                data += packet
            # counting size of sending data
            packed_msg_size = data[: self.payload_size]
            # if in first while loop there was download part of data, need to add it on start
            data = data[self.payload_size :]
            msg_size = struct.unpack("Q", packed_msg_size)[0]
            # receiving concrete data
            while len(data) < msg_size:
                data += self.client_socket.recv(4 * 1024)
            # getting all data for current state
            data_recv_pickled = data[:msg_size]
            # setting data to whats left for next state
            data = data[msg_size:]
            # unpickle what we got
            data_recv = pickle.loads(data_recv_pickled)
            # show image and if q pressed - stop
            cv2.imshow("RECEIVING VIDEO", data_recv.frame)
            print(
                f"[CLIENT] GOT IMAGE AT TIME: {data_recv.decision} | WITH PERCENTAGE: {data_recv.percentage}%"
            )
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        # disconnect from server
        self.disconnect()

    def disconnect(self):
        """Simple function disconnects from server."""
        self.client_socket.close()
