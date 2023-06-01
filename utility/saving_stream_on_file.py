import cv2


# http://192.168.94.231 Mi A3

#URL = "http://192.168.94.231" #casa simo

URL= "http://192.168.1.15" #casa anna 

cap = cv2.VideoCapture(URL + ":81/stream")

#save video resolution
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)

#VideoWriter object will save the stream in 'filename.avi' file.
result = cv2.VideoWriter('videoshooting.avi', cv2.VideoWriter_fourcc(*'MJPG'), 24, size)

while True:
    frame = cap.read()[1]

    result.write(frame)

    cv2.imshow('stream', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

print('Video saved.')