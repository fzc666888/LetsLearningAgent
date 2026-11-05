"""组装 FastAPI 应用。"""

from fastapi import FastAPI

from app.routers import health, items

app = FastAPI(title="LearningAgent")
app.include_router(health.router)
app.include_router(items.router)
