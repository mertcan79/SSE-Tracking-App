from flet import UserControl, Text, ListTile, Column, Card, Icon, icons, Row, TextField
import sys
sys.path.append('../')
from link.members import Members
from link.tasks import Tasks
from link.stream import Stream
import json
import time
import pprint

last_member_update =Members().get_all_members().json()[-1][0]
last_task_update =Tasks().get_tasks().json()[-1][-5]

class SSEBoard(UserControl):
    """
    class for returning SSE output
    """

    def __init__(self):
        super().__init__()
        self.top_res = list()

        for i in range(10):
            self.top_res.append(Stream().get_stream())
        
    def build(self):

            return Column(
                controls=[
                        TextField(
                            value=str(self.top_res),
                            text_size=20,
                            multiline= True,
                            width=1200,
                            
                        )
                    ],
                expand=True,
            )
