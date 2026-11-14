# lnxlink caelestia/hyprland modules

A series of custom caelestia/hyprland focused group of modules for [lnxlink](https://github.com/bkbilly/lnxlink).

## Custom Service start for some qml shells
Lockscreen and Screen state modules may require a custom systemd trigger, depending on the configuration of your shell/greeter, caelestia for example needs to touch a file after starting hyprland to then trigger the lnxlink service start, otherwise it will start before it and not pick up the session environment set by the hyprland startup process.

## Modules:
- hypr_lock (custom caelestia lock/unlock toggle)
- hypr_screen (custom hyprland dpms monitor on/off)
- hypr_color (custom caelestia current accent state)

## MakeYourOwn
Hyprland is merely a compositor, what you run on top is totally your choice, and because of that, making an universal module i basically impossible.

### screen state module 
Uses a custom command that can be easily changed to fit the current shell IPC call for that function

### Lock screen R/W
Simple dmps enable/disable command, should work with most installation out of the box

### System Accent Color
Ricing is important, the included module reads the custom caelestia scheme file, could be easily redirected to whatever color scheme you use

# Usage

just copy the modules somewhere and point your lnxlink custom modules config to it.

remove the default session_lock and screen_onoff if using the respective custom modules.
