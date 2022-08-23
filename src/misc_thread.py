import time
import pymem
import offsets

from threading import Thread
from const import settings
from keyboard import is_pressed
from modules.bhop import do_bhop
from modules.skin_changer import change_skin


class MiscThread(Thread):
    def __init__(self, csgo: pymem.Pymem, client, engine) -> None:
        super(MiscThread, self).__init__()
        self.csgo: pymem.Pymem = csgo
        self.client = client
        self.engine = engine

    def run(self) -> None:
        while True:
            player = self.csgo.read_uint(self.client + offsets.dwLocalPlayer)

            if not player:
                continue

            if settings.bhop_enabled and is_pressed("space"):
                # Bugged for some reason
                # if settings.bhop_delay:
                #     time.sleep(settings.bhop_delay/100)
                do_bhop(self.csgo, self.client, player)

            if settings.skin_changer_enabled:
                change_skin(self.csgo, self.client, player, settings)

            time.sleep(0.01)
