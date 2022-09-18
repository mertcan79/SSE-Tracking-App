from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import database
import schemas
from routers import members, tasks,sse
import uvicorn

app = FastAPI()

app.include_router(members.router)
app.include_router(tasks.router)
app.include_router(sse.router)

@app.get("/")
def route():
    return {"msg", "Hello World"}


@app.post("/login")
def login_user(credentials: OAuth2PasswordRequestForm = Depends()):
    database.cr.execute(
        """select * from users where username=%s and password =%s""",
        (credentials.username, credentials.password),
    )
    user = database.cr.fetchone()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User '{credentials.username} was not found'",
        )
    return user

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)