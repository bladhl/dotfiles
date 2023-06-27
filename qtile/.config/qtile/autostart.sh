#!/bin/sh

# picom --experimental-backends &
picom &

# bg
feh --bg-scale --randomize ~/Pictures/Wallpaper/* &

# wifi
nm-applet &

# systray volume
volumeicon &

# systray battery icon
cbatticon -u 5 -i notification -r 10 -c "shutdown" -l 20 &
