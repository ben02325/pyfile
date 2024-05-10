import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


font = ImageFont.truetype('fonts/SCDream5.otf', 20)


while True:
 
  now = datetime.datetime.now()
  nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

  ret, frame = capture.read() 
  
  
  cv2.rectangle(img=frame, pt1=(10, 15), pt2=(340, 35), color=(0,0,0), thickness=-1)

  
  frame = Image.fromarray(frame)
  draw = ImageDraw.Draw(frame)
  
  draw.text(xy=(10, 15), text="CCTV Monitor"+nowDatetime, font=font, fill=(255, 255, 255))
  frame = np.array(frame)

  cv2.imshow("text", frame) 
  if cv2.waitKey(1) == ord('q'): 
    break

capture.release() 
cv2.destroyAllWindows() 


