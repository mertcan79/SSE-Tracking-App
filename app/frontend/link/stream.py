import requests
from requests.models import Response
import time

from sseclient import SSEClient


class Stream(requests.Session):
    """
    class for handling members data
    """

    def __init__(self) -> None:
        super().__init__()

    def get_stream(self):
        res = SSEClient('http://127.0.0.1:8000/stream?param1=test')
        return str(res.__next__())
