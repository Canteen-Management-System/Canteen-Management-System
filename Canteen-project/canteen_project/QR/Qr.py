import json
import qrcode
from PIL import Image, ImageDraw
# from qrtools import QR
# import cv2
# from pyzbar.pyzbar import decode



# def Create_QR():
with open('canteen_project/QR/student.json','r') as f:
    datajson = json.load(f)
    # print(datajson)
    for i in datajson['student']:
      qrc = qrcode.make(i)
      qrc.save('canteen_project/QR/img/MyQRCode1.png')

# with open('canteen_project/QR/student.json','r') as f:
#     datajson = json.load(f)
#     count = 1
#     for i in datajson['student']:
      
#       qrc = qrcode.make(i)
#       path = (f'canteen_project/QR/ImgQr/MyQRCode{count}.png')
#       qrc.save(path)
#       count +=1

# def Read_QR(): 
#  myCode = QR(filename="canteen_project/QR/ImgQr/MyQRCode1.png")
#  if myCode.decode():
#   print (myCode.data)
#   print (myCode.data_type)
#   print (myCode.data_to_string())