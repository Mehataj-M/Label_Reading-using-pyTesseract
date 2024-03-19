try:
  from PIL import Image
except Import_Error:
  import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def recText(filename):
  text=pytesseract.image_to_string(Image.open(filename))
  return text
info=recText('img1.jpg')
print(info)
file=open("result.txt",'a')
file.write(info)
file.close()
print("success")
