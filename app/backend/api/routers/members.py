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

router = APIRouter(tags=["Members"], prefix="/member")



@router.get("/all")
def get_all_members():
    database.cr.execute("""SELECT * FROM members """)
    members = database.cr.fetchall()
    return members