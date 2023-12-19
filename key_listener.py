
import time
import keyboard
    
def monitor_key(key):
    if keyboard.is_pressed(key):
        start = time.time()
        end = None
        while keyboard.is_pressed(key):
            pass
        end = time.time()
        print(key +','+ str(end-start))


while keyboard.is_pressed('1') == False:
    monitor_key('a')
    monitor_key('s')
    monitor_key('j')
    monitor_key('k')
    monitor_key('l')
