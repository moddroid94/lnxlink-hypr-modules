"""Turns on or off the screen"""

import logging
import os
import re
import subprocess

from lnxlink.modules.scripts.helpers import get_display_variable

logger = logging.getLogger("lnxlink")


class Addon:
    """Addon module"""

    def __init__(self, lnxlink):
        """Setup addon"""
        self.name = "Hypr Screen"
        self.display_variable = get_display_variable()
        session_type = os.environ.get("XDG_SESSION_TYPE", "unknown").lower()
        desktop_env = os.environ.get("XDG_CURRENT_DESKTOP", "unknown").lower()

        if session_type in ["unknown", "wayland"] and "hyprland" in desktop_env:
            self.control_screen = self._control_wayland_hyprland
            self.get_screen_status = self._get_wayland_hyprland
        else:
            raise SystemError(f"Session type '{session_type}' not supported")

    def _run_command(self, argv: list[str]) -> str:
        try:
            return subprocess.run(argv, capture_output=True, text=True).stdout
        except (OSError, subprocess.SubprocessError) as err:
            logger.error("command failed: %s (%s)", " ".join(argv), err)

    def exposed_controls(self):
        """Exposes to home assistant"""
        return {
            "Screen OnOff": {
                "type": "switch",
                "icon": "mdi:monitor",
            }
        }

    def get_info(self):
        """Gather information from the system"""
        return self.get_screen_status()

    def start_control(self, topic, data):
        """Control system"""
        command = data.lower()
        if command not in {"on", "off"}:
            logger.error("Expected `on` or `off`, received: `%s`", command)
            return
        self.control_screen(command)

    def _control_wayland_hyprland(self, command):
        active_state = command == "on"
        if active_state:
            new_state = 'hl.dsp.dpms({ action = "on" })'
        else:
            new_state = 'hl.dsp.dpms({ action = "off" })'
        try:
            self._run_command(["hyprctl", "dispatch", new_state])
        except Exception as err:
            logger.error("Error controlling Hyprland screen: %s", err)

    def _get_wayland_hyprland(self):
        state = self._run_command(["hyprctl", "monitors", "all"])
        value = re.search(r"dpmsStatus: [\d]", state)
        if value:
            if "1" in str(value):
                return "ON"
            else:
                return "OFF"
        else:
            logger.error("Error getting dpms state: %s", state)
