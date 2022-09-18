import requests
from requests.models import Response



class Tasks(requests.Session):
    """
    class for handling tasks data
    """

    def __init__(self) -> None:
        super().__init__()

    def get_tasks(self) -> Response:
        res = self.get(f"http://127.0.0.1:8000/task/all")
        return res
