class CredentialStore:
    def __init__(self, dir_path:str="~/.aws/"):
        self.dir_path = dir_path
        self.credentials = {}
