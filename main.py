from time import time
from fastapi import FastAPI, UploadFile, __version__, HTTPException, Form, File
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import httpx  # Library untuk HTTP request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Gantilah dengan domain yang spesifik jika perlu
    allow_credentials=True,
    allow_methods=["*"],  # Izinkan semua metode HTTP
    allow_headers=["*"],  # Izinkan semua header
)

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>Arutala API</title>
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
        </div>
    </body>
</html>
"""

# Base URLs untuk microservices
TRANSLATE_JAVANESE_SCRIPT = "https://translate.arutalaaksara.com"
SCAN_JAVANESE_SCRIPT = "https://arutala.taufiqdp.com"
SCAN_SUNDANESE_SCRIPT = "https://api-sundanese.arutalaaksara.com"

@app.get("/")
async def root():
    """
    Root endpoint.

    Returns:
        HTMLResponse: An HTML page with links to API documentation.
    """
    return HTMLResponse(html)

@app.get('/ping')
async def hello():
    """
    Health check endpoint.

    Returns:
        dict: A JSON object containing a 'pong' response, FastAPI version, and current timestamp.
    """
    return {'res': 'pong', 'version': __version__, "time": time()}

# Models
class TranslateRequest(BaseModel):
    """
    Model for translation requests.

    Attributes:
        text (str): The text to be translated.
    """
    text: str

class WriteRequest(BaseModel):
    language: str
    letter: str

class WriteTestRequest(BaseModel):
    language: str
    letter: str

# Endpoints

@app.post("/translate/latin-to-aksara")
async def translate_latin_to_aksara(request: TranslateRequest):
    """
    Translate text from latin to Aksara.

    Args:
        request (TranslateRequest): The input text to be translated.

    Returns:
        dict: The original text and its translation to Aksara.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{TRANSLATE_JAVANESE_SCRIPT}/translate/latin-to-aksara",
            json=request.dict(),
        )
        return response.json()

@app.post("/translate/aksara-to-latin")
async def translate_aksara_to_latin(request: TranslateRequest):
    """
    Translate text from Aksara to latin.

    Args:
        request (TranslateRequest): The input text in Aksara.

    Returns:
        dict: The original text and its translation to latinn.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{TRANSLATE_JAVANESE_SCRIPT}/translate/aksara-to-latin",
            json=request.dict(),
        )
        return response.json()

@app.post("/scan/image-to-latin")
async def scan_image_to_latin(file: UploadFile):
    """
    Scan an uploaded image and extract text in latinn.

    Args:
        file (UploadFile): The uploaded image file.

    Returns:
        dict: The filename and detected text in latinn.
    """
    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = await client.post(f"{SCAN_JAVANESE_SCRIPT}/predict", files=files)
        test = await client.post(f"https://414b-182-4-103-116.ngrok-free.app/upload", files=files)
        return response.json()

@app.post("/scan/image-to-aksara")
async def scan_image_to_aksara(file: UploadFile):
    """
    Scan an uploaded image and extract text in Aksara.

    Args:
        file (UploadFile): The uploaded image file.

    Returns:
        dict: The filename and detected text in Aksara.
    """
    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = await client.post(f"{SCAN_JAVANESE_SCRIPT}/scan/image-to-aksara", files=files)
        return response.json()

@app.post("/write")
async def write_aksara(
    letter: str = Form(...),
    language: str = Form(...),
    file: UploadFile = File(...)
):
    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = await client.post(f"{SCAN_JAVANESE_SCRIPT}/predict", files=files)
        response_data = response.json()  # Ambil JSON response

    if str(response_data.get("prediction", "")).lower() == str(letter).lower():
        return {"status": True}
    else:
        return {"status": False}

# 1. LEARNING
@app.post("/write/learning")
async def write_learning(
    letter: str = Form(...),
    file: UploadFile = File(...)
):
    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = await client.post(f"{SCAN_JAVANESE_SCRIPT}/predict", files=files)
        response_data = response.json()

    if str(response_data.get("prediction", "")).lower() == str(letter).lower():
        return {"status": True}
    else:
        return {"status": False}


# 2. PRACTICE
@app.post("/write/practice")
async def write_practice(file: UploadFile = File(...)):
    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = await client.post(f"{SCAN_JAVANESE_SCRIPT}/predict", files=files)
        response_data = response.json()

    return {"prediction": response_data.get("prediction", "")}


# 3. CHALLENGE
@app.post("/write/challenge")
async def write_challenge(
    letter: str = Form(...),
    file: UploadFile = File(...)
):
    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = await client.post(f"{SCAN_JAVANESE_SCRIPT}/predict", files=files)
        response_data = response.json()

    prediction = str(response_data.get("prediction", ""))
    status = prediction.lower() == letter.lower()

    return {"status": status, "prediction": prediction}

# 1. LEARNING
@app.post("/write/sundanese/learning")
async def write_learning(
    letter: str = Form(...),
    file: UploadFile = File(...)
):
    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = await client.post(f"{SCAN_SUNDANESE_SCRIPT}/predict", files=files)
        response_data = response.json()

    if str(response_data.get("prediction", "")).lower() == str(letter).lower():
        return {"status": True}
    else:
        return {"status": False}


# 2. PRACTICE
@app.post("/write/sundanese/practice")
async def write_practice(file: UploadFile = File(...)):
    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = await client.post(f"{SCAN_SUNDANESE_SCRIPT}/predict", files=files)
        response_data = response.json()

    return {"prediction": response_data.get("prediction", "")}


# 3. CHALLENGE
@app.post("/write/sundanese/challenge")
async def write_challenge(
    letter: str = Form(...),
    file: UploadFile = File(...)
):
    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        response = await client.post(f"{SCAN_SUNDANESE_SCRIPT}/predict", files=files)
        response_data = response.json()

    prediction = str(response_data.get("prediction", ""))
    status = prediction.lower() == letter.lower()

    return {"status": status, "prediction": prediction}
