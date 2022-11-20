from fastapi import FastAPI, Request
from app.core import read_blob, upload_blob

app = FastAPI()
b_name = "loqi-loqi.appspot.com"


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/api/upload")
async def read_blob_by_id(request: Request):
    print("HI")
    res = await request.body()
    print(res)
    return read_blob(b_name, "testBlob")