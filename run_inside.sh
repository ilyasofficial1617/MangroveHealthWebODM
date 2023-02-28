#!/bin/bash

if [ ! -d "yolov7" ]; then
	echo "cloning yolov7"
	git clone -b mask https://github.com/WongKinYiu/yolov7.git
fi
if [ ! -f "model/yolov7-mask.pt" ]; then
	wget -P model/ https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-mask.pt
fi
echo "installing required python package"
pip3 install -r requirements.txt 
echo "starting flask webapp"
python3 -m flask run --host=0.0.0.0 --port 5001 --debug