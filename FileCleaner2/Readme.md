# Batch File Cleaner

An upgraded Python tool that scans your folders for giant files. It lets you choose how many files to display and lets you delete multiple files all at once to save time.

## Features
* **Custom View Limits:** You choose exactly how many files to look at (like viewing the top 5, 10, or 15 biggest files).
* **Delete Multiple Files:** Type numbers separated by commas (like `1, 3, 5`) to delete a whole batch at once.
* **Cleans Input:** If you accidentally type the same number twice, it removes the duplicate of your choice so nothing breaks.
* **Safety Report:** It checks your file choices against safety rules *before* asking you to confirm.

## Safety
* **No Accidental Deletions:** It automatically skips and saves system files (`.exe`, `.sys`, `.dll`) even if you accidentally select them.
* **Core Folder Shield:** Hard-blocks any changes to core operating system folders.
* **Final Warning:** Tells you exactly how many Megabytes (MB) of space you are about to clear before you hit the final `YES`.

## How To Run
1. Run the script in your terminal: `python analyzer.py`
2. Paste in the path to the folder you want to clean up.