hl.on("hyprland.start", function()
	hl.exec_cmd("sh -c 'touch /run/user/$(id -u)/shell-ready'")
end)