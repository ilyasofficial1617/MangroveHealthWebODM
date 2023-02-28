import yaml
import matplotlib.pyplot as plt
import torch
import cv2
import yaml
from torchvision import transforms
import numpy as np

# add yolov7 as module path
import sys
import os
sys.path.append(os.path.abspath("yolov7/"))

from utils.datasets import letterbox
from utils.general import non_max_suppression_mask_conf

from detectron2.modeling.poolers import ROIPooler
from detectron2.structures import Boxes
from detectron2.utils.memory import retry_if_cuda_oom
from detectron2.layers import paste_masks_in_image

class MangroveHealth : 
    def __init__(self):
        pass
        
    def test(self):
        return "Hi There! Welcome Back"