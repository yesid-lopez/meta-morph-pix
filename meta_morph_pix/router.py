import uvicorn
from fastapi import FastAPI, UploadFile
from meta_morph_pix.services import transformation_service, storage_service

app = FastAPI()


@app.get("/")
async def healthcheck():
    return {"Hello": "World"}


@app.post("/transform_image")
async def transform_image(file: UploadFile):
    transformed_image = await transformation_service.transform_image(file)
    # storage_service.upload_image(transformed_image, file.filename)
    return {"status": "success"}


def run():
    uvicorn.run("meta_morph_pix.router:app", reload=True)
