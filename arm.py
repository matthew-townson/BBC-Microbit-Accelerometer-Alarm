#system armed logic
from microbit import pin_logo, accelerometer, sleep, display, Image
import countdown, music, renderer

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
    renderer.setDisplay('armedWait', displayMode)
    music.play(['c3:2','c'])
    while True:
        if pin_logo.is_touched():
            disarm()
            break
        if (abs(accelerometer.get_strength())-1000) > 125:
            print('Motion detected, beginning countdown')
            countdown.selector(3, 0, 'countdownX', displayMode)
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