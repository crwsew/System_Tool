import os
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

def list_files(path="."):
    try:
        files = list(Path(path).iterdir())
        table = Table(title=f"Files in {path}")
        table.add_column("Filename", style="cyan")
        for f in files:
            table.add_row(f.name)
        console.print(table)
    except FileNotFoundError:
        print("[ERROR] Path not found.")

def create_file(filename):
    try:
        Path(filename).touch(exist_ok=False)
        print(f"[SUCCESS] File created: {filename}")
    except FileExistsError:
        print("[ERROR] File already exists.")

def delete_file(filename):
    if Path(filename).exists():
        os.remove(filename)
        print(f"[SUCCESS] File deleted: {filename}")
    else:
        print("[ERROR] File not found.")

def file_size(filename):
    if Path(filename).exists():
        size = Path(filename).stat().st_size
        print(f"[INFO] Size of {filename}: {size} bytes")
    else:
        print("[ERROR] File not found.")
