import psutil
import platform
from rich.console import Console
from rich.table import Table

console = Console()

def display_system_info():
    info = {
        "OS": f"{platform.system()} {platform.release()} ({platform.architecture()[0]})",
        "CPU Cores": psutil.cpu_count(logical=True),
        "CPU Usage": f"{psutil.cpu_percent(interval=1)}%",
        "RAM Used": f"{round(psutil.virtual_memory().used / 1024**3,2)}GB",
        "RAM Total": f"{round(psutil.virtual_memory().total / 1024**3,2)}GB",
        "Disk Free": f"{round(psutil.disk_usage('/').free / 1024**3,2)}GB",
        "Disk Total": f"{round(psutil.disk_usage('/').total / 1024**3,2)}GB"
    }

    table = Table(title="System Information")
    table.add_column("Component", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    for key, value in info.items():
        table.add_row(key, str(value))

    console.print(table)
