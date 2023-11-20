from microbit import display, Image

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