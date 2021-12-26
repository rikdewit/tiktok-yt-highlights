from PIL import Image, ImageFilter

OriImage = Image.open('thumnb.png')
boxImage = OriImage.filter(ImageFilter.GaussianBlur(6))
boxImage.show()