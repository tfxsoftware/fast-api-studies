from fastapi import APIRouter
from src.modules.user.user_router import router as user_router

router: APIRouter = APIRouter()
router.include_router(user_router)