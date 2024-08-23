from fastapi import FastAPI
from app.router.resourcesRouter import router

app = FastAPI(
	title="API Historial de Divisas",
    description="API para registrar y consultar el historial de divisas.",
    version="1.0.0",
)

app.include_router(router)