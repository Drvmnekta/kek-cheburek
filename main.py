from json import load
import sys
from dotenv import load_dotenv
import os
from PIL import Image
from pynput import keyboard
load_dotenv()

LORD_PATH = os.getenv('FILEPATH')


def show_lord():
    img = Image.open(LORD_PATH)
    img.show()


def on_press(key):
    if key == keyboard.Key.shift:
        show_lord()
    if key == keyboard.Key.right:
        sys.exit()


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
