import pyautogui as p
#import selenium.webdriver as webdriver
import time
import pyperclip as clip
import pymsgbox as msg
"""
#driver = webdriver.Firefox()

#def abrirNav():
#    driver.get('https://www.issdigitalthe.com.br/nfse/')
"""

def formata(s):
    return s.replace('.','*').replace(',','.').replace('*',',')

def iniciar():
    time.sleep(0.2)
    p.click(x=350,y=580)
    time.sleep(3)
    p.press('end')
    time.sleep(2)
    p.click(x=360,y=580)
    time.sleep(2)
    p.press('pagedown')
    p.press('down',presses=2)

def finalizar():
    time.sleep(1)
    p.hotkey('ctrl','shift','tab')
    p.hotkey('ctrl','w')

def importa(data):
    num = ""
    time.sleep(0.5)
    try:
        xi,yi = p.locateCenterOnScreen('data_inicio.png')
        time.sleep(3)
        p.click(x = xi + 130,y = yi)
    except:
        msg.alert(KeyError,'','ok')
    #p.click(x= 715,y= 157) #posição do campo de data inicial
    p.write(data)
    p.press('tab')
    p.write(data)
    time.sleep(0.5)

    try:
        x1,y1 = p.locateCenterOnScreen('consultar_pdf.png')
        time.sleep(1)
        p.click(x=x1,y=y1)
    except:
        msg.alert("Incapaz de consultar pdf",'','ok')
    time.sleep(3)
    p.hotkey('ctrl','f')
    time.sleep(1)
    p.write('total geral')
    time.sleep(2)
    try:
        x1,y1 = p.locateCenterOnScreen('total_geral.png',confidence=0.9)
        p.click(x=x1 + 410,y=y1,clicks=3)
        time.sleep(1)
        p.hotkey('ctrl','c')
        num = clip.paste()
    except:
        print('Total geral nao consta!')
        num = '0,0'
        
    p.hotkey('ctrl','tab')
    p.write(formata(num))
    p.press('enter')
    time.sleep(1)
    
    
    
    


