import uvicorn
from fastapi import FastAPI
from backend.core.settings import settings
from apis.general_pages.route_homepage import general_pages_router


def include_router(app):
	app.include_router(general_pages_router)


def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	return app


app = start_application()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)