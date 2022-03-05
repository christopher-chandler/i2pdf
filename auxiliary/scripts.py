# standard
import datetime
import os
import time

# Pip
None

# Custom
None


def generate_folders():
    """

    :return:
    """

    file_paths = dict()
    my_list = os.listdir(os.getcwd())
    for i in my_list:
        file_paths[i] = fr"{os.getcwd()}/{i}"

    return file_paths


folders = generate_folders()
ts = time.time()
time_stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
