import pymem
import sys

sys.path.append("..")
import offsets
from const import Settings, skin_from_id


def change_skin(csgo: pymem.Pymem, client, player, settings: Settings):
    # Loop through weapons
    for i in range(0, 3):
        current_weapon: int = csgo.read_int(player + offsets.m_hMyWeapons + i * 0x4) & 0xfff
        current_weapon = csgo.read_int(client + offsets.dwEntityList + (current_weapon - 1) * 0x10)

        # Continue if no weapon is active
        if not current_weapon:
            continue

        weapon_id: int = csgo.read_short(current_weapon + offsets.m_iItemDefinitionIndex)
        # Get the skin associated with the current weapon
        weapon_skin: int = skin_from_id(settings.weapons_list, weapon_id)

        # Write the skin to memory
        if weapon_skin:
            csgo.write_int(current_weapon + offsets.m_iItemIDHigh, -1)
            csgo.write_uint(current_weapon + offsets.m_nFallbackPaintKit, weapon_skin)
            csgo.write_float(current_weapon + offsets.m_flFallbackWear, 0.0001)  # Float = 0.0001

