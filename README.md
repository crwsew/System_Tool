
# System Tool

Python project: **System Monitor + File Manager**  
Purpose: OS concepts practice (CPU, RAM, Process, Thread, File System, I/O)  
Level: College prep / GitHub showcase

---

## Features
- Interactive CLI menu with clear options
- **System Info**: CPU cores, CPU usage, RAM used/total, Disk free/total, OS info
- **Process Viewer**: Show top running processes with memory usage
- **Kill Process**: Terminate process by PID (with permission handling)
- **File Manager**: List/Create/Delete/Check Size of files
- **Logging**: All user actions logged with timestamps (`log.txt`)
- **Fancy CLI**: Colored tables and clear formatting using `rich`
- **Exception Handling**: Prevents crashes, handles permissions, not found, timeout

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/crwsew/system_tool.git
````

2. Navigate to the project folder:

```bash
cd system_tool
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the program:

```bash
python main.py
```

---

## Concepts Demonstrated

* CPU & RAM monitoring
* Process & Thread handling
* File System I/O operations
* Exception handling
* Logging
* CLI design with colors and tables

---

## Optional Enhancements

* Add screenshots of CLI outputs
* Extend File Manager with folders
* Filter processes by name or memory usage
* Add interactive search in Process Viewer

---

## Dependencies

* psutil – Access system/process info
* rich – Fancy colored CLI output

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Notes

* Kill Process requires permission; may not terminate system-critical processes
* Tested on Windows/Linux/macOS
* Logs are stored in `log.txt` automatically
* CLI designed for readability and ease of use

---

## Author

crwsew
