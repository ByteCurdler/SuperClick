import pynput, time, random
mc = pynput.mouse.Controller()

Key = pynput.keyboard.Key
CharToCode = pynput.keyboard.KeyCode.from_char
Button = pynput.mouse.Button

HOT_KEY =           Key.cmd
LEFT_CLICK_KEY =    CharToCode("c")
RIGHT_CLICK_KEY =   CharToCode("v")
STOP_KEY =          CharToCode("q")

is_hot_pressed =    False
is_left_active =    False
is_right_active =   False
is_stopped =        False

def on_press(key):
    global is_hot_pressed
    global is_left_active
    global is_right_active
    global is_stopped
    if key == HOT_KEY:
        is_hot_pressed = True
    elif key == LEFT_CLICK_KEY and is_hot_pressed:
        is_left_active = True
    elif key == RIGHT_CLICK_KEY and is_hot_pressed:
        is_right_active = True
    elif key == STOP_KEY and is_hot_pressed:
        is_stopped = True
        return False
            

def on_release(key):
    global is_hot_pressed
    global is_left_active
    global is_right_active
    if key == HOT_KEY:
        is_hot_pressed = False
        is_left_active = False
        is_right_active = False
    elif key == LEFT_CLICK_KEY:
        is_left_active = False
    elif key == RIGHT_CLICK_KEY:
        is_right_active = False
    
kl = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
kl.start()

while not is_stopped:
    if is_left_active:
        mc.press(Button.left)
        mc.release(Button.left)
    if is_right_active:
        mc.press(Button.right)
        mc.release(Button.right)
    time.sleep(0.009)
