def on_bluetooth_connected():
    basic.show_leds("""
        . . # # #
                . # . . .
                # . . . .
                . # . . .
                . . # # #
    """)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_leds("""
        # # # . .
                # . . # .
                # . . . #
                # . . # .
                # # # . .
    """)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_uart_data_received():
    global uartdata
    uartdata = str(bluetooth.uart_read_buffer())
    basic.show_string(uartdata)
    if uartdata.includes("NORTH"):
        basic.show_arrow(ArrowNames.NORTH)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

uartdata = ""
basic.show_leds("""
    # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
""")
bluetooth.start_accelerometer_service()
bluetooth.start_button_service()
bluetooth.start_led_service()
bluetooth.start_temperature_service()
bluetooth.start_magnetometer_service()
basic.show_leds("""
    . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
""")