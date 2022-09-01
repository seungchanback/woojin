"""qr 코드 생성기
"""
import qrcode


def make_qrcode(data) -> dict:

    qrcode_setting = qrcode.QRCode(
        box_size=3
    )
    qrcode_setting.add_data(data)
    img = qrcode_setting.make_image(fit=True)
    img.save("./sample.png")
    return None

import pyzbar.pyzbar as pyzbar  # pip install pyzbar and brew install zbar

# 바코드 탐지하는 엔진 (바코드 및 QR코드 탐지)
def decode(image):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(image)

    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print(obj.data)
        
        str_qrcode_data = obj.data.decode('utf-8')
        qrcode_dict = eval(str_qrcode_data)

        print('Data : ',qrcode_dict)

    return decodedObjects

import cv2                      # pip install opencv-python

# make_barcode("name","category")
# im = cv2.imread('sample.png')
# decoded_object = decode(im)
# breakpoint()


