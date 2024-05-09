from ultralytics import YOLO
model = YOLO("yolov8n.yaml") # build a new model from scratch
model = YOLO("yolov8n.pt") # load a pretrained model (recommended for training)
results = model.predict("https://ultralytics.com/images/bus.jpg") #predict on an image
result = results[0]
len(result.boxes)
box = result.boxes[0]
print("Object type:",box.cls[0])
print("Coordinates:",box.xyxy[0])
print("Probability:",box.conf[0])
cords = box.xyxy[0].tolist()
cords = [round(x) for x in cords]
class_id = result.names[box.cls[0].item()]
conf = round(box.conf[0].item(), 2)
print("Object type:", class_id)
print("Coordinates:", cords)
print("Probability:", conf)
for box in result.boxes:
 class_id = result.names[box.cls[0].item()]
if class_id:
 count = count + 1
cords = box.xyxy[0].tolist()
cords = [round(x) for x in cords]
conf = round(box.conf[0].item(), 2)
print("Object type:", class_id)
print("Coordinates:", cords)
print("Probability:", conf)
print("---")
from PIL import Image
Image.fromarray(result.plot())