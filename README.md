# Typing-Robot
Problem Statement:-To develop a robot to be able to type a given alpha-numeric sequence autonomously.There will be two types of keyboards

Key board specification:
Type 1:

Each key is of size (5cmX5cm)
There will be a 1cm gap in between the keys
There would be 16 total keys in the keyboard
The keys are black in color with the character in white color
The gaps can be of any color

Type 2:

Each key is of size (4cmX4cm)
There will be a 1cm gap in between the keys
There would be 24 total keys in the keyboard
The keys are black in color with the character in white color
The gaps can be of any color
Solution
Steps Involved:

Computer Vision
Detecting all the contours in the image
Finding the area range in which our keys lie
Cropping out each key
processing each key and sending it for recognition
Scaling the pixel coordinates to the world coordinates
Extracting coordinates of our sequence and converting to G-code
Arduino

Receiving the coordinates and storing in a .txt file
Running a loop to execute all the lines of the text file
Sending G-code to arduino serial monitor using pyserial
