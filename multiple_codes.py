import qrcode                                                                                           # type: ignore
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H          # type: ignore

data = "https://github.com/samiVanga/QR-Code-Generator"

levels = {
    "L": ERROR_CORRECT_L,
    "M": ERROR_CORRECT_M,
    "Q": ERROR_CORRECT_Q,
    "H": ERROR_CORRECT_H
}

for name, level in levels.items():
    qr = qrcode.QRCode(error_correction=level)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qr_{name}.png")

print("All QR codes generated!")

