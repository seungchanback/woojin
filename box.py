from pyzbar import pyzbar
import streamlit as st


def search_best_box():
    """QR 인식 시 바코드 추가
    """
    pass




def decode(image):
    # Find barcodes and QR codes
    print("hello")
    decodedObjects = pyzbar.decode(image)
    qrcode_dict = "{}"
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print(obj.data)
        
        str_qrcode_data = obj.data.decode('utf-8')
        qrcode_dict = eval(str_qrcode_data)

        print('Data : ',qrcode_dict)

    return qrcode_dict
