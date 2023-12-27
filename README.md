<h1 align="center">Key5</h1>

<p align="center">
  <img src="https://github.com/Rexaintreal/key5/blob/main/KEY%205.jpg" alt="Key5 Logo">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/python-3.8-blue.svg" alt="Python: 3.8">
</p>

<p align="center">
  Key5 is a discreet Python application designed for keyboard input monitoring. It operates in stealth mode, logging keystrokes and uploading the log file to Dropbox for remote access. Use it responsibly and comply with legal and ethical standards.
</p>

--- 
__Warning:__ This program monitors keyboard inputs and logs them. Use responsibly and ensure compliance with legal and ethical standards.

## Table of Contents

- [Features](#features)
- [How it Works](#how-it-works)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
- [Configuration](#configuration)
  - [Obtain Dropbox API Credentials](#obtain-dropbox-api-credentials)
  - [Update Dropbox Access Token](#update-dropbox-access-token)
- [Set Secret Termination Phrase](#set-secret-termination-phrase)
- [Dependencies](#dependencies)
  - [pynput](#pynput)
  - [dropbox](#dropbox)
  - [plyer](#plyer)
  - [pygetwindow](#pygetwindow)
  - [requests](#requests)
  - [datetime](#datetime)
  - [socket](#socket)
  - [os](#os)
  - [Installing Dependencies](#installing-dependencies)
- [Obtaining Dropbox API Token](#obtaining-dropbox-api-token)
- [Author](#author)
- [You may also like...](#you-may-also-like)

---

## Features

- **Stealth Mode:** Operates silently in the background without a console window.
- **Remote Logging:** Logs keyboard inputs and uploads the log file to Dropbox.
- **Secret Phrase:** Allows you to terminate the program with a secret key combination.

## How it Works

Key5 uses the [pynput](https://github.com/moses-palmer/pynput) library to monitor keyboard inputs. The program runs in the background and logs keystrokes, capturing the active application at the time of input. The log file is periodically uploaded to Dropbox using the Dropbox API for remote access.

## Installation

**Clone the Repository:**
   ```bash
   https://github.com/Rexaintreal/key5.git
   ```
---
## Configuration

Before running Key5, you need to perform a few configuration steps:

1. **Obtain Dropbox API Credentials:**
   - Visit the [Dropbox Developer Console](https://www.dropbox.com/developers/apps).
   - Create a new app to get the `APP_KEY` and `APP_SECRET`.
   - Generate an access token with the necessary permissions.
   
2. **Update Dropbox Access Token:**
   - Open the `key5.py` file.
   - Replace `DROPBOX_ACCESS_TOKEN` with the obtained access token.

   ```python
   # Dropbox API credentials
   DROPBOX_ACCESS_TOKEN = 'your_access_token_here'
   ```

---
## Set Secret Termination Phrase

Key5 uses a secret termination phrase to allow you to exit the program and upload logs to Dropbox securely. Follow these steps to set the secret termination phrase:

1. Open the `key5.py` file in your preferred code editor.

2. Locate the `secret_phrase` list in the script:

   ```python
   # Secret termination phrase
   secret_phrase = ['t', 'e', 'r', 'm', 'i', 'n', 'a', 't', 'e']
   ```
   ## Dependencies

Key5 relies on the following Python libraries and tools:

- [pynput](https://github.com/moses-palmer/pynput): A library to control and monitor input devices.

- [dropbox](https://github.com/dropbox/dropbox-sdk-python): The Dropbox SDK for Python, used for uploading logs to Dropbox.

- [plyer](https://github.com/pbernut/plyer): A Python library for accessing features commonly found on various platforms.

- [pygetwindow](https://github.com/asweigart/pygetwindow): A simple module for getting window information.

- [requests](https://github.com/psf/requests): A popular Python library for making HTTP requests.

- [datetime](https://docs.python.org/3/library/datetime.html): A module supplying classes for working with dates and times.

- [socket](https://docs.python.org/3/library/socket.html): A low-level networking interface in Python.

- [os](https://docs.python.org/3/library/os.html): A module for interacting with the operating system.

These dependencies can be installed using the following command:

```bash
pip install pynput dropbox plyer pygetwindow requests
```
Ensure you have Python installed on your system before installing these dependencies.

For Dropbox integration, you need to have a Dropbox account and create a Dropbox app to obtain the necessary API credentials.


### Obtaining Dropbox API Token

Before you can use Key5 to log keyboard inputs and upload the log file to Dropbox, you need to obtain a Dropbox API token. Follow these steps:

1. Visit the [Dropbox Developer Console](https://www.dropbox.com/developers/apps).

2. Create a new app:
   - Click on "Create app."
   - Select "Scoped access."
   - Choose the type of access your app needs (e.g., "Full dropbox" or "App folder").
   - Enter a unique name for your app.

3. Generate an access token:
   - Scroll down to the "OAuth 2" section.
   - Click on the "Generate" button under the "OAuth 2 access token" heading.

4. Copy the generated access token.

5. Open the `key5.py` file in your preferred code editor.

6. Locate the `DROPBOX_ACCESS_TOKEN` variable in the script.

7. Replace `'your_access_token_here'` with the copied access token:

   ```python
   # Dropbox API credentials
   DROPBOX_ACCESS_TOKEN = 'your_access_token_here'
   ```

## Author

Object Tales was created by [Saurabh Tiwari](https://github.com/Rexaintreal). 

- [Email](mailto:saurabhtiwari7986@gmail.com)

## You may also like...

- [Libro Voice](https://github.com/Rexaintreal/Libro-Voice) - A PDF to Audio Converter
- [Snippet Vision](https://github.com/Rexaintreal/Snippet-Vision)- A Youtube Video Summarizer
- [Weather App](https://github.com/Rexaintreal/WeatherApp) - A Python Weather Forcast App
- [Python Screenrecorder](https://github.com/Rexaintreal/PythonScreenrecorder) - A Python Screen Recorder
- [Typing Speed Tester](https://github.com/Rexaintreal/TypingSpeedTester) - A Python Typing Speed Tester
- [Movie Recommender](https://github.com/Rexaintreal/Movie-Recommender) - A Python Movie Recommender
- [Password Generator](https://github.com/Rexaintreal/Password-Generator) - A Python Password Generator
- [Object Tales](https://github.com/Rexaintreal/Object-Tales) - A Python Image to Story Generator
- [Finance Manager](https://github.com/Rexaintreal/Finance-Manager) - A Flask WebApp to Moniter Savings
- [Codegram](https://github.com/Rexaintreal/Codegram) - A Social Media Web App
- [Simple-Flask-Notes](https://github.com/Rexaintreal/Simple-Flask-Notes) - A Flask Notes App
