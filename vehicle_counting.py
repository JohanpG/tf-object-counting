#----------------------------------------------
#--- Author         : Ahmet Ozlu
#--- Mail           : ahmetozlu93@gmail.com
#--- Date           : 27th January 2018
#----------------------------------------------

# Imports
import tensorflow as tf

# Object detection imports
from utils import backbone
from api import object_counting_api
import cv2

#if tf.__version__ < '1.4.0':
#  raise ImportError('Please upgrade your tensorflow installation to v1.4.* or later!')



#input_video = "./input_images_and_videos/vehicle_survaillance.mp4" 
#input_video = "./input_images_and_videos/Transmi.mp4" 
input_video = 0
cam = cv2.VideoCapture(0)


# By default I use an "SSD with Mobilenet" model here. See the detection model zoo (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.
detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28')

# Filter python objects with list comprehensions
#category_index  = [category_index[i] for i in [1,2,3,4]]
#category_index = { your_key: category_index[your_key] for your_key in [1,2,3,4] }
#print(category_index)
fps = 30 # change it with your input video fps
width = 640 # change it with your input video width
height = 480 # change it with your input vide height

cam.set(3,width)
cam.set(4,height)

is_color_recognition_enabled = 0 # set it to 1 for enabling the color prediction for the detected objects
roi = round(width/2) # roi line position
roiAreas= []
roi_1 = (100, 10, 300, 190)
roiAreas.insert(0,roi_1)
roiTop = round((height/3)*2) # roi line position
roiBottom = round((height/3)*1) # roi line position
roiLeft = round((width/3)*1) # roi line position
roiRight = round((width/3)*2) # roi line position
#roiAreas= [roiTop,roiBottom,roiLeft,roiRight ]
deviation = 5 # the constant that represents the object counting area
logFile = "traffic_measurement.csv"
targeted_objects = ["car","bus", "truck","bycicle", "motorbike"] # (for counting targeted objects) change it with your targeted objects
#targeted_objects = "car" # (for counting targeted objects) change it with your targeted objects
#object_counting_api.cumulative_object_counting_y_axis(input_video, detection_graph, category_index, is_color_recognition_enabled, fps, width, height, roi, deviation) # counting all the objects
object_counting_api.cumulative_object_counting_x_axis(input_video, detection_graph, category_index, is_color_recognition_enabled, targeted_objects, fps, width, height, roi, deviation, logFile, roiAreas) # counting all the objects
