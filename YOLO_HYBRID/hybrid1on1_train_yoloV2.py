from roboflow import Roboflow
from ultralytics import YOLO

# Conexión con Roboflow
rf = Roboflow(api_key="JhU4fcAWzdRdeOykkQgm")  # API KEY
project = rf.workspace("avyolo").project("av_test1-1")  # ← cambia el nombre del nuevo proyecto
dataset = project.version(2).download("yolov8")           # ← selecciona la versión v2

# Entrenamiento del modelo YOLOv8
model = YOLO("yolov8n.yaml")
model.train(data=dataset.location + "/data.yaml", epochs=50, imgsz=640)