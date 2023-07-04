import qrcode

def generate_qrcode(data, filename):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)

data = input("Enter the link to encode as a QR code: ")
filename = input("Enter the file name with extension(png,jpeg): ")

generate_qrcode(data, filename)
