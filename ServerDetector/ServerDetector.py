import socket
import threading
import multiprocessing
import cv2
import pickle
import struct
import imutils
import errno
from datetime import date, datetime
from typing import Any
import sys
from ServerDetector.face_mask_detector import FaceMaskDetector
from ServerDetector.parameters import (
    IMG_HEIGHT,
    IMG_WIDTH,
    SAVE_DIR,
    FACE_DETECTOR_PATH,
)
from DataPacker.DataPacker import DataPacker
from DetectorExceptions.ConnectionExceptions import WrongPortException, validate_port


class ServerDetector:
    """Server detector represents server (working in LAN) which dowloads
    image from camera and sends it to connected host
    """

    def __init__(self, serv_addr: str, serv_port: int, camera: Any = None):
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
        self.detector = FaceMaskDetector(
            face_detector_path=FACE_DETECTOR_PATH,
            model_path=SAVE_DIR,
        )
        if camera is None:
            self.camera = cv2.VideoCapture(0)
            _ = self.camera.read()
        else:
            self.camera = camera

    def handle_client(self, conn: socket, addr: Any) -> None:
        """Function handles connected client by sending him image from camera.

        Args:
            conn (socket): socket of client
            addr (Any): address of client
        """
        print(f"[SERVER] {addr} connected.")
        try:
            time_after_send = None
            while True:
                # get frame
                img, frame = self.camera.read()
                # get time
                time_of_read = datetime.now()
                # resize frame
                frame_classify = cv2.resize(frame, (IMG_WIDTH, IMG_HEIGHT))
                # create data to send
                prediction, percentage, frame = self.detector.predict_img(
                    frame_classify
                )
                data_to_send = DataPacker(
                    frame, prediction, percentage, time_after_send
                )
                # pickle frame, pack and send
                pickled_to_send = pickle.dumps(data_to_send)
                message = struct.pack("Q", len(pickled_to_send)) + pickled_to_send
                conn.sendall(message)
                time_after_send = datetime.now() - time_of_read

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
