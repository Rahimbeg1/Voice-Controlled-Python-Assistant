import psutil
import time


def cpu_usage():

    return (
        f"CPU usage is "
        f"{psutil.cpu_percent(interval=1)} percent"
    )


def ram_usage():

    memory = psutil.virtual_memory()

    return (
        f"RAM usage is "
        f"{memory.percent} percent"
    )


def battery_status():

    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information unavailable"

    return (
        f"Battery is at "
        f"{battery.percent} percent"
    )


def disk_usage():

    disk = psutil.disk_usage('/')

    return (
        f"Disk usage is "
        f"{disk.percent} percent"
    )


def network_status():

    net = psutil.net_io_counters()

    sent = round(
        net.bytes_sent / (1024 * 1024),
        2
    )

    received = round(
        net.bytes_recv / (1024 * 1024),
        2
    )

    return (
        f"Data sent {sent} MB "
        f"and received {received} MB"
    )


def uptime():

    up = time.time() - psutil.boot_time()

    hours = int(up // 3600)

    return (
        f"System has been running "
        f"for {hours} hours"
    )