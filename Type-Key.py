import cv2 as cv
import pytesseract 
import serial
import time
import numpy as np

def preprocess_predict(img):
  #Function for processing the image to be sent to tesseract for predicting

  #Resizing image
  img=cv.resize(img,(512,512),interpolation=cv.INTER_AREA)

  blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)

  _,thresh=cv.threshold(blur,110,255,cv.THRESH_BINARY) #Converting all pixels below 110 to black else white

  #Inverting Pixel values 
  img=cv.bitwise_not(thresh) #Converting to white alphabet/number over black background to black alphabet over white background 

  return img

def preprocess(img):
  #This function threshold the image over our given color range

  img = cv.imread("img1.jpg")

  img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

  lower = np.array([0, 0, 0])
  upper = np.array([179, 179, 115])

  mask = cv.inRange(img_hsv, lower, upper)

  mask_blur = cv.GaussianBlur(mask, (5, 5), 1)

  _, thresh = cv.threshold(mask_blur, 200, 255, cv.THRESH_BINARY)

  contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
  return contours,thresh


def scaling_factor(img):

  #Function to calculate the scaling factor 

  pixel_length=img.shape[1]

  scale=pixel_length/5

  return scale

def draw_rectangle(img,box_values):

  # Function to draw rectangle over the identified sections
  hImg,wImg,channel=img.shape
  
  x,y,w,h=box_values

  cv.rectangle(img,(x,y),((x+w),(y+h)),(0,0,255),thickness=2)


def predict(img):
  
  coordinates=pytesseract.image_to_boxes(img,config=('--psm 7 --oem 3 tessedit_char_whitelist= 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ tessedit_char_blacklist", "#@!&*()!"":;,./?><}{][|'
  ))

  return coordinates



#--------------------------------------------------------------MAIN CODE---------------------------------------------------------------------------------------

str=input("ENTER STRING:")

# cap=cv.VideoCapture('http://100.78.54.51:8080/video')

# result,i=cap.read()

# copy_original=i

# i=cv.resize(i,(640,420),interpolation=cv.INTER_CUBIC)

# if result:
#   cv.imwrite('img1.jpg',i)


image=cv.imread('img1.jpg')
copy=image

contours,thresh1=preprocess(image)

cnt1=max(contours, key=cv.contourArea)

x,y,w,h=cv.boundingRect(cnt1)

single=image[y:y+h,x:x+w]

scale=scaling_factor(single)

j=0

all_locations={}


for cnt in contours:
  area=cv.contourArea(cnt)

  if area>2000 and area<4000: #For my cast the contour area of the keys lied between 2000 and 4000

    x,y,w,h=cv.boundingRect(cnt)

    cropped=image[y:y+h,x:x+w]

    img=preprocess_predict(cropped)

    prediction=predict(img)
    print(area,prediction)

    draw_rectangle(copy,(x,y,w,h))

    x/=(scale)
    y/=(scale)

    x*=10
    y*=10

    x-=55
    y-=15

    x=round(x,2)
    y=round(y,2)

    val= prediction.split(' ')

    if val[0]=='|':
      val[0]=='I'
    
    val[0]=val[0].upper()

    all_locations[val[0]]=(x,y,w,h)


    cv.imshow('img',copy)
    cv.waitKey(0)
    

wanted_locations=[]

for a in str:

  for key in all_locations:

    if a==key:
      wanted_locations.append(all_locations[key])

f=open('grbl.gcode.txt','a')

for location in wanted_locations:

  x,y,w,h=location
  f.write("G1 X{} Y{} F2000\n".format(x,y))

  f.write("M3 S90\n")

  f.write("M5\n")

f.close()

print(all_locations)

print(wanted_locations)


#-------------------------------------------------------------------ARDUINO CODE-------------------------------------------------------------------


s = serial.Serial('COM5',115200)

# Open g-code file
f = open(r'grbl.gcode.txt','r')

# Wake up grbl
s.write("\r\n\r\n".encode('utf-8'))

time.sleep(3)   # Wait for grbl to initialize 

s.flushInput()  # Flush startup text in serial input

# Stream g-code to grbl
for line in f:
    l = line.strip() # Strip all EOL characters for consistency

    print('Sending: ' + l,)

    if l=='M5':
      time.sleep(2)

    s.write((l + '\n').encode('utf-8')) # Send g-code block to grbl

    grbl_out = s.readline() # Wait for grbl response with carriage return

    print (grbl_out.strip())

    time.sleep(0.25)
