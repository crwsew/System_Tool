import psutil

def get_top_processes(limit=10):
    """Return top processes sorted by memory usage."""
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes = sorted(
        processes,
        key=lambda x: x['memory_info'].rss,
        reverse=True
    )

    return processes[:limit]

def display_processes(limit=10):
    print("\n--- Top Running Processes ---")
    processes = get_top_processes(limit)

    for p in processes:
        memory_mb = round(p['memory_info'].rss / 1024**2, 2)
        print(f"PID: {p['pid']} | Name: {p['name']} | Memory: {memory_mb} MB")
