import urllib3
from auth.api import router as auth_router
from content.api import router as content_router
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


app = FastAPI()


origins = [
    "http://localhost:3000",
    "http://0.0.0.0:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8888",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routing
app.include_router(auth_router)
app.include_router(content_router)
