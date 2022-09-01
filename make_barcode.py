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



