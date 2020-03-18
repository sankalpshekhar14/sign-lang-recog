# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:29:45 2020

REQUIREMENTS:-
Hey Sankalp, for now I have not enabled any form of Hand symbol recognition.
You need to press 's' (on keyboard) for conversion and capture of 28x28 image conversion.
One would require DLIB for image recognition, on which I am working.
Here is the basic code or skeleton of our project for detection purposes only. 
"""

import cv2

key = cv2. waitKey(1)
cam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = cam.read()
        print(check) #prints true as long as the cam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        
        if key == ord('s'):  #Keyboard input 's' saves an image 
            cv2.imwrite(filename='new_gray_saved_img.jpg', img=frame)
            cam.release()
            img_new = cv2.imread('new_gray_saved_img.jpg', cv2.IMREAD_GRAYSCALE) #Read and grayscale conversion
            img_new = cv2.imshow("Captured Image", img_new) #Show image
            cv2.waitKey(1650) #sleep functionality equivalent
            cv2.destroyAllWindows()
            
            print("Processing image...")
            img_ = cv2.imread('new_gray_saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='gray_saved_img-final.jpg', img=img_)
            print("Image saved!")
            break
        
        elif key == ord('q'):
            print("Turning off camera.")
            cam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        cam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break