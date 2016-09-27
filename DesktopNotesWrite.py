import os
import sys
import ctypes
import subprocess
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("Desktop_Clean.jpg")
f = open("DesktopTxt.txt")
tmp = 0
for line in f:
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font.ttf", 25)
    draw.text((25,tmp), line, (255,255,255),font=font)
    tmp = tmp+30
    print(line, end='')
img.save("DesktopNotes.jpg")
p = subprocess.Popen(["powershell.exe", "C:\\Users\\Home\\Desktop\\DesktopNotes\\DesktopNotesV2\\ChangeBackground.ps1"], stdout=sys.stdout)
p.communicate()
