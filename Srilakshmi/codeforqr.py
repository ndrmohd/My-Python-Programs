Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import qrcode
import pyqrcode
import png
details=input("enter name and age")
enter name and agesrilakshmi 21
code=qrcode.make(details)
code.save("mywr.png")
code.save("myqr.png")
