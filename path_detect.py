import cv2
import numpy as np
import math
video = cv2.VideoCapture(r"C:\Users\sinha\Downloads\lane_vgt.mp4")
cnt=1
while True:
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture(r"C:\Users\sinha\Downloads\lane_vgt.mp4")
        continue

    if cnt==1:
        #height,width=orig_frame.shape[:2]
        #roi=np.array([[(0, height), (10, 350), (400, 150), (2500, height)]], dtype=np.int32)
        #blank = np.zeros_like(orig_frame)
        #r = cv2.fillPoly(blank, roi, 255)
        r = cv2.selectROI(orig_frame)
       
        cnt=2
    imCrop = orig_frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    
    
    #frame = cv2.medianBlur(orig_frame, 5)
    #frame = cv2.bilateralFilter(orig_frame, 7, 75, 75)
    frame = cv2.GaussianBlur(imCrop, (5,5), 0)
    kernal = np.ones((5,5),np.uint8)
   # opening = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernal)
    closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernal)
    #cat = np.ones((3,3),np.unit8)
    #dilation = cv2.dilate(opening, kernal, 3)
   # kel = np.ones((3,3),np.uint8)
    #ppl = cv2.erode(opening, kel)
    hsv = cv2.cvtColor(closing, cv2.COLOR_BGR2HSV)
    low_yellow = np.array([45, 40, 180])
    up_yellow = np.array([172, 111, 255])
    mask = cv2.inRange(hsv, low_yellow, up_yellow)
    
    #threshold = cv2.threshold(mask, 170, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(mask, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    if lines is not None:
      for line in lines:
         x1, y1, x2, y2 = line[0]
         x1=x1+r[0]
         y1=y1+r[1]
         x2=x2+r[0]
         y2=y2+r[1]
         m=(y2-y1)/(x2-x1)
         if m<0.283 and m>-0.5:
            continue
         cv2.line(orig_frame, (x1, y1), (x2, y2), (0, 0 , 225), 2)
    cv2.imshow("mask", mask)
    cv2.imshow("orig_frame", orig_frame)
    cv2.imshow("edges", edges)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()
