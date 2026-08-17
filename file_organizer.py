import os
import shutil


def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Error: Folder does not exist.")
        return

    if not os.path.isdir(folder_path):
        print("Error: The path is not a folder.")
        return

    files_moved = 0

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get file extension
        extension = os.path.splitext(file_name)[1].lower()

        # Skip files without extension
        if not extension:
            continue

        # Remove the dot from extension
        extension = extension[1:]

        # Create folder based on extension
        target_folder = os.path.join(folder_path, extension.upper())
        os.makedirs(target_folder, exist_ok=True)

        # Destination path
        destination = os.path.join(target_folder, file_name)

        # Avoid overwriting existing files
        if os.path.exists(destination):
            base_name, file_extension = os.path.splitext(file_name)

            counter = 1

            while os.path.exists(destination):
                new_file_name = f"{base_name}_{counter}{file_extension}"
                destination = os.path.join(target_folder, new_file_name)
                counter += 1

        # Move the file
        shutil.move(file_path, destination)

        print(f"Moved: {file_name} -> {extension.upper()}/")

        files_moved += 1

    print("\n==============================")
    print("       ORGANIZATION DONE")
    print("==============================")
    print(f"Files moved: {files_moved}")


def main():
    print("==============================")
    print("       FILE ORGANIZER")
    print("==============================")

    folder_path = input("Enter folder path: ").strip()

    if folder_path:
        organize_files(folder_path)
    else:
        print("Please enter a folder path.")


if __name__ == "__main__":
    main()