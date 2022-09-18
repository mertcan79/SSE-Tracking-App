from flet import UserControl, Text, ListTile, Column, Card, Icon, icons
import sys
sys.path.append('../')
from link.members import Members
import json

members =Members().get_all_members().json()

class MembersBoard(UserControl):
    """
    class for returning cards of members
    """

    def __init__(self):
        super().__init__()

    def build(self):
        
        return Column(
            controls=[
                Card(
                    content=ListTile(
                        leading=Icon(icons.PERSON),
                        title=Text(str(member[0])),
                        subtitle=Text(
                            str(member[1])
                            + "\n"
                            + str(member[2])
                            + "\n"
                            + str(member[3])
                            + "\n"
                            + str(member[4])
                        ),
                    ),
                    width=500,
                    height=123,
                )
                for member in members
            ],
            expand=True,
        )
