import os

def analyze_folder(folder_path):
    print(f"\nScanning: {folder_path}...")
    file_data = []

    # Go through directory and get files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Get file size in Megabytes (MB)
                size_bytes = os.path.getsize(file_path)
                size_mb = size_bytes / (1024 * 1024)
                file_data.append((file_path, size_mb))
            except (FileNotFoundError, PermissionError):
                # Skip files that are locked by the system or missing
                continue

    # File sorting (Largest to smallest)
    file_data.sort(key=lambda x: x[1], reverse=True)

    if not file_data:
        print("No files found or accessible.")
        return

    # --- FEATURE UPGRADE 1: CUSTOM PRINT AMOUNT ---
    print(f"\nFound {len(file_data)} total files.")
    limit_input = input("How many of the largest files would you like to view? (Default is 5): ")
    
    # If they press enter without typing a number (Default 5)
    limit = int(limit_input) if limit_input.isdigit() else 5
    
    print(f"\n--- TOP {limit} LARGEST FILES ---")
    top_files = file_data[:limit]
    for i, (path, size) in enumerate(top_files, 1):
        print(f"{i}. {path} | Size: {size:.2f} MB")

    # Multiple deletes
    print("\n---------------------------")
    print("To delete files, enter their numbers separated by commas (e.g., 1,3,4).")
    choice = input("Enter numbers to delete, or 'N' to exit: ")

    if choice.strip().upper() == 'N' or not choice.strip():
        print("\nExiting utility. No files were changed.")
        return

    #Turn input into str of numbers
    selections = []
    for x in choice.split(','):
        cleaned = x.strip()
        if cleaned.isdigit():
            num = int(cleaned)
            if 1 <= num <= len(top_files):
                selections.append(num)

    if not selections:
        print("\nNo valid file numbers selected. Exiting.")
        return

    # Remove duplicate entries if user put number twice
    selections = list(set(selections))

    print("\nFiles selected for permanent deletion:")
    total_freed_space = 0
    valid_files_to_delete = []

    # Verify each with safety guards in mind
    for num in selections:
        file_to_delete = top_files[num - 1][0]
        file_size = top_files[num - 1][1]
        
        # Safety Guards
        protected_extensions = ('.exe', '.dll', '.sys', '.ini')
        if file_to_delete.lower().endswith(protected_extensions):
            print(f"  [SKIPPED - SAFETY] {file_to_delete} (System File)")
            continue

        if "C:\\Windows" in file_to_delete or "system32" in file_to_delete.lower():
            print(f"  [SKIPPED - SAFETY] {file_to_delete} (Core Directory)")
            continue

        print(f"  [{num}] {file_to_delete} ({file_size:.2f} MB)")
        valid_files_to_delete.append((file_to_delete, file_size))
        total_freed_space += file_size

    if not valid_files_to_delete:
        print("\nAll selected files were blocked by safety guards or invalid. No changes made.")
        return

    # Double check
    print("\n---------------------------")
    confirm = input(f"Are you absolutely sure you want to permanently delete these {len(valid_files_to_delete)} files?\nThis will free up {total_freed_space:.2f} MB.\n(Type 'YES' to confirm): ")
    
    if confirm == "YES":
        print()
        for file_path, size in valid_files_to_delete:
            try:
                os.remove(file_path)
                print(f"[DELETED] {os.path.basename(file_path)}")
            except Exception as e:
                print(f"[FAILED] Could not delete {os.path.basename(file_path)}: {e}")
        print(f"\n[SUCCESS] Cleanup complete!")
    else:
        print("\nDeletion canceled by user. No files were changed.")

# Start
target_folder = input("Enter the full path of the folder you want to scan: ")
analyze_folder(target_folder)