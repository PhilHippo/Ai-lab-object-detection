import cv2 as cv

URL = "http://192.168.94.231"

cap = cv.VideoCapture(URL + ":81/stream")

while True:
    ret, frame = cap.read()
    frame = cap.read()[1]
    cv.imshow('Matches', frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
print('Done.')

