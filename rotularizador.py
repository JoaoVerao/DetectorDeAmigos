from ultralytics import YOLO

model = YOLO(f"runs/detect/train4/weights/best.pt")

results = model.predict(source="friends.mp4", conf=0.5, save=True)

results.show()