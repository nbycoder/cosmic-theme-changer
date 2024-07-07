# Cosmic Theme Changer Bash Script

Hello! Ever since Mozilla closed their API to third party Cosmic no longer switches theme as sunset _so_ I figured I would write a script to make things a little easier! Before we go any further **please back up the files listed in the DIR variables!** I am not responsible for any damage made to these config files.

This can be used with either **darkman** or **crontab**

## Changing themes at a certain time

crontab follows the following syntax: **MINUTE | HOUR | DAY (month) | MONTH | DAY (week) [sun-sat, or 0-6]**

So, for example, if you wanted to turn your light theme at 10am, you could add ```00 10 * * * /.light-theme.sh``` at the end of your crontab file (with **crontab -e**)

## Using Darkman

The first step is to install [darkman](https://gitlab.com/WhyNotHugo/darkman). 

Then, create **dark-mode.d** & **light-mode.d** in $HOME/.local/share, and paste/move the scripts there, and you're done!

## A few notes

- For the icons, it's important to remember to leave the formatting as is! If you remove any of the commas the command will not run properly
    - To get the name of your icon pack simply go to _Settings > Desktop > Apparence > Experimental settings_ 
- For the wallpapers/backgrounds, simply change the name of it to your own.
    - If your wallpapers are in different locations you will need to change the next two variables to include the whole path. For example:
      - light_bg = '"$HOME/Images/light_background.png"' **DOUBLE QUOTES ARE NEEDED**
      - dark_bg = '"/$HOME/backgrounds/dark_background.png"'
- The variables _light_theme_ & _dark_theme_ are taken from the _name_ property in the .ron config files or _$HOME/.config/cosmic/com.system76.CosmicTheme.Light/v1/name_.
