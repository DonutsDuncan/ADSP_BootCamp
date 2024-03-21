import cv2
import torch
from djitellopy import Tello  # Make sure to install djitellopy library

# Initialize the Tello drone
tello = Tello()

# Connect to the Tello drone
tello.connect()

# Start video streaming from Tello
tello.streamon()

# Setup YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

while True:
    # Get the current frame from the Tello drone's video stream
    frame = tello.get_frame_read().frame
    if frame is None:
        print("Failed to grab frame")
        break

    # Convert the frame from BGR (OpenCV default) to RGB (YOLOv5 expects RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Pass the frame to YOLOv5 for object detection
    results = model(frame_rgb)

    # Convert results to rendered frame (with detection overlays) and display
    rendered_frame = results.render()[0]
    
    # Convert rendered frame back to BGR for OpenCV display
    rendered_frame_bgr = cv2.cvtColor(rendered_frame, cv2.COLOR_RGB2BGR)
    cv2.imshow('YOLOv5 Tello Detection', rendered_frame_bgr)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
tello.streamoff()
cv2.destroyAllWindows()
