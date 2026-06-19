from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Kredaura API",
    version="0.1.0",
)

allowed_origins = [
    "http://localhost:3000",
    "https://kredaura.com",
    "https://www.kredaura.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "name": "Kredaura API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }
