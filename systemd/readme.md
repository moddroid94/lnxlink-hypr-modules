# Installation of custom systemd path

## 1 - trigger path
Move `shell-ready.path` to

`~/.config/systemd/user` 

and 

`~/.config/systemd/user/default.target.wants`

## 2 - untriggerd base service

then replace the `lnxlink.service` in 

`/usr/lib/systemd/user`

## 3 - startup file touch

add 

`hl.exec_cmd("sh -c 'touch /run/user/$(id -u)/shell-ready'")`

to the `hl.on("hyprland.start"` function