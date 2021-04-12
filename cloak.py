import cv2
import numpy as np
import time

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
time.sleep(3)

for i in range(30):
    check,background = video.read()
background = np.flip(background, axis=1)

while(video.isOpened()):
    check,img=video.read()
    if check==False:
        break

    img=np.flip(img,axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,50])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    mask1 = mask1+mask2
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(img,img, mask=mask2)
    res2 = cv2.bitwise_and(background,background, mask=mask1)

    final = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow("final",final)
    key = cv2.waitKey(1)
    if  key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
    
 


