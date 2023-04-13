import pyautogui as p
import time
import pymsgbox as msg
p.hotkey('alt','tab')
time.sleep(2)
"""
try:
    xi,yi = p.locateCenterOnScreen('consultar_pdf.png')
    time.sleep(1)
    p.click(x = xi,y = yi)
except:
    msg.alert(KeyError,'','ok')
"""
p.typewrite('0.0')
p.press('enter')