from mainFile import mainFile
import cv2.cv as cv
import sys
#imagetohide = cv.LoadImage("index.jpeg")
#carrier = cv.LoadImage("maxresdefault.jpg")
imagetohide = cv.LoadImage("mobile.jpg")
carrier = cv.LoadImage("image.jpg")
steg = mainFile(carrier)
steg.hideImage(imagetohide)
steg.saveImage("resultindex.png")

    
    

