from fastapi import FastAPI
import src.api_router as api_router
from src.database import Base, engine

print("ola mundo1")
app = FastAPI(
    title="teste",
    version="1.0"
    )

app.include_router(api_router.router)
Base.metadata.create_all(bind=engine)
