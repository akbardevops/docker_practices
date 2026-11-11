from fastapi import FastAPI

app = FastAPI(title="hit-api")

@app.get("/")
def root():
    #root endpoint
    return {"message": "Hello to container!"}

@app.get("/health")
def health():
    #health endpoint to check the health of the application
    return {"status": "ok"}