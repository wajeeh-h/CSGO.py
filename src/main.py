import os
import time
import pymem

from gui import init_gui
from visuals_thread import VisualThread
from aim_thread import AimThread
from misc_thread import MiscThread
from offsets import load_offsets


def setup_threads() -> None:
    # Create threads for each section of the multi hack (visuals, aim, misc)
    # The main thread will run the GUI
    visuals = VisualThread(csgo, client, engine)
    aim = AimThread(csgo, client, engine)
    misc = MiscThread(csgo, client, engine)
    visuals.daemon = True
    aim.daemon = True
    misc.daemon = True
    visuals.start()
    aim.start()
    misc.start()


if __name__ == '__main__':
    csgo_running = False

    while not csgo_running:
        try:
            # Connect to CSGO and set up our modules
            csgo = pymem.Pymem("csgo.exe")
            client = pymem.process.module_from_name(csgo.process_handle, "client.dll").lpBaseOfDll
            engine = pymem.process.module_from_name(csgo.process_handle, "engine.dll").lpBaseOfDll
            os.system("cls")
            os.system("\n [CSGO.py] Retrieving Offsets")
            load_offsets()
            os.system("\n [CSGO.py] Offsets Retrieved")
            os.system("\n [CSGO.py] Injected...")
            csgo_running = True
        except pymem.exception.ProcessNotFound:
            os.system("cls")
            print("[CSGO.py] Waiting for CSGO")
            time.sleep(5)
        except pymem.exception.MemoryReadError:
            os.system("cls")
            print("[CSGO.py] CSGO Closed - Exiting")
        except AttributeError:
            os.system("cls")
            print("[CSGO.py] Waiting for Modules...")
            time.sleep(5)

    setup_threads()
    init_gui()

