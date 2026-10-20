from fastapi import FastAPI
import src.api_router as api_router

print("ola mundo")
app = FastAPI(
    title="teste",
    version="1.0"
    )

app.include_router(api_router)