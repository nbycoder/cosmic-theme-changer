#!/bin/bash
set -e

# VARIABLES

# THEME
theme_DIR="$HOME/.config/cosmic/com.system76.CosmicTheme.Mode/v1/is_dark"
theme_light="false" 
theme_dark="true"

# WALLPAPER
bg_DIR="$HOME/.config/cosmic/com.system76.CosmicBackground/v1/all"
bg_light="su-light.png" # CHANGE TO YOUR WALLPAPER NAME
bg_dark="su-dark.jpeg" # CHANGE TO YOUR WALLPAPER NAME

# ICONS
icons_DIR="$HOME/.config/cosmic/com.system76.CosmicTk/v1/icon_theme"
icons_light='"rose-pine-dawn"' # CHANGE TO YOUR ICON THEME NAME
icons_dark='"rose-pine-moon"' # CHANGE TO YOUR ICON THEME NAME

# CODE

sed -i -e "s/$theme_dark/$theme_light/g" "$theme_DIR" # CHANGE THEME
sed -i -e "s/$bg_dark/$bg_light/g" "$bg_DIR" # CHANGE WALLPAPER
sed -i -e "s/$icons_dark/$icons_light/g" "$icons_DIR" # CHANGE ICONS
