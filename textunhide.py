from mainFile import mainFile
import cv2.cv as cv
import sys  

im = cv.LoadImage("res.png")
steg = mainFile(im)
print "Text value:",steg.unhideText()
