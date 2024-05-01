
from fastapi import FastAPI
from .routes.endpoints import router as api_router

app = FastAPI(title="My FastAPI Application")

# Include all routers
app.include_router(api_router)
