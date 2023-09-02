import os

import uvicorn
from fastapi import FastAPI, UploadFile

from meta_morph_pix.services import transformation_service, storage_service
from meta_morph_pix.utils.blackblaze_client import get_b2_client

app = FastAPI()


@app.get("/")
async def healthcheck():
    cl = get_b2_client()
    bucket = cl.get_bucket_by_id("76ac3dd4126f93fb8a6f061e")
    for file_version, _ in bucket.ls(recursive=True):
        print(file_version.file_name)
    return {"Hello": "Pano Rabbit"}


@app.post("/transform_images")
async def transform_image(folder_name: str, files: list[UploadFile]):
    messages = []
    for file in files:
        transformed_image = await transformation_service.transform_image(file)
        try:
            filename = storage_service.upload_image(transformed_image, f"{folder_name}/{file.filename}")
            messages.append(f"Image {filename} uploaded successfully")
        except FileExistsError as error:
            messages.append(f"{str(error)}")
    return {"data": messages}


def run():
    host = os.getenv("HOST", "127.0.0.1")
    uvicorn.run("meta_morph_pix.router:app", host=host, reload=True)
