radio.setGroup(23)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("przud")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("tyl")
})
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    radio.sendString("tyl")
    
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p01() {
    radio.sendString("skretwlewo")
    
})
