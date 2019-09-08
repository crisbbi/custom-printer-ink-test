import pyautogui
import pytesseract
import re

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
screenshot = pyautogui.screenshot('test.png')
extractedText = pytesseract.image_to_data(screenshot)

filteredText = extractedText.replace("\t"," ")
filteredText = filteredText.replace("\n"," ")
extractedArray = filteredText.split(" ")
print(extractedArray)

if re.search("D.*test", extractedText):
    print("Match: " + str(re.search("D[^0-9]*test", extractedText)))