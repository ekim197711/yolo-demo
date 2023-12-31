from ultralytics import YOLO

# Create a new YOLO model from scratch
# model = YOLO('yolov8n.yaml')

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')


# Perform object detection on an image using the model
results = model('cafeteria.jpg')

# Export the model to ONNX format
success = model.export(format='onnx')