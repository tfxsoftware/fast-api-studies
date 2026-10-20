from fastapi import APIRouter
import user_service as service

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users():
    return [{"id": 1, "name": "Tomas"}, {"id": 2, "name": "Maria"}]

@router.get("/")
def get_user():
    return service.get_user()