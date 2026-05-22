import os

def analyze_folder(folder_path):
    print(f"\nScanning: {folder_path}...")
    file_data = []

    #Directory
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

    #File sorting by size (largest to smallest)
    file_data.sort(key=lambda x: x[1], reverse=True)

    #Print the top 5 largest files
    print("\n--- TOP 5 LARGEST FILES ---")
    if not file_data:
        print("No files found or accessible.")
        return

    # Keep top 5 files
    top_files = file_data[:5]
    for i, (path, size) in enumerate(top_files, 1):
        print(f"{i}. {path} | Size: {size:.2f} MB")

    # 4. Interaction to delete
    print("\n---------------------------")
    choice = input("Would you like to delete any of these files? (Enter the number 1-5, or 'N' to exit): ")

    if choice.isdigit():
        num = int(choice)
        if 1 <= num <= len(top_files):
            file_to_delete = top_files[num - 1][0]
            
        #SAFETY GUARDS
            # Block system extensions that are important
            protected_extensions = ('.exe', '.dll', '.sys', '.ini')
            if file_to_delete.lower().endswith(protected_extensions):
                print(f"\n[SAFETY BLOCK] Deletion canceled. System files ({', '.join(protected_extensions)}) cannot be deleted through this utility.")
                return

            # Blocks from deleting important systems
            if "C:\\Windows" in file_to_delete or "system32" in file_to_delete.lower():
                print("\n[SAFETY BLOCK] Deletion canceled. Modifying core operating system directories is strictly prohibited.")
                return

            # confirmation
            confirm = input(f"Are you absolutely sure you want to permanently delete:\n--> {file_to_delete}?\n(Type 'YES' to confirm): ")
            
            if confirm == "YES":
                try:
                    os.remove(file_to_delete)
                    print(f"\n[SUCCESS] File successfully deleted. Freed up {top_files[num - 1][1]:.2f} MB!")
                except Exception as e:
                    print(f"\n[ERROR] Could not delete file: {e}")
            else:
                print("\nDeletion canceled by user.")
        else:
            print("\nInvalid number selection.")
    else:
        print("\nExiting utility. No files were changed.")

# Start point
target_folder = input("Enter the full path of the folder you want to scan: ")
analyze_folder(target_folder)