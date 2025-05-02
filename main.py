from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils.ocr import extract_text
from recommendation import generate_recommendation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_chart(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(content)
    symbol = "BTC/USDT" if "BTC" in text else "ETH/USDT"
    result = generate_recommendation(symbol)
    return result