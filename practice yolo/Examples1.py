import cv2
from ultralytics import YOLO

#The model 
model = YOLO("yolov10x.pt")

#open video 
cap = cv2.VideoCapture("highway_traffic.mp4")

#To save id 
track_history = {}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    #Turn on the tracking from use BOT-SORT to save Track IDS
    results = model.track(source=frame, persist=True, tracker="botsort.yaml", conf=0.45)

    for result in results:
        #Check for the presence of tracked targets
        if result.boxes is not None and result.boxes.id is not None:
            boxes = result.boxes.xyxy.cpu().numpy()
            track_id = result.boxes.id.int().cpu().numpy()
            class_id = result.boxes.cls.int().cpu().numpy()
            
            

            for box, track_id, cls_id in zip(boxes, track_id, class_id):
                xmin, ymin, xmax, ymax = box

                x_center = (xmin + xmax) / 2
                y_center = (ymin + ymax) / 2

                if track_id not in track_history:
                    track_history[track_id] = []
                
                track_history[track_id].append((x_center, y_center))

                print(f"Vehicle ID #{track_id} | Class: {cls_id} | Total Recorded Positions: {len(track_history[track_id])}")
cap.release()
