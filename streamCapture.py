import cv2

# se lo stream non parte forse è perchè è già attivo sul browser
# o browser o openCV, entrambi contemporaneamente non va

# http://192.168.178.146 wifi
# http://192.168.132.152 Mi A3

URL = "http://192.168.178.146"

cap = cv2.VideoCapture(URL + ":81/stream")

while True:
    frame = cap.read()[1]

    cv2.imshow('stream', frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
