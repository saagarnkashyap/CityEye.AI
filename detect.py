from ultralytics import YOLO

model = YOLO("yolo11n.pt")
results = model.predict(source="input_video.mp4", save=True, conf=0.25)

print("Detection complete. Check the 'runs/detect/predict/' folder.")