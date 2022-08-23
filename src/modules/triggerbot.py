import pymem
import sys

sys.path.append("..")
import offsets


def trigger(csgo: pymem.Pymem, client, player) -> None:
    player_team: int = csgo.read_int(player + offsets.m_iTeamNum)
    crosshair_id: int = csgo.read_uint(player + offsets.m_iCrosshairId)
    crosshair_target: int = csgo.read_uint(csgo.read_uint(client + offsets.dwEntityList + (crosshair_id - 1) * 0x10))
    crosshair_team: int = csgo.read_uint(crosshair_target + offsets.m_iTeamNum)

    if 0 < crosshair_id < 64 and player_team != crosshair_team:
        csgo.write_int(client + offsets.dwForceAttack, 6)
