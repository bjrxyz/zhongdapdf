
from reportlab.pdfgen import canvas
from PIL import ImageGrab
from reportlab.lib.utils import ImageReader
import win32api
import time


def checkBlank(image,imageSize):
    for y in range(imageSize[1]):
        for x in range(imageSize[0]):
            pixel=image.getpixel((x, y))
            if pixel!=(255,255,255):
                return False
    return True

workpath="F:/zhongda/"
wait=10
print("PDF自动截图将在"+str(wait)+"秒后开始，请做好准备！！！")
time.sleep(wait)
totalCount = 15
count=1
print("PDF自动截图开始：总共截图"+str(totalCount)+"页")
imagePos=(534,134,1565,976)
temp=ImageGrab.grab(imagePos)
imageSize=temp.size
pdf = canvas.Canvas(workpath+"pdf.pdf", imageSize)
currentHeight=0
while count<=totalCount:
    while True:
        image = ImageGrab.grab(imagePos)
        if not checkBlank(image,imageSize):
            break

    image.save(workpath+'image/'+str(count)+'.jpg')
    win32api.keybd_event(34,0,0,0)  #pagedown键位码是34
    pdf.drawImage(ImageReader(image),0,0)  
    pdf.showPage()  
    print("截图:"+str(count)+"页")
    count=count+1
    time.sleep(0.5)
pdf.save()