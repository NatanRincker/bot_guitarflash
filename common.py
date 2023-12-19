
import win32api
import win32con
from time import sleep
VK_CODE = {
    '1': 0x31,
    'a': 0x41,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    's': 0x53,
    'spacebar': 0x20,
}

def pressHoldRelease(key, hold_time = .015):
    win32api.keybd_event(VK_CODE[key], 0, 0, 0)
    sleep(hold_time)
    win32api.keybd_event(VK_CODE[key], 0, win32con.KEYEVENTF_KEYUP, 0)