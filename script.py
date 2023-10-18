import os
import glob

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("To start classifying your files by file type, please paste the folder path below:")

    # Getting the folder path
    folder_path = "F:\\Descargas"

    # Changing the current working directory
    os.chdir(folder_path)

    # Counting the items and folders to classify
    items_in_folder = os.listdir(folder_path)
    files_counter = 0
    dirs_counter = 0
    # print(items_in_folder)

    for item in items_in_folder:
        # TODO continue here
        item.split(".")
        # print(item)
        # if os.path.isfile(os.path.join(folder_path, item)):
        if os.path.isfile(item):
            files_counter += 1
        # elif os.path.isdir(os.path.join(folder_path, item)):
        elif os.path.isdir(item):
            dirs_counter += 1

    # Awaiting user to accept the classification
    print(f"There are {files_counter} files in the directory, and {dirs_counter} folders")
    print("\nPress enter to start classifying by file extension or type exit to terminate program:")
    if input() == "exit":
        print("Exiting process...")
        exit(0)

