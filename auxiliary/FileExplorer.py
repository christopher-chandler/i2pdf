# Standard
import os
import platform

# Pip
None

# custom
None

# The slashes vary based on the operating system.
system = platform.system()
if system == "Darwin":
    slash = "/"
elif system == "Windows":
    slash = "\\"


class FileExplorer:
    """
    This class collections all folders from the home directory
    and provides the functions get_folders and get_files to
    the retrieve the absolute paths of the folders and their respective folders
    """

    def __init__(self, home_dir: str):
        self.home_dir = home_dir

    def get_folders(self) -> dict:
        """
        All folders in the current directory are gathered and then
        collected in a dictionary

        :return:
            file_paths: {the name of the folder : absolute path}
        """
        home_dir: str = self.home_dir
        file_paths = dict()

        folders: list = os.listdir(home_dir)
        for f in folders:
            file_paths[f] = fr"{home_dir}{slash}{f}"

        return file_paths

    def get_files(self, folder: str) -> dict:
        """
        The files that reside within the folders are gathered and
        assigend to a dictionary.

        :param folder: str:
            The folders from which the files should be ascertained.

        :return:
            file_paths: dict: {name of file: absolute path}
        """
        home_dir: str = self.home_dir
        file_paths = dict()
        folders: list = self.get_folders().get(folder)

        dir_fold: list = os.listdir(folders)
        for f in dir_fold:
            file_paths[f] = fr"{home_dir}{slash}{folder}{slash}{f}"

        return file_paths


if __name__ == "__main__":
     pass