#switches between high and low power mode
import music, renderer

def changeMode(x):
    if x == 0:
        #display minimal
        x = x + 1
        renderer.setDisplay('initialise', 0)
        music.play(['e:2','e:2'])
        return x
    elif x == 1:
        #default
        x = 0
        renderer.setDisplay('initialise', 1)
        music.play(['c:2','g'])
        return x
    else:
        x = 0
        return x