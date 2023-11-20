#Accelerometer alarm for bbc micro:bit
#Created by Matthew Townson - https://mtownson.com

from microbit import *
import music, speech

print('To arm the system, press both buttons')

def setDisplay(image, mode):
    if (image == 'initialise') and mode == 1:
        display.show(Image('00000:00009:00090:90900:09000'))

    elif (image == 'initialise') and mode == 0:
        display.show(Image('00000:00005:00050:50500:05000'))

    elif (image == 'armStage1') and mode == 1:
        display.show(Image('90000:90000:90000:90000:90000'))

    elif (image == 'armStage1') and mode == 0:
        display.show(Image('00000:00000:00000:00000:90000'))
    
    elif (image == 'armStage2') and mode == 1:
        display.show(Image('99000:99000:99000:99000:99000'))

    elif (image == 'armStage2') and mode == 0:
        display.show(Image('00000:00000:00000:00000:99000'))
    
    elif (image == 'armStage3') and mode == 1:
        display.show(Image('99900:99900:99900:99900:99900'))

    elif (image == 'armStage3') and mode == 0:
        display.show(Image('00000:00000:00000:00000:99900'))
    
    elif (image == 'armStage4') and mode == 1:
        display.show(Image('99990:99990:99990:99990:99990'))

    elif (image == 'armStage4') and mode == 0:
        display.show(Image('00000:00000:00000:00000:99990'))
    
    elif (image == 'armStage5') and mode == 1:
        display.show(Image('99999:99999:99999:99999:99999'))

    elif (image == 'armStage5') and mode == 0:
        display.show(Image('00000:00000:00000:00000:99999'))
    
    elif (image == 'armedWait') and mode == 1:
        display.show(Image('09990:90009:97979:90009:09990'))

    elif (image == 'armedWait') and mode == 0:
        display.show(Image('00000:00000:00000:00000:55555'))

    elif (image == 'countdown1') and mode == 1:
        display.show(Image('99900:99000:90000:00000:00000'))
        
    elif (image == 'countdown1') and mode == 0:
        display.show(Image('55500:55000:50000:00000:00000'))
        
    elif (image == 'countdown2') and mode == 1:
        display.show(Image('99999:99999:99990:99900:99000'))
        
    elif (image == 'countdown2') and mode == 0:
        display.show(Image('55555:55555:55550:55500:55000'))
    
    elif (image == 'countdown3') and mode == 1:
        display.show(Image('99999:99999:99999:99999:99999'))

    elif (image == 'countdown3') and mode == 0:
        display.show(Image('55555:55555:55555:55555:55555'))

def changeMode(x):
    if x == 0:
        #display minimal
        x = x + 1
        setDisplay('initialise', 0)
        music.play(['e:2','e:2'])
        return x
    elif x == 1:
        #default
        x = 0
        setDisplay('initialise', 1)
        music.play(['c:2','g'])
        return x
    else:
        x = 0
        return x

def preArm(displayMode):
    music.set_tempo(bpm=60)
    print('Arming system...')
    print(5)
    setDisplay('armStage1', displayMode)
    music.play(['c5'])
    print(4)
    setDisplay('armStage2', displayMode)
    music.play(['c5'])
    print(3)
    setDisplay('armStage3', displayMode)
    music.play(['c5'])
    print(2)
    setDisplay('armStage4', displayMode)
    music.play(['c5'])
    print(1)
    setDisplay('armStage5', displayMode)
    music.play(['c5'])
    sleep(100)
    music.set_tempo(bpm=120)

def disarm():
    music.stop()
    print('System disarmed, to rearm, press both buttons')
    music.play(['c5:2','c4'])

def alert():
    for p in range(100,1000):
        music.pitch(p)
        sleep(1)
        music.stop()
        
def armed(displayMode):
    print('System armed, to deactivate, touch logo')
    setDisplay('armedWait', displayMode)
    music.play(['c3:2','c'])
    while True:
        if pin_logo.is_touched():
            disarm()
            break
        if (abs(accelerometer.get_strength())-1000) > 125:
            print('Motion detected, beginning countdown\n3')
            setDisplay('countdown1', displayMode)
            sleep(1000)
            print('2')
            setDisplay('countdown2', displayMode)
            sleep(1000)
            print('1')
            setDisplay('countdown3', displayMode)
            sleep(1000)
            if pin_logo.is_touched():
                alarm = 0
                disarm()
                break
            print('Alarm activated')
            alarm = 1
            display.show(Image.ANGRY)
            while alarm == 1:
                alert()
                if pin_logo.is_touched():
                    alarm = 0
                    disarm()
                    break
            break

def main(x):
    while True:
        if pin_logo.is_touched():
            x = changeMode(x)
            print('Mode',x,'enabled')
            displayMode = 0
            sleep(500)
            
        if x == 1:
            displayMode = 0

        else:
            displayMode = 1

        setDisplay('initialise', displayMode)
        
        if button_a.is_pressed() and button_b.is_pressed():
            preArm(displayMode)
            armed(displayMode)

setDisplay('initialise', 1)
music.play(['c:2','g'])
main(0)
