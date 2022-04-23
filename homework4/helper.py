import os


def get_version():
    repo_root = os.path.abspath(os.path.join(__file__, os.path.pardir))
    dir_name = os.path.join(repo_root, "stuff")
    print(os.listdir(dir_name)[0].split("_")[1][1:7])
