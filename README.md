# Typing-Robot
<H3>Problem Statement:-To develop a robot to be able to type a given alpha-numeric sequence autonomously.There will be two types of keyboards</H3>

<H2>Key board specification:</H2>
<br>
<H4>Type 1:</H4>

<li>Each key is of size (5cmX5cm)</li>
<li>There will be a 1cm gap in between the keys</li>
<li>There would be 16 total keys in the keyboard</li>
<li>The keys are black in color with the character in white color</li>
<li>The gaps can be of any color</li>
<br>
<H4>Type 2:</H4>

<li>Each key is of size (4cmX4cm)</li>
<li>There will be a 1cm gap in between the keys</li>
<li>There would be 24 total keys in the keyboard</li>
<li>The keys are black in color with the character in white color</li>
<li>The gaps can be of any color</li>
 <br>
<H2>Solution</H2>
  <br>

https://user-images.githubusercontent.com/97799598/227696134-cd46ca04-2180-44d1-9945-973e23f56c74.mp4


<H4>Steps Involved:</H4>
<H4>Computer Vision</H4>
<li>Detecting all the contours in the image</li>
<li>Finding the area range in which our keys lie</li>
<li>Cropping out each key</li>
<li>processing each key and sending it for recognition</li>
<li>Scaling the pixel coordinates to the world coordinates</li>
<li>Extracting coordinates of our sequence and converting to G-code</li>
  <br>
<H4>Arduino<H4>

<li>Receiving the coordinates and storing in a .txt file</li>
<li>Running a loop to execute all the lines of the text file</li>
<li>Sending G-code to arduino serial monitor using pyserial</li>
