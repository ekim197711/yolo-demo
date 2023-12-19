from ultralytics import YOLO
# Load a model
# model = YOLO('yolov8n.pt')  # load an official detection model
model = YOLO('yolov8n-seg.pt')  # load an official segmentation model
# model = YOLO('path/to/best.pt')  # load a custom model

# Track with the model
results = model.track(source="https://www.youtube.com/watch?v=Xdzuze5XSXE&ab_channel=MikeM%C3%B8llerNielsen", show=True)
# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")