import cv2
import numpy as np
import glob
from models import Yolov4
from tool import utils, torch_utils
import torch

f_names = glob.glob("test2/*.png")

model = Yolov4(yolov4conv137weight=None, n_classes=1, inference=True)
model.load_state_dict(torch.load("Yolov4.pth"))
model.cuda().eval()

for f in f_names:
    im = cv2.imread(f)
    im = cv2.resize(im, (512, 320))

    with torch.no_grad():
        boxes = torch_utils.do_detect(model, cv2.cvtColor(im, cv2.COLOR_BGR2RGB), 0.4, 0.4, 1)
        utils.plot_boxes_cv2(im, boxes[0], "b" + f, color=(0,0,255))
