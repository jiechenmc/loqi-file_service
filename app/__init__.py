from fastapi import FastAPI
from app.core import read_blob, upload_blob

app = FastAPI()
b_name = "loqi-loqi.appspot.com"


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/get")
async def read_blob_by_id():
    return read_blob(b_name, "testBlob")


async def upload_blob_bytes():
    upload_blob(b_name)
    return "success"