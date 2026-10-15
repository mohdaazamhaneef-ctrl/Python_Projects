import qrcode
url=input("Enter URL to make QR: ")

if url.startswith("http://") or url.startswith("https://"):
    qr=qrcode.make(url)
    qr.save("FristQR.png")
    print("QR Code Generated")
else:
    print("URL not valid")
