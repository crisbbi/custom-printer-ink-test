import pyautogui
import pytesseract
import re

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
screenshot = pyautogui.screenshot('test.png')
extractedText = pytesseract.image_to_string(screenshot)
print(extractedText)

if re.search("D.*test", extractedText):
    print("Match: " + str(re.search("D.*test", extractedText)))