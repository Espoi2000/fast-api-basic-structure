from fastapi import APIRouter ,Depends ,BackgroundTasks
from dependencies import get_token_header
router = APIRouter()


router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@router.post("/")
async def update_admin( email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, "message sent")
    return {"message": "Admin getting  email"}
@router.post("/notification/{email}")
async def send_notification(email: str ,background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, "message sent")
    return {"message": f"message sent to {email}"}