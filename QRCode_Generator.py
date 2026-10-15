# Create QR Code
import qrcode
url=input("Enter URL to make QR: ")

#Create QR Code
if url.startswith("http://") or url.startswith("https://"):
    qr=qrcode.make(url)
    qr.save("FristQR.png")
    print("QR Code Generated")
else:
    print("URL not valid")


#QR Code 
import qrcode
data=input("Enter Number to Make QR: ")
qr=qrcode.make(data) #qrcode

qr.save("FristQR_2026_MCA.png") #pillow

print("QR Code Generated")


#QR Code Generator
import qrcode
data=input("Enter Number to Make QR: ")
if url.startswith("http://") or url.startswith("https://"):
    qr=qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CONNECT_H,
                    box_size=10,
                    border=4
                    )
    qr.add_data(url)
    qr.make()

    image=qr.make_image(fill_color="blue", back_color="red")
    image.save("ThirdQR.png")

else:
    print("Invalid Url...!!! Must start with http or https")


#Create QR Code for UPI with specific Amount
import qrcode
upi_id=input("Enter UPI ID: ")
name=input("Enter Name: ")
amount=int(input("Enter Amount: "))

upi_url=f"upi://pay?pa={upi_id}&pn={name}&am={amount}"

qr=qrcode.make(upi_url)
qr.save("Aazam_UPI_1.png")

print("UPI QR Generated")