from ultralytics import YOLO

model = YOLO()

model.train(
    task='detect',
    mode='train',
    model='yolov8m.pt',
    data='data.yaml',
    epochs=50,
    batch=10,
    imgsz=256,
    cache=True,
    device='cuda',
    workers=8,
    close_mosaic=0,
    mixup=0.2,
    verbose=True
)