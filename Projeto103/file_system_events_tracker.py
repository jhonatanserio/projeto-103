import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass

from_dir=""

class FileEventHandler (FileSystemEventHandler):

    def on_created(seld,event):
        print(f"ola,{event.src_path} foi criado")
    def on_deleted(seld,event):
        print(f"pelo visto,{event.src_path} ja foi excluido")
    def on_moved(seld,event):
        print(f"o,{event.src_path} foi reposicionado")
    def on_modified(seld,event):
        print(f"o,{event.src_path} sofreu alterações")

try:
     while True:
          time.sleep(2)
          print("executando..")
except KeyboardInterrupt:
     print("interropido")
     Observer.stop()