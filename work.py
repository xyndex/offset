import mouse, time, keyboard

while True:
    keyboard.wait('caps lock')

    start_position = mouse.get_position()

    mouse.double_click()

    time.sleep(0.12)

    mouse.move( 765, 190 )
    mouse.click()

    time.sleep(0.12)

    mouse.move( 841, 190 )
    mouse.click()

    time.sleep(0.12)

    mouse.move( 545, 330 )
    mouse.click()

    time.sleep(0.12)

    mouse.move( 335, 236 )
    mouse.click()

    time.sleep(0.12)

    mouse.move( 335, 236 )
    mouse.double_click()

    time.sleep(0.12)

    mouse.move( 1150, 632 )
    mouse.click()