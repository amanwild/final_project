import cv2                     
c = cv2.VideoCapture(0)
c.open("http://192.168.0.101:8080/video")

while (True):
    success, f = c.read()
    cv2.imshow("Object Detection in real time (Press q to EXIT)", f)             
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break 
cv2.destroyAllWindows()

