import os


def get_credentials():
    repo_root = os.path.abspath(os.path.join(__file__, os.path.pardir))
    cred_path = os.path.join(repo_root, "credentials.txt")
    with open(cred_path, "r") as file:
        line = file.readlines()
        login = line[0].split("=")[-1].strip()
        password = line[1].split("=")[-1].strip()
    return login, password
