from actions import *

COMMANDS = {

    "open google": open_google,

    "open youtube": open_youtube,

    "open instagram": open_instagram,

    "open linkedin": open_linkedin,

    "open whatsapp": open_whatsapp,

    "open music": play_music,

    "cpu usage": cpu_status,

    "ram usage": ram_status,

    "memory usage": ram_status,

    "battery status": battery_info,

    "battery percentage": battery_info,

    "disk usage": disk_info,

    "network status": network_info,

    "system uptime": uptime_info
}


def process_command(command):

    command = command.lower()

    for keyword, action in COMMANDS.items():

        if keyword in command:

            action()

            return True

    return False