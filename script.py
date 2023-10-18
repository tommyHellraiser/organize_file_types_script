import os
import shutil


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("To start classifying your files by file type, please paste the folder path below:")

    # Getting the folder path
    cur_dir = os.getcwd()
    print(cur_dir)

    # Organized files folder
    organized_folder = cur_dir + "\\organized"

    if not os.path.exists(organized_folder):
        os.mkdir(organized_folder)
    else:
        shutil.rmtree(organized_folder)
        os.mkdir(organized_folder)

    # Changing the current working directory
    os.chdir(cur_dir)

    # Counting the items and folders to classify
    items_in_folder = os.listdir(cur_dir)
    files_counter = 0
    dirs_counter = 0

    for item in items_in_folder:
        if os.path.isfile(item):
            files_counter += 1
        elif os.path.isdir(item):
            dirs_counter += 1

    # Awaiting user to accept the classification
    print(f"There are {files_counter} files in the directory, and {dirs_counter} folders")
    print("\nPress enter to start classifying by file extension or type exit to terminate program:")
    if input() == "exit":
        print("Exiting process...")
        exit(0)

    copy_count = 0

    os.chdir(organized_folder)

    # Iterate and classify all items
    for item in items_in_folder:

        # If file is current executable named script.exe, skip
        if item == "script.exe":
            continue
            
        # Split into file name and extension
        split = os.path.splitext(item)

        extension = split[1][1::]

        # If folder with extension name does not exist, create it
        if not os.path.exists(extension) and extension != "":
            os.mkdir(extension)

        if extension != "":
            result = shutil.copy(os.path.join(cur_dir, item), extension)
            if result is not None:
                copy_count += 1

    print(f"Successfully organized {copy_count} files")
    print("Press enter to exit...")
