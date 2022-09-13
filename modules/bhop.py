import time
import pymem
import sys

sys.path.append("..")
import offsets


def do_bhop(csgo: pymem.Pymem, client, player) -> None:
    force_jump: int = client + offsets.dwForceJump
    on_ground: int = csgo.read_uint(player + offsets.m_fFlags)
    # If we are in the ground
    if on_ground == 257 or on_ground == 263:
        # Force a jump by writing to memory
        csgo.write_int(force_jump, 6)
