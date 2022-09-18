import requests
#from ..core.config import settings


class Login(requests.Session):
    """
    class for validating the user input from the api
    """

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        super().__init__()

    def send_creds(self):
        res = self.post(
            f"http://127.0.0.1:8000/login",
            data={"username": self.username, "password": self.password},
        )
        return res
