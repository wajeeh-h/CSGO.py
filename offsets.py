import os
import subprocess
import json
from typing import IO


# def get_sig(module: str, pattern, extra: int, offset: int, relative: bool) -> str:
#     csgo: pymem.Pymem = pymem.Pymem("csgo.exe")
#     module = pymem.process.module_from_name(csgo.process_handle, module)
#     bytes_: bytes = csgo.read_bytes(module.lpBaseOfDll, module.SizeOfImage)
#     match = re.search(pattern, bytes_).start()
#
#     if relative:
#         result = csgo.read_int(module.lpBaseOfDll + match + offset) + extra
#     else:
#         result = csgo.read_int(module.lpBaseOfDll + match + offset) + extra - module.lpBaseOfDll
#
#     get_result = "0x{:X}".format(result)
#     return result


def load_offsets():
    path_to_dir: str = os.path.dirname(__file__)
    path_to_dir = os.path.join(path_to_dir, "hazedumper")
    assert os.path.isdir(path_to_dir)
    os.chdir(path_to_dir)
    subprocess.Popen(["hazedumper.exe"])


path_to_dir: str = os.path.dirname(__file__)
path_to_json = os.path.join(path_to_dir, "hazedumper", "csgo.json")
f: IO = open(path_to_json)
data: dict[str, dict[str, int]] = json.load(f)

signatures: dict[str, int] = data["signatures"]
dwForceJump: int = signatures["dwForceJump"]
dwLocalPlayer: int = signatures["dwLocalPlayer"]
dwEntityList: int = signatures["dwEntityList"]
dwGlowObjectManager: int = signatures["dwGlowObjectManager"]
dwForceAttack: int = signatures["dwForceAttack"]

netvars: dict[str, int] = data["netvars"]
m_fFlags: int = netvars["m_fFlags"]
m_hMyWeapons: int = netvars["m_hMyWeapons"]
m_iItemDefinitionIndex: int = netvars["m_iItemDefinitionIndex"]
m_iItemIDHigh: int = netvars["m_iItemIDHigh"]
m_nFallbackPaintKit: int = netvars["m_nFallbackPaintKit"]
m_flFallbackWear: int = netvars["m_flFallbackWear"]
m_iTeamNum: int = netvars["m_iTeamNum"]
m_iGlowIndex: int = netvars["m_iGlowIndex"]
m_bSpotted: int = netvars["m_bSpotted"]
m_iCrosshairId: int = netvars["m_iCrosshairId"]