import os
from pathlib import Path

def list_files(path="."):
    print(f"\nFiles in {path}:")
    try:
        for f in Path(path).iterdir():
            print(f.name)
    except FileNotFoundError:
        print("Path not found.")

def create_file(filename):
    try:
        Path(filename).touch(exist_ok=False)
        print(f"File created: {filename}")
    except FileExistsError:
        print("File already exists.")

def delete_file(filename):
    if Path(filename).exists():
        os.remove(filename)
        print(f"File deleted: {filename}")
    else:
        print("File not found.")

def file_size(filename):
    if Path(filename).exists():
        size = Path(filename).stat().st_size
        print(f"Size of {filename}: {size} bytes")
    else:
        print("File not found.")
