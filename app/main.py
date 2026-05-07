from fastapi import FastAPI

app = FastAPI(title="Flight Info")

@app.get("/health")
def health_check():
    return {"status": "healthy"}
