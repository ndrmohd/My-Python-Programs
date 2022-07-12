import qrcode
data='Aswin Kandanakam'
img=qrcode.make(data)
img.save('img.png')