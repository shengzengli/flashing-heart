basic.forever(function () {
    basic.showString("shen")
    basic.showIcon(IconNames.Heart)
    basic.pause(1000)
    basic.clearScreen()
    kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Forward, 15)
})
