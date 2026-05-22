# File Cleaner
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