from fastapi import FastAPI

import routes

app = FastAPI(docs_url="/swagger", title="SmallBusinessApplication")

app.include_router(routes.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}
