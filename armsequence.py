from microbit import sleep
import music, renderer

def preArm(displayMode):
    music.set_tempo(bpm=60)
    print('Arming system...')
    print(5)
    renderer.setDisplay('armStage1', displayMode)
    music.play(['c5'])
    print(4)
    renderer.setDisplay('armStage2', displayMode)
    music.play(['c5'])
    print(3)
    renderer.setDisplay('armStage3', displayMode)
    music.play(['c5'])
    print(2)
    renderer.setDisplay('armStage4', displayMode)
    music.play(['c5'])
    print(1)
    renderer.setDisplay('armStage5', displayMode)
    music.play(['c5'])
    sleep(100)
    music.set_tempo(bpm=120)