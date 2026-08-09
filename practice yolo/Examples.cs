import cv2
from ultralytics import YOLO

def calculate_center_and_area(bbox):
    xmin, ymin, xmax, ymax = bbox
    
    x_center = (xmin + xmax) / 2  
    y_center = (ymin + ymax) / 2
    
    width = xmax - xmin
    height = ymax - ymin 
    area = width * height
    if area > 5000:
        return (x_center, y_center), area
    else:
        return None, area

box = [100, 50, 300, 250] # xmin=100, ymin=50, xmax=300, ymax=250
center1, area1 = calculate_center_and_area(box1)
print("Box 1 -> Center:", center1, "| Area:", area1)

box2 = [10, 10, 20, 20] 
center2, area2 = calculate_center_and_area(box2)
print("Box 2 -> Center:", center2, "| Area:", area2)
