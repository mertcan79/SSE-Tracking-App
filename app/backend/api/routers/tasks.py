from fastapi import APIRouter
import schemas
import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)
 
# now we can import the module in the parent
# directory.
import database


router = APIRouter(tags=["Tasks"], prefix="/task")


@router.get("/all")
def get_all_tasks():
    database.cr.execute("""SELECT * FROM tasks""")
    tasks = database.cr.fetchall()
    return tasks
