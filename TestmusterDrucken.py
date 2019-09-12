import win32ui
import win32api
import win32print
from PIL import Image, ImageWin

printer = "Canon MG5200 series Printer WS"
# file names must be absolute path so the task scheduler doesn't throw errors
pathToImageFile = "C:\\Users\\chris\\Documents\\custom-printer-ink-test\\imageColors.jpg"
pathToPDFFile = "C:\\Users\\chris\\Documents\\custom-printer-ink-test\\lorem-test.pdf"

'''
---------------------------------------------
Print image
Code is pretty much copy-pasted from 
http://timgolden.me.uk/python/win32_how_do_i/print.html#shellexecute
---------------------------------------------
'''
# Constants for GetDeviceCaps
# HORZRES / VERTRES = printable area
HORZRES = 8
VERTRES = 10

# LOGPIXELS = dots per inch
LOGPIXELSX = 88
LOGPIXELSY = 90

# PHYSICALWIDTH/HEIGHT = total area
PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111

# PHYSICALOFFSETX/Y = left / top margin
PHYSICALOFFSETX = 112
PHYSICALOFFSETY = 113

#  You can only write a Device-independent bitmap
#  directly to a Windows device context; therefore
#  we need (for ease) to use the Python Imaging
#  Library to manipulate the image.
#  Create a device context from a named printer
#  and assess the printable size of the paper.
hDC = win32ui.CreateDC()
hDC.CreatePrinterDC(printer)
printable_area = hDC.GetDeviceCaps(HORZRES), hDC.GetDeviceCaps(VERTRES)
printer_size = hDC.GetDeviceCaps(PHYSICALWIDTH), hDC.GetDeviceCaps(PHYSICALHEIGHT)
printer_margins = hDC.GetDeviceCaps(PHYSICALOFFSETX), hDC.GetDeviceCaps(PHYSICALOFFSETY)

#  Open the image, rotate it if it's wider than
#  it is high, and work out how much to multiply
#  each pixel by to get it as big as possible on
#  the page without distorting.
bmp = Image.open(pathToImageFile)
if bmp.size[0] > bmp.size[1]:
  bmp = bmp.rotate(90)

ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
scale = min(ratios)

#  Start the print job, and draw the bitmap to
#  the printer device at the scaled size.
hDC.StartDoc(pathToImageFile)
hDC.StartPage()

dib = ImageWin.Dib(bmp)
scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
x1 = int((printer_size[0] - scaled_width) / 2)
y1 = int((printer_size[1] - scaled_height) / 2)
x2 = x1 + scaled_width
y2 = y1 + scaled_height
dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))

hDC.EndPage()
hDC.EndDoc()
hDC.DeleteDC()
'''
---------------------------------------------
Print image
---------------------------------------------
'''

# Sources for GhostScript to print PDF
pathToGhostScript = "C:\\Users\\chris\\Documents\\GHOSTSCRIPT\\bin\\gswin32.exe"
pathToGSPrint = "C:\\Users\\chris\\Documents\\GSPRINT\\gsprint.exe"

# Choose either the default printer or hard-code the desired printer to use
#currentprinter = win32print.GetDefaultPrinter()
win32api.ShellExecute(0, 'open', pathToGSPrint, '-ghostscript "' + pathToGhostScript + '" -printer "' + printer + '" "' + pathToPDFFile, '.', 0)