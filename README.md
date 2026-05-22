# File Cleaner V1
A simple Python tool that scans any folder on your computer, finds the biggest files hiding inside it, and asks if you want to delete them to free up space.

## Features
* **Deep Scan:** Searches folder and subfolder.
* **Auto-Sort:** Automatically lists your files from biggest to smallest.
* **Crash Protection:** If system file is hit the program skips it instead of crashing.

## Safety
* **Blocks System Files:** It will refuse to delete critical files like `.exe` or `.dll`.
* **Protects Windows:** It blocks you from touching your main `C:\Windows` folder.
* **Double Check:** It forces you to type `YES` in all caps before it deletes anything.

## How To Run
1. Run the script in your terminal: `python analyzer.py`
2. Paste in the path to the folder you want to clean up.

# File Cleaner V2
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
