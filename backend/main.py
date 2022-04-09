import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.settings import settings
from apis.general_pages.route_homepage import general_pages_router
from db.session import engine
from db.base_class import Base


def include_router(app):
	app.include_router(general_pages_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
	Base.metadata.create_all(bind=engine)


def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	create_tables()
	return app


app = start_application()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)