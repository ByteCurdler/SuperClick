import pynput, time, random
mc = pynput.mouse.Controller()

Key = pynput.keyboard.Key
CharToCode = pynput.keyboard.KeyCode.from_char
Button = pynput.mouse.Button

HOT_KEY =   CharToCode("s")
CLICK_KEY = CharToCode("c")
STOP_KEY =  CharToCode("q")

is_hot_pressed =    False
is_combo_active =   False
is_stopped =        False

def on_press(key):
    global is_hot_pressed
    global is_combo_active
    global is_stopped
    if key == HOT_KEY:
        is_hot_pressed = True
    elif key == CLICK_KEY and is_hot_pressed:
        is_combo_active = True
    elif key == STOP_KEY and is_hot_pressed:
        is_stopped = True
        return False
            

def on_release(key):
    global is_hot_pressed
    global is_combo_active
    if key == HOT_KEY:
        is_hot_pressed = False
        is_combo_active = False
    elif key == CLICK_KEY:
        is_combo_active = False
    
kl = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
kl.start()

while not is_stopped:
    if is_combo_active:
        mc.press(Button.left)
        mc.release(Button.left)
        time.sleep(0.01)
        print("COMBO ACTIVE!")
