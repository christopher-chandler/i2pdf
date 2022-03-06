# Standard
import os

# Pip
None

# custom
None


class FileExplorer:
    """
    This class collections all folders from the home directory
    and provides the functions get_folders and get_files to
    the retrieve the absolute paths of the folders and their respective folders
    """

    def __init__(self, home_dir):
        self.home_dir = home_dir

    def get_folders(self):
        home_dir = self.home_dir
        file_paths = dict()
        my_list = os.listdir(home_dir)
        for i in my_list:
            file_paths[i] = fr"{home_dir}\{i}"

        return file_paths

    def get_files(self, folder: str):
        file_paths = dict()
        home_dir = self.home_dir
        fold = self.get_folders().get(folder)

        my_list = os.listdir(fold)
        for i in my_list:
            file_paths[i] = fr"{home_dir}\{folder}\{i}"

        return file_paths

if __name__ == "__main__":
    pass