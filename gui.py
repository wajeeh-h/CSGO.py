import re
import dearpygui.dearpygui as dpg
from const import settings


# Updates the list for our list box
def update_skins() -> None:
    dpg.configure_item("skins", items=settings.weapons_list)


# Changes the Skin ID associated with a given weapon in const.py
def set_skin() -> None:
    skin_id = dpg.get_value("skin_ids")
    weapon_name = dpg.get_value("skins")
    weapon_name = re.search('=(.*),', weapon_name).group(1).replace("'", "")
    for i in settings.weapons_list:
        if i.name == weapon_name:
            i.change_skin(skin_id)


def init_gui() -> None:
    dpg.create_context()
    dpg.create_viewport(title="CSGO.py", width=500, height=500, resizable=False)
    dpg.setup_dearpygui()

    # Create the GUI
    with dpg.window(label="Menu Version 0.1A", width=500, height=500, no_resize=True,
                    no_move=True, no_collapse=True, no_close=True):
        with dpg.tab_bar():
            with dpg.tab(label="Visuals"):
                with dpg.collapsing_header(label="Glow"):
                    dpg.add_checkbox(label="Enemy Glow?", tag="enemy_glow_enabled")
                    dpg.add_color_edit(label="Enemy Colour", tag="glow_colour_enemy",
                                       default_value=settings.settings_dict.get("glow_colour_enemy"))
                    dpg.add_checkbox(label="Team Glow?", tag="team_glow_enabled")
                    dpg.add_color_edit(label="Team Colour", tag="glow_colour_team",
                                       default_value=settings.settings_dict.get("glow_colour_team"))
                with dpg.collapsing_header(label="Radar"):
                    dpg.add_checkbox(label="Enabled", tag="radar_enabled")

            with dpg.tab(label="Aim"):
                with dpg.collapsing_header(label="Trigger"):
                    dpg.add_checkbox(label="Enabled", tag="trigger_enabled")
                    dpg.add_input_text(label="Trigger Key", tag="trigger_key", uppercase=True, no_spaces=True)
                    dpg.add_slider_float(label="Delay (ms)", tag="trigger_delay", min_value=0, max_value=10)

            with dpg.tab(label="Misc"):
                with dpg.collapsing_header(label="Bhop"):
                    dpg.add_checkbox(label="Enabled", tag="bhop_enabled")
                    dpg.add_slider_float(label="Delay (ms)", tag="bhop_delay", min_value=0, max_value=10)

                with dpg.collapsing_header(label="Skin Changer"):
                    dpg.add_checkbox(label="Enabled", tag="skin_changer_enabled")
                    dpg.add_listbox(items=settings.weapons_list, tag="skins", num_items=13)
                    dpg.add_input_int(label="ID", tag="skin_ids", step=0, callback=set_skin)
                    dpg.add_button(label="Update Skins Index", callback=update_skins)

    dpg.show_viewport()
    while dpg.is_dearpygui_running():
        # Update the values of our settings each time the GUI updates
        settings_dict_temp = {}
        for key in settings.settings_dict:
            settings_dict_temp[key] = dpg.get_value(key)
        settings.settings_dict = settings_dict_temp
        dpg.render_dearpygui_frame()
    dpg.destroy_context()
