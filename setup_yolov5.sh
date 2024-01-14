#!/bin/bash

# install yolov5
git clone https://github.com/ultralytics/yolov5
pip install -r yolov5/requirements.txt

sudo apt-get update
sudo apt-get install libgl1-mesa-dev

# detection test 
python yolov5/detect.py --weights yolov5s.pt --source yolov5/data/images/bus.jpg 