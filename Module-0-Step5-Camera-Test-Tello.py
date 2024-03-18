# First, you need to install the necessary packages for Tello and OpenCV:
# pip install opencv-python
# pip install djitellopy

from djitellopy import Tello
import cv2

# Initialize and connect to Tello
tello = Tello()
tello.connect()
tello.streamon()  # Start the video stream

# Get the video frame from the Tello stream
frame_read = tello.get_frame_read()

# Display the video stream until 'q' is pressed
while True:
    frame = frame_read.frame
    cv2.imshow("Tello Stream", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Properly close the video stream and disconnect
cv2.destroyAllWindows()
tello.streamoff()
tello.end()
