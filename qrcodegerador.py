import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
            version = 1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=6,
            )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save("qrcode.png")
url = input("Digite a página web para gerar QRCode: ")
generate_qrcode(url)
