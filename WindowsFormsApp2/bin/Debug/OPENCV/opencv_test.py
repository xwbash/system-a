import cv2
import numpy as np
import sys
#kamera = cv2.VideoCapture(0)
kamera = cv2.VideoCapture(0)#http://192.168.1.107:8080/video")
#ret,kare = kamera.read()
a = open("selam.txt","w+")
while True:
	ret,kare = kamera.read()
	heart = cv2.CascadeClassifier("OPENCV/kalp.xml")
	lung = cv2.CascadeClassifier("OPENCV/ciger.xml")
	brain = cv2.CascadeClassifier("OPENCV/beyin.xml")
	gri_ton = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
	lungs =  lung.detectMultiScale(gri_ton,1.2,2)
	hearts = heart.detectMultiScale(gri_ton,1.2,2)
	brains = brain.detectMultiScale(gri_ton,1.3,2)
	for (x,y,w,h) in brains:
		a.write("brain##QRCODE")
		cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),2)
		sys.exit()
	for (x,y,w,h) in hearts:
		a.write("heart##QRCODE")
		cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),2)
		sys.exit()
	for (x,y,w,h) in lungs:
		a.write("lungs##QRCODE")
		cv2.rectangle(kare,(x,y),(x+w,y+h),(25,0,255),2)
		sys.exit()
	cv2.imshow("ekran",kare)
	if cv2.waitKey(1) == 60:
    	 break

#kamera.release()
