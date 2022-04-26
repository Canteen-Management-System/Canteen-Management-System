
from PIL import Image, ImageDraw
import json 
# from qrtools import QR
import qrcode
import cv2
import os
import pyzbar.pyzbar as pyzbar 

class Qr():
    @staticmethod
    def Create_Qr():

        with open('Student_info.json', 'r') as f:
            data=json.load(f)
            for i in data:
                a=i['id']
                qrc = qrcode.make(a)
                qrc.save(f'canteen_project/imgQr/{a}.png')

    @staticmethod
    def Read_Qr(path):
        

        
                image = cv2.imread(path)
                detect = cv2.QRCodeDetector()
               
                data , vertices_array , binary_qrcode = detect.detectAndDecode(image)
                if vertices_array is not None:
                    DataQr = data
                    print(DataQr)
                    return(DataQr)
                else :
                    print('There is some Error')
            
    
    # def Scan_Qr():
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# camera = True
# while camera == True :
#     success,frame = cap.read()
#     for code in decode(frame):
#         print(code.type)
#         print(code.data.decode('utf-8'))
#         cv2.imshow('Testing',frame)
#         cv2.waitKey(1)


        
            
           


if __name__ == '__main__':
    Qr.Read_Qr('canteen_project/imgQr/2022450.png')
    Qr.Create_Qr()
    # Qr.Scan_Qr()
