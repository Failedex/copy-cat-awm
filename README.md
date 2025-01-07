# A copy of Cat awm in sway(fx) and eww

I made this because it was "possible". (And to prove a point)

[Original Cat awm](https://github.com/beckkake/cat-awm)

![Copy Cat](https://github.com/Failedex/copy-cat-awm/blob/main/screenshot.png?raw=true)

## Running
THIS IS INCREDIBLY HACKY!!! I DON'T RECOMMEND DAILY DRIVING THIS!!!

But if you still want to try it out, here's how

```
# Running this again will close it
eww -c ./ open-many windowbars bar --toggle

# Remove borders
swaymsg default_border pixel 0

# citsfsip manages tiling. This is optional because you could still use sway tiling
swaymsg for_window '[app_id=.*]' floating enable
./scripts/citsfsip.py
```

Note that this ~~config~~ gimmick was made for a single 1920x1080 monitor.

## Issues
If you encounter any issues, fix it yourself.

