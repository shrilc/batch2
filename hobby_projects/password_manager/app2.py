from fastapi import FastAPI

app2 = FastAPI()

@app2.get("/passwords")
def index():
    return {"Hello": "World"}