import streamlit as st

def search_best_box():
    """상품 포장 시 최적의 박스를 찾아주는 기능
    """
        
    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is not None:
        # To read image file buffer as bytes:
        bytes_data = img_file_buffer.getvalue()
        # Check the type of bytes_data:
        # Should output: <class 'bytes'>
        st.write(type(bytes_data))