#! /usr/bin/env python

from suntimes import sunset, today

#time = datetime.now()

# VARIABLES -- replace $USER with your own username
theme_DIR = "/home/$USER/.config/cosmic/com.system76.CosmicTheme.Mode/v1/is_dark"
theme_light = "false" 
theme_dark = "true"

bg_DIR = "/home/$USER/.config/cosmic/com.system76.CosmicBackground/v1/all"
bg_light = "su-light.png" 
bg_dark = "su-dark.jpeg"

icons_DIR = "/home/$USER/.config/cosmic/com.system76.CosmicTk/v1/icon_theme"
icons_light = '"rose-pine-dawn"'
icons_dark = '"rose-pine-moon"'

# CHANGE THEME TO LIGHT

if today < sunset :

    # THEME
    with open(theme_DIR, 'w') as file:
        file.write(theme_light)
    
    # WALLPAPER
    with open(bg_DIR, 'r') as file:
        file_contents = file.read()

        updated_contents = file_contents.replace(bg_dark, bg_light)

    with open(bg_DIR, 'w') as file:
        file.write(updated_contents)


    # ICONS
    with open(icons_DIR, 'w') as file:
        file.write(icons_light)
    
# CHANGE THEME TO DARK
elif today >= sunset:

    # THEME
    with open(theme_DIR, 'w') as file:
        file.write(theme_dark)

    # WALLPAPER
    with open(bg_DIR, 'r') as file:
        file_contents = file.read()

        updated_contents = file_contents.replace(bg_light, bg_dark)

    with open(bg_DIR, 'w') as file:
        file.write(updated_contents)

    # ICONS
    with open(icons_DIR, 'w') as file:
        file.write(icons_dark)
