import streamlit as st
from make_barcode import make_qrcode

page_title = "✨ QR 코드 생성"
st.set_page_config(page_title=page_title, page_icon="✨", layout="centered")
st.title(page_title)

item_append, box_append, package  = st.tabs(["✨ 상품 QR 생성", "📦 박스 QR 생성", "🎁 상품 포장하기"])

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
                ]
        )
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
        '포장할 상품을 고르세요',
        ['item1', 'item2', 'item3', 'item4'],
        ['item5', 'item6'])

        st.write('You selected:', options)

        
def item_table_append():
    """QR 인식 시 바코드 추가
    """
    pass

def search_best_box():
    """상품 포장 시 최적의 박스를 찾아주는 기능
    """
    pass