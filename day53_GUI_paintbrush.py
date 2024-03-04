# Create a program that allows users to draw on a canvas using a GUI

import cv2 as cv
import numpy as np

# Tutorial: https://docs.opencv.org/4.x/db/d5b/tutorial_py_mouse_handling.html

####################################
# draw curve of small circles by dragging mouse
####################################

# mouse callback function
def draw_circle(event,x,y,flags,param):
    # take global variables:
    global ix,iy,drawing,mode
    # if the user presses the mouse: start drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    # if the mouse moves and the button is pressed: continue adding cricles
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(img,(x,y),5,(0,0,255),-1)
    # if buton is unpressed: stop drawing but still add a circle
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img,(x,y),5,(0,0,255),-1)

# initiate
drawing = False # true if mouse is pressed
ix,iy = -1,-1 #initial coordinates
# make a black window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF

    # close window on pressing Esc:
    if k == 27:
        break
cv.destroyAllWindows()
