#arming warning sequence
from microbit import sleep
import countdown, music

def preArm(displayMode):
    music.set_tempo(bpm=60)
    print('Arming system...')
    countdown.selector(5, 1, 'armStageX', displayMode)
    sleep(100)
    music.set_tempo(bpm=120)