# # This Need Internet To Download Lip PIL IN CMD => pip install pillow
# # Fix The Path
from PIL import Image, ImageFilter

before   = Image.open("../Images/Data_Types_In_Python_2.jpg")
after   =  before.filter(ImageFilter.BoxBlur(2))
after.save("../Images/out.tmp")
