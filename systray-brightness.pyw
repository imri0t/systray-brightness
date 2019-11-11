from infi.systray import SysTrayIcon
import subprocess

b = 0

def bri_100(systray):
    '''brightness: 100%'''
    b = 100
    screen_brightness()

def bri_75(systray):
    '''brightness: 75%'''
    b = 75
    screen_brightness()

def bri_50(systray):
    '''brightness: 50%'''
    b = 50
    screen_brightness()

def bri_25(systray):
    '''brightness 25%'''
    b = 25
    screen_brightness()

def bri_0(systray):
    '''brightness: 0%'''
    b = 0
    screen_brightness()

def screen_brightness():
    '''screen brightness assignment'''
    #not sure if possible yet
    #will continue looking
    subprocess.Popen(["$b={};(gwmi -n root\\wmi -cl WmiMonitorBrightnessMethods).WmiSetBrightness(5, $b)".format(b)])


def restart():
    '''restarts program'''
    systray.start()

menu = (("brightness: 100%", None, bri_100), 
                ("brightness: 75%", None, bri_75),  
                ("brightness: 50%", None, bri_50), 
                ("brightness: 25%", None, bri_25), 
                ("brightness: 0%", None, bri_0))

systray = SysTrayIcon("icon.ico", "brightness", menu)

systray.start()
