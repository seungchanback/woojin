import streamlit as st
import cv2
import numpy as np
from box import decode
from make_barcode import make_qrcode

page_title = "✨ QR 코드 생성"
st.set_page_config(page_title=page_title, page_icon="✨", layout="centered")
st.title(page_title)

item_append, box_append, package,qr_code  = st.tabs(["✨ 상품 QR 생성", "📦 박스 QR 생성", "🎁 상품 포장하기", "🖍 QR 코드 인식"])

with item_append:
    with st.form("상품_추가"):
        cols = st.columns((1,1))
        name = cols[0].text_input("상품이름 : ")
        category = cols[1].selectbox(
            label="상품 카테고리",
            options=[
                "그림",
                "폭스바겐",
                "자전거"
                ])
        selected_date = st.date_input("상품 추가일자")
        cols = st.columns(3)
        width = cols[0].text_input("가로 : ")
        depth = cols[1].text_input("세로 : ")
        height = cols[2].text_input("높이 : ")
        submitted = st.form_submit_button(label="QR 생성")
        data = {
            'item_code' : 'sample',
            'name' : name,
            'category' : category,
            'width' : width,
            'depth' : depth,
            'height' : height
        }

        if submitted:
            make_qrcode(data)
            st.text(f"""
                *** 아래 데이터에 대한 바코드가 생성되었습니다. ***
                {data}
                """)
            st.image('./sample.png')

with box_append:
    with st.form("박스_추가"):
        
        name = st.text_input("박스이름 : ")
        selected_date = st.date_input("박스추가일자")
        cols = st.columns(3)
        width = cols[0].text_input("가로 : ")
        depth = cols[1].text_input("세로 : ")
        height = cols[2].text_input("높이 : ")
        submitted = st.form_submit_button(label="QR 생성")
        data = {
            'item_code' : 'sample',
            'name' : name,
            'category' : category,
            'width' : width,
            'depth' : depth,
            'height' : height
        }

        if submitted:
            make_qrcode(data)
            st.text(f"""
                *** 아래 데이터에 대한 바코드가 생성되었습니다. ***
                {data}
                """)
            st.image('./sample.png')

with package:
    with st.form("상품포장하기"):
        options = st.multiselect(
            '포장할 상품을 클릭하세요',
            ['item1', 'item2', 'item3', 'item4'])

       
        submitted = st.form_submit_button(label="적합한 박스 찾기")
        if submitted:
            st.write('You selected:', options)

with qr_code:
    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is not None:
        # To read image file buffer with OpenCV:
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

        # Check the shape of cv2_img:
        # Should output shape: (height, width, channels)
        st.write(cv2_img.shape)
        detected_dict = decode(cv2_img)
        
        if detected_dict == "{}":
            st.write("QR 코드가 인식되지 않았습니다 🔴")
        else:
            st.write("QR 코드가 인식되었습니다 🟢")
            st.write(detected_dict)
