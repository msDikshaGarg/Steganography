from mainFile import mainFile
import cv2.cv as cv
import sys
    
inp = cv.LoadImage("resultindex.png")
steg = mainFile(inp)
dec = steg.unhideImage()
cv.SaveImage("recovered.png", dec) #Image retrieve into the other image

