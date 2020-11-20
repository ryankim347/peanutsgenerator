import pytesseract
from PIL import Image

print(pytesseract.image_to_string(Image.open('split/tpb-1_297_weekday_2.jpg')))