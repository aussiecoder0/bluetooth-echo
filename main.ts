bluetooth.onBluetoothConnected(function () {
    basic.showLeds(`
        . . # # #
        . # . . .
        # . . . .
        . # . . .
        . . # # #
        `)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showLeds(`
        # # # . .
        # . . # .
        # . . . #
        # . . # .
        # # # . .
        `)
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    uartdata = "" + bluetooth.uartReadBuffer()
    basic.showString(uartdata)
    if (uartdata.includes("NORTH")) {
        basic.showArrow(ArrowNames.North)
    }
})
let uartdata = ""
basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    `)
bluetooth.startAccelerometerService()
bluetooth.startButtonService()
bluetooth.startLEDService()
bluetooth.startTemperatureService()
bluetooth.startMagnetometerService()
basic.showLeds(`
    . . # . .
    . . # . .
    # # # # #
    . . # . .
    . . # . .
    `)
