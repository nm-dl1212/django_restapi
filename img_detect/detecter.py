import os
import torch

# 予測モデル
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

def detect(img):
    result = model(img)
    result.save(save_dir=f"{os.path.dirname(img)}_detect/")
    return result