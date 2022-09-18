import requests
from requests.models import Response



class Members(requests.Session):
    """
    class for handling members data
    """

    def __init__(self) -> None:
        super().__init__()

    def get_all_members(self) -> Response:
        res = self.get(f"http://127.0.0.1:8000/member/all")
        return res
