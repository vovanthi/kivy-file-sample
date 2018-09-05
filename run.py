import subprocess
from subprocess import TimeoutExpired
import time, os, configparser
from watchdog.events import PatternMatchingEventHandler, FileSystemEventHandler
from watchdog.observers import Observer

iniFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'sample.kv')
mode = []
proc = None
class IniFileHandler(FileSystemEventHandler):
    def __init__(self, callback):
        super(IniFileHandler, self).__init__()
        self.callback = callback

    def on_modified(self, event):
        if not event.is_directory:
            try:
                self.callback()
            except configparser.NoSectionError:
                pass

def run_kivy_main():
    global proc
    proc = subprocess.Popen(["python", "sampleApp.py"])

def kill_kivy_main():
    print('-----------kill-------------')
    global proc
    try:
        proc.communicate(timeout=1)
    except TimeoutExpired:
        proc.kill()
        proc.communicate()

def restart_kivy_main():
    kill_kivy_main()
    run_kivy_main()

if __name__ == '__main__':
    run_kivy_main()

    # set watchdog handler
    event = IniFileHandler(restart_kivy_main)
    observer = Observer()
    observer.schedule(event, os.path.dirname(os.path.abspath(__file__)), recursive=True)
    observer.start()

    # loop and print setting value
    while True:
        print('Loop watch file in main')
        time.sleep(1)