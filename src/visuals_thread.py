import time
import pymem
import offsets

from threading import Thread
from const import settings
from modules.visuals import do_visuals


class VisualThread(Thread):
    def __init__(self, csgo: pymem.Pymem, client, engine) -> None:
        super(VisualThread, self).__init__()
        self.csgo: pymem.Pymem = csgo
        self.client = client
        self.engine = engine

    def run(self) -> None:
        while True:
            player = self.csgo.read_uint(self.client + offsets.dwLocalPlayer)

            if not player:
                continue

            if settings.enemy_glow_enabled or settings.team_glow_enabled or settings.radar_enabled:
                do_visuals(self.csgo, self.client, player, settings)

            time.sleep(0.05)
