from fastapi import FastAPI

app = FastAPI(docs_url="/swagger")


@app.get("/")
async def root():
    return {"message": "Hello World"}
