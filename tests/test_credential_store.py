from src.credential_store import CredentialStore

class TestCredentialStoreAttributes:
    def test_dir_path_set_to_passed_arg_when_arg_present(self):
        test_directory_path = "../test_data"
        store = CredentialStore(test_directory_path)

        assert store.dir_path == test_directory_path

    def test_dir_path_set_to_default_when_arg_not_present(self):
        store = CredentialStore()

        assert store.dir_path == "~/.aws/"

    def test_credentials_initialized_as_empty_dict(self):
        store = CredentialStore()
        assert store.credentials == {}
