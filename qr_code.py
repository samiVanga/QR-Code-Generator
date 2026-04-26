import qrcode
from qrcode.constants import ERROR_CORRECT_H

def generate_qr():
    data = "https://github.com/samiVanga/QR-Code-Generator"

    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_advanced.png")

    print("✅ QR code generated and saved as qr_advanced.png")

if __name__ == "__main__":
    generate_qr()