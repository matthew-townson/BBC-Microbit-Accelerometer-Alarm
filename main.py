#Accelerometer alarm for bbc micro:bit
#Created by Matthew Townson - https://mtownson.com

from microbit import button_a, button_b, pin_logo, sleep
import arm, armsequence, modeselect, music, renderer

print('To arm the system, press both buttons')

def main(x):
    while True:
        if pin_logo.is_touched():
            x = modeselect.changeMode(x)
            print('Mode',x,'enabled')
            displayMode = 0
            sleep(500)
            
        if x == 1:
            displayMode = 0

        else:
            displayMode = 1

        renderer.setDisplay('initialise', displayMode)
        
        if button_a.is_pressed() and button_b.is_pressed():
            armsequence.preArm(displayMode)
            arm.armed(displayMode)

renderer.setDisplay('initialise', 1)
music.play(['c:2','g'])
main(0)