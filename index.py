from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

import base64

from aiHelper import aiIMGExplain, aiTextExplain
from html import contentHTML

app = FastAPI()

# Allow all origins in CORS (you might want to restrict it to specific origins in a production environment)
app.add_middleware(
    CORSMiddleware,
    # This should be more restrictive in a production environment
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload-image")
async def upload_image(plant: str, file: UploadFile = File(...)):
    # Read the file content
    contents = await file.read()

    # Encode the file content as base64
    img_data = base64.b64encode(contents).decode('utf-8')

    # Create a data URL for the image
    # data_url = f"data:image/png;base64,{img_data}"
    return aiIMGExplain(img_data, plant)
    # return {"message": "Image saved successfully", 'img_data_url': data_url}


@app.post("/chat")
async def upload_image(text: str, context: str):
    return aiTextExplain(text, context)


@app.get("/status", response_class=HTMLResponse)
async def backend_status():

    return contentHTML
