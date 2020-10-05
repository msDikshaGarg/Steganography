from mainFile import mainFile
import cv2.cv as cv
import sys
str = "Hello World"
carrier = cv.LoadImage("maxresdefault.jpg")

steg = mainFile(carrier)
steg.hideText(str)
steg.saveImage("res.png") #Image that contain datas

