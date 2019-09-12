
from reportlab.pdfgen import canvas
from PIL import ImageGrab
from reportlab.lib.utils import ImageReader
import win32api
import time


workpath="F:/zhongda/"
wait=10
print("PPT自动截图将在"+str(wait)+"秒后开始，请做好准备！！！")
time.sleep(wait)
totalCount = 14
count=1
print("PPT自动截图开始：总共截图"+str(totalCount)+"页")
temp=ImageGrab.grab((315,209,1581,915))
imageSize=temp.size
pdf = canvas.Canvas(workpath+"ppt.pdf", imageSize)
currentHeight=0
while count<=totalCount:
    image = ImageGrab.grab((315,209,1581,915))
    image.save(workpath+'image/'+str(count)+'.jpg')
    win32api.keybd_event(34,0,0,0)  #pagedown键位码是34
    pdf.drawImage(ImageReader(image),0,0)  
    pdf.showPage()  
    print("截图:"+str(count)+"页")
    count=count+1
    time.sleep(0.5)
pdf.save()