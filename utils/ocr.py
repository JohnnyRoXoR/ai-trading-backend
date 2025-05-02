import pytesseract
from PIL import Image
import io

def extract_text(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    text = pytesseract.image_to_string(image)
    return text