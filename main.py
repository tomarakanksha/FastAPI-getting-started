from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/name")
async def name():
    return {"name": "Akanksha Tomar"}