input.onLoudSound(function () {
    light.setAll(0x000000)
})

input.onTemperatureConditionChanged(TemperatureCondition.Cold, 15, TemperatureUnit.Celsius, function () {
    light.setAll(0x0000ff)
})

input.onLightConditionChanged(LightCondition.Dark, function () {
    light.setAll(0x00ff00)
})

input.buttonsAB.onEvent(ButtonEvent.Click, function () {
    for (let i = 0; i < 4; i++) {
        light.setBrightness(130)
        light.showRing(
            `yellow yellow yellow yellow yellow yellow yellow yellow yellow yellow`
        )
        music.powerUp.play()
    }
})

input.onGesture(Gesture.TiltDown, function () {
    for (let i = 0; i < 4; i++) {
        light.showRing(
            `blue blue blue blue blue white white white white white`
        )
        music.baDing.play()
        light.clear()
    }
})

input.buttonB.onEvent(ButtonEvent.Click, function () {
    light.setAll(0xffffff)
    music.baDing.play()
})

input.onGesture(Gesture.Shake, function () {
    for (let i = 0; i < 4; i++) {
        light.showRing(
            `white purple white purple white white purple white purple white`
        )
        light.showRing(
            `purple white purple white purple purple white purple white purple`
        )
        music.playMelody("F G E C5 B D A C ", 120)
    }
})

let Start = 1

control.runInParallel(function () {
    if (Start == 1) {
        music.playMelody("E A D F E D E C ", 120)
        music.playMelody("C5 B A G F E D C ", 120)
        music.playMelody("C D E F G A B C5 ", 120)
        music.playMelody("C D E F G F E D ", 120)
        music.playMelody("C5 B A G F G A B ", 120)
    }
})
