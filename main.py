from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from PIL import Image
import pytesseract
import io
from pathlib import Path

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = Path("templates/index.html")
    return html_path.read_text()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return {"extracted_text": text}