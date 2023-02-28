FROM ubuntu:20.04

# updating the os
RUN apt-get update && apt-get upgrade -y
# install python
RUN apt-get install -y python3 python3-pip python3-wheel python3-setuptools
# install the pytorch
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
RUN apt-get install -y git g++ gcc  && \
	python3 -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
RUN apt-get -y install wget
RUN python3 -V 