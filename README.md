# custom-printer-ink-test
A custom approach to automate the process of regular printing. This repo was (originally) created for a printer with edible ink. 

**Disclaimer: I don't guarantee anything for this content, code or the functionality and I'm not responsible for anything that might go wrong.**

The edible ink (in a compatible printer) should be used regularly, otherwise it dries up. When it is dry, further printing might damage the printer to the point where it's damaged permanently and thus not usable anymore. I've had personal experience with this and didn't want to keep track manually of that, so I wanted to somehow automate this process. I wanted to have a program that is automatically called by the OS and prints something to keep the ink "alive".

### Requirements:
* Python, works for me with v3.7.2, not tested any other version
* pywin32, enter `pip install pywin32` in your console
* Ghostscript, get it [here](http://www.mediafire.com/file/yf52p2izc57z456/GHOSTSCRIPT.rar/file)
* gsprint, get it [here](http://www.mediafire.com/file/h2dpmq2frtw5psu/GSPRINT.rar/file)
* Windows, don't know whether it works on Linux too

### Setup:
1. Install Python, if not already installed 
1. Install pywin32, if not already installed 
1. Unpack the Ghostscript and gsprint files and save the folders somewhere 
1. Open the batch file in an editor. Replace the location in the first string with the absolute path of your installed python.exe. The path must remain as a string. Same goes with the second string. Insert the absolute path of the PrinterInkTest python file in that second string.
1. Go to the PrinterInkTest python file. Replace the name inside the `printer` variable with your desired printer. In case, look up the name in your settings.
    1. (Optional): remove the `#` before `printer = win32print.GetDefaultPrinter()` to select your standard printer
1. Replace the location of `pathToImageFile` with the absolute path of the image file (imageColors.jpg) provided. Otherwise take the absolute path of any image you prefer (on your computer).
1. Replace the location of `pathToPDFFile` with the absolute path of the PDF file (lorem-ipsum.pdf) provided. Otherwise take the absolute path of any PDF you prefer (on your computer).

### Usage:
You can now go to the Windows task scheduler and create a new task that executes the batch file however you like.

### Some additional info:
I'm not an expert with printers. I have my own printer Canon MG 5200 which I successfully used for testing, without edible ink. I can't guarantee though that everything works on your printer or computer. I don't know much about Ghostscript, gsprint or anything related besides the commands I have put into the Python script, which I have put together by googling. The code that prints the image is almost copy pasted from the source (thanks to the author!), which is linked in the Python file. The absolute paths are necessary (at least they were for me) so that the task scheduler wouldn't throw any errors. 
