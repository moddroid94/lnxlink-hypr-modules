# lnxlink hyprland modules

A small collection of custom hyprland shell focused group of modules for [lnxlink](https://github.com/bkbilly/lnxlink).

## Custom Service start for some qml shells
All user session related modules may require a custom systemd trigger, depending on the configuration of your shell/greeter. 
In my case, using caelestia or dux shell, I have to touch a file after starting hyprland in the shell, as the login greeter uses hyprland itself, lnxlink gets triggered before the actual login.

I've included the edited systemd service, the trigger ready path service and the touch command to be added to hyprland.lua, more info on [systemd/readme.md](/systemd/readme.md)

## Modules:
- hypr_lock (custom lock/unlock toggle)
- hypr_screen (custom hyprland dpms monitor on/off)
- hypr_color (custom current accent state)

## Usage
Hyprland is merely a compositor, what you run on top is totally your choice, and because of that, making an universal module is basically impossible.


### - Lock screen R/W
Change the `compositor` variable at the beginning of the file depending on your shell, this only works in that specific shell.

Available shells:
- Dux "dms" - Default
- Caelestia "caelestia"


### - Screen OnOff R/W
Simple dpms enable/disable command, should work with most installations out of the box


### - System Accent Color RO
Ricing is important, the included module reads the current scheme accent color from the generated file.
There are 2 variants:
- caelestia: uses a custom json/generator
- dux: uses standard matugen toml file

# Installation

Copy the modules somewhere in your home and point your lnxlink custom modules entry to them, refer to the [lnxlink](https://github.com/bkbilly/lnxlink) page for more info.
