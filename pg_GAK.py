import pyautogui as pg
import time 

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')
pg.typewrite('bn.com\n',0.5)
time.sleep(5)

pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.typewrite('harry potter and the goblet of fire\n',0.5)
pg.moveTo(527,509,3)
pg.click()
pg.moveTo(836,694,3)
pg.click()



