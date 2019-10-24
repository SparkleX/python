import cv2
import pytesseract 
from PIL import Image,ImageDraw,ImageFont
import numpy as np

watch_cascade = cv2.CascadeClassifier('./cascade.xml')

image = cv2.imread("car1.jpg")

resize_h = 1000
height = image.shape[0]
scale = image.shape[1]/float(image.shape[0])
image = cv2.resize(image, (int(scale*resize_h), resize_h))

image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
watches = watch_cascade.detectMultiScale(image_gray, 1.1, 2, minSize=(36, 9), maxSize=(36*40, 9*40))

print("检测到车牌数", len(watches))
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)
    cropImg = image[y:y+h,x:x+w]
    cropImg = cv2.cvtColor(cropImg, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(cropImg, lang="chi_sim", config="--psm 7")
#    cv2.putText(image, text, (x,y), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 255, 0), 12)
    cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)
    font = ImageFont.truetype("simhei.ttf", 64, encoding="utf-8")
    draw.text((x, y+h), text, (255, 0, 0), font=font)
    image = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    print(text)

cv2.imshow("image", image)
cv2.imwrite("out.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()