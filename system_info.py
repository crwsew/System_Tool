import psutil
import platform

def get_system_info():
    """Return system information as dictionary."""
    return {
        "os": f"{platform.system()} {platform.release()} ({platform.architecture()[0]})",
        "cpu_cores": psutil.cpu_count(logical=True),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "ram_used": round(psutil.virtual_memory().used / 1024**3, 2),
        "ram_total": round(psutil.virtual_memory().total / 1024**3, 2),
        "disk_free": round(psutil.disk_usage('/').free / 1024**3, 2),
        "disk_total": round(psutil.disk_usage('/').total / 1024**3, 2),
    }

def display_system_info():
    info = get_system_info()
    print("\n--- System Information ---")
    print(f"OS: {info['os']}")
    print(f"CPU Cores: {info['cpu_cores']}")
    print(f"CPU Usage: {info['cpu_usage']}%")
    print(f"RAM: {info['ram_used']}GB / {info['ram_total']}GB")
    print(f"Disk Free: {info['disk_free']}GB / {info['disk_total']}GB")
