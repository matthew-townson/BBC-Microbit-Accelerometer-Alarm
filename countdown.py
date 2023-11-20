#countdown loops
from microbit import sleep
import music, renderer

def selector(x, sound, renderImage, displayMode):
    for i in range(x):
        renderImage = renderImage[:-1] + str (i+1)
        print(i+1)
        renderer.setDisplay(renderImage, displayMode)
        if sound == 1:
            music.play(['c5'])
        elif sound == 0:
            sleep(1000)
