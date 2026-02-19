import psutil
from rich.console import Console
from rich.table import Table

console = Console()

def display_processes(limit=10):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes = sorted(processes, key=lambda x: x['memory_info'].rss, reverse=True)
    table = Table(title="Top Running Processes")
    table.add_column("PID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Memory (MB)", style="magenta")

    for p in processes[:limit]:
        memory_mb = round(p['memory_info'].rss / 1024**2, 2)
        table.add_row(str(p['pid']), p['name'], str(memory_mb))

    console.print(table)


def kill_process():
    pid_input = input("Enter PID to kill: ")
    try:
        pid = int(pid_input)
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait(timeout=3)
        print(f"[SUCCESS] Process {pid} terminated.")
        return f"Killed process {pid}"

    except psutil.NoSuchProcess:
        print("[ERROR] Process not found.")
        return f"Failed to kill process {pid_input}"

    except psutil.AccessDenied:
        print("[ERROR] Permission denied.")
        return f"Failed to kill process {pid_input} (Access Denied)"

    except psutil.TimeoutExpired:
        print("[ERROR] Process termination timed out.")
        return f"Failed to kill process {pid_input} (Timeout)"

    except Exception as e:
        print(f"[ERROR] {e}")
        return f"Failed to kill process {pid_input} ({e})"
