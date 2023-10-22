from ultralytics import YOLO
model = YOLO("yolov8n.yaml")
results = model.train(date="", epochs=3)