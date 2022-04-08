import uvicorn
from fastapi import FastAPI
#from dotenv import load_dotenv
from backend.core.settings import settings

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
#app = FastAPI()

@app.get("/")
def hello_api():
    return {"msg":"Hello API -2"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)