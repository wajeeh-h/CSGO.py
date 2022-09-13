import time
import pymem
import offsets

from typing import NoReturn
from threading import Thread
from modules.triggerbot import trigger
from keyboard import is_pressed
from const import settings


class AimThread(Thread):
    def __init__(self, csgo: pymem.Pymem, client, engine) -> None:
        super(AimThread, self).__init__()
        self.csgo: pymem.Pymem = csgo
        self.client = client
        self.engine = engine

    def run(self) -> NoReturn:
        while True:
            player = self.csgo.read_uint(self.client + offsets.dwLocalPlayer)

            if not player:
                continue

            if settings.settings_dict.get("trigger_enabled") and is_pressed("j"):
                trigger_delay = settings.settings_dict.get("trigger_delay")
                if trigger_delay:
                    time.sleep(trigger_delay/100)
                trigger(self.csgo, self.client, player)

            time.sleep(0.01)

