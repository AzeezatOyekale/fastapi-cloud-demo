from fastapi import FastAPI

app = FastAPI(title="FastAPI Cloud Demo")

@app.get("/")
def read_root():
    return {
        "message": "FastAPI app deployed successfully 🚀",
        "status": "ok"
    }

@app.get("/health")
def health_check():
    return {
        "service": "running",
        "uptime": "stable"
    }