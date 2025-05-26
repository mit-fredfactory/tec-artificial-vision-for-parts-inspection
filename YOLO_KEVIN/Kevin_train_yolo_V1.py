from roboflow import Roboflow
from ultralytics import YOLO

# Conexión con Roboflow
rf = Roboflow(api_key="JhU4fcAWzdRdeOykkQgm")  # API KEY 
project = rf.workspace("avyolo").project("av_test1")
dataset = project.version(1).download("yolov8")

# Entrenamiento del modelo YOLOv8
model = YOLO("yolov8n.yaml")
model.train(data=dataset.location + "/data.yaml", epochs=50, imgsz=640)
