from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('GetCapchar.jpg'))
print(text)
