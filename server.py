from fastapi  import FastAPI

app = FastAPI()

@app.get("/attack_url")
async def root():
    return {"url": "http://155.212.217.171:8000/"}