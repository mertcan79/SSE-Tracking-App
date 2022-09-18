from flet import (
    UserControl,
    Column,
    Card,
    ListTile,
    Icon,
    icons,
    Text,
    PopupMenuButton,
    PopupMenuItem,
)
import sys
sys.path.append('../')
from link.tasks import Tasks
import json

tasks = Tasks().get_tasks().json()

class TasksBoard(UserControl):
    """
    class for returning cards of tasks
    """

    def build(self):
        
        return Column(
            controls=[
                Card(
                    content=ListTile(
                        leading=Icon(icons.TASK),
                        title=Text(str(task[0])),
                        subtitle=Text(
                            f"Description : {str(task[1])}"
                            + "\n"
                            + f"Created at : {str(task[2])}"
                            + "\n"
                            + f"Deadline : {str(task[3])}"
                            + "\n"
                            + f"Created by : {str(task[4])}"
                            + "\n"
                            + f"Member id : {str(task[5])}"
                            + "\n"
                            + f"Task id : {str(task[6])}"
                            + "\n"
                            + f"Member Name : {str(task[7])}"
                        ),
                        trailing=PopupMenuButton(
                            icon=icons.MORE_VERT,
                            items=[
                                PopupMenuItem(text="Delete"),
                                PopupMenuItem(text="Update"),
                            ],
                        ),
                    ),
                    width=700,
                    height=200,
                )
                for task in tasks
            ]
        )
