import pyautogui
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
screenshot = pyautogui.screenshot('test.png')
print(pytesseract.image_to_data(screenshot))