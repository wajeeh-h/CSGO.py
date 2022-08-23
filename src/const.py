from dataclasses import dataclass, field


@dataclass
class Weapon:
    name: str
    skin_id: int

    def change_skin(self, skin_id) -> None:
        self.skin_id = skin_id


@dataclass
class Settings:
    enemy_glow_enabled: bool = False
    glow_colour_enemy: tuple[float] = (255, 0, 0, 255)  # R, G, B, A
    team_glow_enabled: bool = False
    glow_colour_team: tuple[float] = (0, 0, 255, 255)
    radar_enabled: bool = True
    trigger_enabled: bool = False
    trigger_delay: float = 0
    trigger_key: str = "J"
    bhop_enabled: bool = False
    bhop_delay: float = 0
    skin_changer_enabled: bool = False
    # Holds the corresponding (chosen) weapon skin for each weapon
    weapons_list: list[Weapon] = field(default_factory=lambda: [
        Weapon("Desert Eagle", 0),
        Weapon("Dual Berettas", 0),
        Weapon("Five-SeveN", 0),
        Weapon("Glock-18", 0),
        Weapon("AK-47", 0),
        Weapon("AUG", 0),
        Weapon("AWP", 0),
        Weapon("FAMAS", 0),
        Weapon("G3SG1", 0),
        Weapon("Galil AR", 0),
        Weapon("M249", 0),
        Weapon("M4A4", 0),
        Weapon("MAC-10", 0),
        Weapon("P90", 0),
        Weapon("MP5-SD", 0),
        Weapon("UMP-45", 0),
        Weapon("XM1014", 0),
        Weapon("PP-Bizon", 0),
        Weapon("MAG-7", 0),
        Weapon("Negev", 0),
        Weapon("Sawed-Off", 0),
        Weapon("Tec-9", 0),
        Weapon("P2000", 0),
        Weapon("MP7", 0),
        Weapon("MP9", 0),
        Weapon("Nova", 0),
        Weapon("P250", 0),
        Weapon("SCAR-20", 0),
        Weapon("SG 553", 0),
        Weapon("SSG 08", 0),
        Weapon("M4A1-S", 0),
        Weapon("USP-S", 0),
        Weapon("CZ75", 0),
        Weapon("R8 Revolver", 0),
    ])

    def update_vars(self, args: tuple) -> None:
        self.enemy_glow_enabled, self.glow_colour_enemy, self.team_glow_enabled, self.glow_colour_team, \
        self.radar_enabled, self.trigger_enabled, self.trigger_delay, self.trigger_key, self.bhop_enabled, \
        self.bhop_delay, self.skin_changer_enabled = args

    def update_weapons_list(self, weapons_list: list[Weapon]) -> None:
        self.weapons_list = weapons_list


# Global settings manager
settings: Settings = Settings()

# Holds all the games weapon ids, corresponds with the order of weapons_list[]
weapon_ids = [
    1,
    2,
    3,
    4,
    7,
    8,
    9,
    10,
    11,
    13,
    14,
    16,
    17,
    19,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    32,
    33,
    34,
    35,
    36,
    38,
    39,
    40,
    60,
    61,
    63,
    64
]


# Returns a skin id given a weapon id
def skin_from_id(weapons_list: list[Weapon], weapon_id: int) -> int:
    for i in range(0, len(weapon_ids)):
        if weapon_ids[i] == weapon_id:
            return weapons_list[i].skin_id
    return 0
