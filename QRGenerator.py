import pyqrcode

url=input("Enter URL to generate QR code: ")

qr_code=pyqrcode.create(url)
qr_code.svg('qrcode.svg', scale=5)