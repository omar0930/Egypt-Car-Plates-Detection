# -*- coding: utf-8 -*-
"""Omar's AI301Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LFVPMa8__FHKBH8OoTPOh27HKMo9B5hT

#Cars Plates Project

#Install Dependencies

We will Install YOLO v7 Dependencies to begin usage of our model.
"""

!nvidia-smi

# Commented out IPython magic to ensure Python compatibility.
# Download PreTrained Model YOLO v7 repository and install requirements

!git clone https://github.com/SkalskiP/yolov7.git
# %cd yolov7
!git checkout fix/problems_associated_with_the_latest_versions_of_pytorch_and_numpy
!pip install -r requirements.txt

# We will call Our dataset from roboflow

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="Wu0sLKhSnRHxDyxReORm")
project = rf.workspace("must-usuxb").project("ai301-2ngoj")
dataset = project.version(1).download("yolov7")

"""# Start The Training


"""

# Commented out IPython magic to ensure Python compatibility.
# download COCO starting checkpoint
# %cd /content/yolov7
!wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt

# Commented out IPython magic to ensure Python compatibility.
#  Start The project for training
# %cd /content/yolov7
!python train.py --batch 16 --epochs 80 --data {dataset.location}/data.yaml --weights 'yolov7_training.pt' --device 0

# Run evaluation
!python detect.py --weights runs/train/exp/weights/best.pt --conf 0.1 --source {dataset.location}/test/images

#display inference on ALL test images

import glob
from IPython.display import Image, display

i = 0
limit = 10000 # max images to print
for imageName in glob.glob('/content/yolov7/runs/detect/exp/*.jpg'): #assuming JPG
    if i < limit:
      display(Image(filename=imageName))
      print("\n")
    i = i + 1



"""#  Deployment


"""

# saving the model to not train again

!zip -r export.zip runs/detect
!zip -r export.zip runs/train/exp/weights/best.pt
!zip export.zip runs/train/exp/*

"""#thank you

I trained this object  Using YOLOV7 and it achieved 0.94 mAP!

I can use this model to read the plate number with high performance.


"""