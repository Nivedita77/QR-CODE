import qrcode
from PIL import Image

# URL to encode
url = "https://saiproperty.wixsite.com/saiproperty"

# Create QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # about 7% error can be corrected
    box_size=10,  # size of each box in the QR code
    border=4,  # thickness of the border (minimum is 4)
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("qrcode.png")

# Display the image
img.show()
