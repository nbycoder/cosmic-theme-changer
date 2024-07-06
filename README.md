# Cosmic Theme Changer Python Script

Hello! Ever since Mozilla closed their API to third party Cosmic no longer switches theme as sunset _so_ I figured I would write a script to make things a little easier! Before we go any further **please back up the files listed in the DIR variables!** I am not responsible for any damage made to these config files.

## Changing themes at a certain time

This script can be tweaked to change themes at a certain time. To do so, in **suntimes.py** replace the **today** variable with:

```python
today = date.strftime("%H:%M:%S")
```

and create a new **time** variable:

```python
time = sunset.strftime("%H:%M:%S")
```

then in **cosmic-theme.py** change:

```python
from suntimes import sunset, today
```
to
```python
from suntimes import time, today
```

## A few notes

- For the icons, it's important to remember to leave the formatting as is! If you remove any of the commas the command will not run properly
    - To get the name of your icon pack simply go to _Settings > Desktop > Apparence > Experimental settings_ 
- For the wallpapers/backgrounds, simply change the name of it to your own.
    - If your wallpapers are in different locations you might need to change the next two variables to include the whole path. For example:
      - light_bg = '"/home/$USER/Images/light_background.png"' **DOUBLE QUOTES ARE NEEDED**
      - dark_bg = '"/home/$USER/backgrounds/dark_background.png"'
- To run the script at startup open _Startup Applications_, click Add, name it whatever you want, in the Command section do: _python3 /path/to/script &_. (The _&_ at the end keeps it running in the background.)
- The variables _light_theme_ & _dark_theme_ are taken from the _name_ property in the .ron config files or _$HOME/.config/cosmic/com.system76.CosmicTheme.Light/v1/name_.
