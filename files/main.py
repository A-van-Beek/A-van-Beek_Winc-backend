__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os

# folder path
dir_path = r"F:\\Documenten\A-van-Beek_Winc-backend\files\\"
cache_dir = r"F:\\Documenten\A-van-Beek_Winc-backend\files\cache\\"

# # list to store files
res = []

# iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

# print(os.listdir(dir_path))
# print("lijst van files", res)

# # list to store directories
dirs = []

# iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isdir(os.path.join(dir_path, path)):
        dirs.append(path)

# print("lijst van directories", dirs)


def clean_cache():
    # check of cache-directory bestaat:
    if not os.path.exists(cache_dir):
        print("voeg de directory toe")
        os.makedirs(cache_dir)
    # iterate directory: check of cache bestaat...
    else:
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isdir(os.path.join(dir_path, path)):
                if path == "cache":
                    print("bestaat:", path)

                    for file_name in os.listdir(cache_dir):
                        print(file_name)
                        # construct full file path
                        file = cache_dir + file_name
                        if os.path.isfile(file):
                            print("deleting file:", file)
                            os.remove(file)
    return
