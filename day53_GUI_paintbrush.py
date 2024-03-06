# Create a program that allows users to draw on a canvas using a GUI

import cv2 as cv
import numpy as np

# using openCV
# Tutorial: https://docs.opencv.org/4.x/db/d5b/tutorial_py_mouse_handling.html
# will not work in ipython notebook!
# use opencv pyenv

# others use tkinter

####################################
# draw curve of small circles by dragging mouse
####################################

# mouse callback function
def draw_circle(event,x,y,flags,param):
    # take global variables:
    global ix,iy,drawing,mode,r,g,b,size
    # if the user presses the mouse: start drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    # if the mouse moves and the button is pressed: continue adding cricles
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(img,(x,y),size,(r,g,b),-1)
    # if button is unpressed: stop drawing but still add a circle
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img,(x,y),size,(r,g,b),-1)

# initiate
drawing = False # true if mouse is pressed
ix,iy = -1,-1 #initial coordinates
# make a black window
#img = np.zeros((512,512,3), np.uint8)
# or a white one:
img = np.full((512,512,3),255, np.uint8)
cv.namedWindow('image')

##############################################
# add trackbar for color palette
##############################################

# it still requires callback - in this case, empty
def nothing(x):
    pass

cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
# trackbar for brush size selection
cv.createTrackbar('brush size', 'image', 1, 20, nothing)

cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF

    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    size = cv.getTrackbarPos('brush size', 'image')
    # close window on pressing Esc:
    if k == 27:
        break
cv.destroyAllWindows()
