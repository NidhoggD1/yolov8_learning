from ultralytics import YOLO

model = YOLO('models/yolov8s.pt')

model.info()