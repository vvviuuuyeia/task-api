from fastapi import FastAPI
from routers import tasks

app = FastAPI(title="Task API", version="0.4.0")
app.include_router(tasks.router)