
radio.set_group(23)

def on_button_pressed_a():
    radio.send_string("przud")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string("tyl")
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_pin_pressed_p0():
    radio.send_string("tyl")
    pass
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
def on_pin_pressed_p01():
    radio.send_string("skretwlewo")
    pass
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p01)