import pymem
import sys
sys.path.append("..")
import offsets
from const import Settings

def do_visuals(csgo: pymem.Pymem, client, player, settings: Settings) -> None:
    glow_manager: int = csgo.read_int(client + offsets.dwGlowObjectManager)

    for i in range(1, 16):  # Loop through all entities (max=32)
        entity: int = csgo.read_int(client + offsets.dwEntityList + i * 0x10)

        if entity:
            entity_team: int = csgo.read_int(entity + offsets.m_iTeamNum)
            entity_glow: int = csgo.read_int(entity + offsets.m_iGlowIndex)
            player_team: int = csgo.read_int(player + offsets.m_iTeamNum)
            if player_team == entity_team:
                if settings.team_glow_enabled:
                    write_glow(csgo, glow_manager, entity_glow, settings.glow_colour_team)

            elif player_team != entity_team:
                if settings.enemy_glow_enabled:
                    write_glow(csgo, glow_manager, entity_glow, settings.glow_colour_enemy)
                if settings.radar_enabled:
                    csgo.write_int(entity + offsets.m_bSpotted, 1)


def write_glow(csgo: pymem.Pymem, glow_manager: int, entity_glow: int, colours: tuple[float]) -> None:
    csgo.write_float(glow_manager + entity_glow * 0x38 + 0x8, colours[0] / 255)   # R
    csgo.write_float(glow_manager + entity_glow * 0x38 + 0xC, colours[1] / 255)   # G
    csgo.write_float(glow_manager + entity_glow * 0x38 + 0x10, colours[2] / 255)   # B
    csgo.write_float(glow_manager + entity_glow * 0x38 + 0x14, colours[3] / 255)  # Alpha
    csgo.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)                   # Enable glow
