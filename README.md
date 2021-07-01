# Real-Time Face Mask Detector

![Baner](https://user-images.githubusercontent.com/59453698/123649505-1788cf00-d82a-11eb-8bed-03fa0dd2136c.png)


<!-- badges: start -->
![CI/CD STATUS](https://github.com/bartooo/mask-detector/actions/workflows/python-package.yml/badge.svg)
<!-- badges: end -->

### I. Introduction
Real-Time Face Mask Detector is a project made by [Łukasz Staniszewski](https://github.com/lukasz-staniszewski) and [Bartosz Cywiński](https://github.com/bartooo) for college classes. Our purpose was to create and develop application which enables to detect Covid-19 mask in real time with Client-Server socket connection architecture.

:poland: :poland: If you want to see full documentation of project, prepared specially for college course, [click here](https://github.com/bartooo/mask-detector/blob/main/docs/final_documentation_pl.pdf). :poland: :poland:

Project architecture is divided on:
+ **Server** - python script representing socket server, to which client can connect. After client's correct connection server is downloading in real-time frames from camera, which is connected to same (sub)system on which server is running. Server processes image by using Haar Cascades with OpenCV in order to detect face(s) in the frame and then, when face is detected, its running algorithm with pre-trained (using tensorflow) model to detect Covid-19 mask. After full processing, server sends to client frame with decision made on it and conviction in made decision.
+ **Client** - python script representing socket client with proper Graphical User Inteface made with QT. Client's application enables to connect to server by giving IP of server and allows user to receive detection status.

### II. Folder structure
    .
    ├── ClientDetector              # code and resources for client application
    │   ├── pyui                    # code implementing ui
    │   │   └── ui                  # ui created with qt designer
    │   ├── resources               # resources for gui
    │   ├── config.ini              # config file to type manually server's ip and port
    │   └── tests                   # unit tests provided for client app
    ├── DataPacker                  # code for data sended between server and client
    │   └── tests                   # unit tests for data packer
    ├── DetectorExceptions          # connection exceptions code
    ├── ServerDetector              # code and resources for server application
    │   ├── haar-classifier         # face detection model
    │   ├── images                  # images for tests
    │   ├── model                   # mask-detection model
    │   └── tests                   # unit tests provided for server app
    ├── docs                        # folder with official polish documentation
    ├── logs                        # folder when logs are placed
    ├── requirements.txt            # python modules needed to be installed to run apps
    ├── mainClient.py               # script running client app
    └── mainServer.py               # script running server app

### III. Installation
1. In order to install app you need to stock up with [Python 3.9.5](https://www.python.org/downloads/release/python-395/) and Windows/Linux Operating System.
2. Download repository:
```
git clone https://github.com/bartooo/mask-detector.git
cd mask-detector
git-lfs pull
```
3. Create virtual environment and install modules:
```
python -m venv venv
.\venv\Scripts\activate   [on Linux: source ./venv/bin/activate]
pip install -r .\requirements.txt
```
### IV. How to run
1. Open two separate terminal windows and _cd_ in both of them to folder with installed project.
2. Activate virtual environment in both terminals:
```
.\venv\Scripts\activate   [on Linux: source ./venv/bin/activate]
```
3. Run _Server_ script in one of terminals:
```
python .\mainServer.py
```
4. When server finishes running, check server name to which you will connect. In below example its _DESKTOP-HT34P2E_:
```
...
2021-07-01 15:31:10.931750: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1264]
[SERVER] Listening on DESKTOP-HT34P2E:8006...
```
5. Run _Client_ script in second terminal:
```
python .\mainClient.py
```
6. Go to _SETTINGS_, type server name in correct input and _TEST CONNECTION_, you should see similiar result:

![CORRECT SETTINGS](https://user-images.githubusercontent.com/59453698/124145795-67b39b80-da8d-11eb-9f8c-5a34d49e3094.png)


7. If you see correct frame, click _CHANGE SERVER_.

8. You are free to detect your mask. Go back to Main Menu and click _START DETECTION_.

### V. Some results
+ Application correctly working.

![working gif](https://user-images.githubusercontent.com/59453698/124143671-9af52b00-da8b-11eb-99b7-06cf15697100.gif)

+ Application when no face provided.

![no face gif](https://user-images.githubusercontent.com/59453698/124144115-f6bfb400-da8b-11eb-94c5-d1016c949c27.gif)

+ Testing connection.

![test connection gif](https://user-images.githubusercontent.com/59453698/124144529-5918b480-da8c-11eb-9042-494d6ae38718.gif)

### VI. Credits
Surgical Medical Mask Graphic Vector Designed By rovian1993 from <a href="https://pngtree.com/">Pngtree.com</a>.



