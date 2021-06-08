import socket
import struct
import socket


class DataGetter:
    """Class represents getter of data from server."""

    def __init__(self):
        """Constructor of DataGetter."""
        self.data = b""
        self.payload_size = struct.calcsize("Q")

    def get(self, client_socket: socket.socket) -> bytes:
        """

        Args:
            client_socket (socket.socket): client's socket

        Returns:
            bytes: series of bytes received
        """
        while len(self.data) < self.payload_size:
            packet = client_socket.recv(4 * 1024)  # 4KB
            if not packet:
                break
            self.data += packet
        # counting size of sending data
        packed_msg_size = self.data[: self.payload_size]
        # if in first while loop there was download part of data, need to add it on start
        self.data = self.data[self.payload_size :]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
        # receiving concrete data
        while len(self.data) < msg_size:
            self.data += client_socket.recv(4 * 1024)

        data_recv_pickled = self.data[:msg_size]
        self.data = self.data[msg_size:]
        return data_recv_pickled
