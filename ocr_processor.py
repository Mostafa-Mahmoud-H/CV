# ocr_processor.py (النسخة النهائية باستخدام كودك)
import os
import cv2
import pytesseract
import re

# تأكد من أن هذا المسار صحيح على جهازك
try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print("INFO: Tesseract path set successfully.")
except Exception as e:
    print(f"WARNING: Could not set Tesseract path. Make sure Tesseract is in your system's PATH. Details: {e}")


def extract_text_from_image(image_path):
    """
    تستخدم الكود الخاص بك لاستخراج النص من صورة.
    """
    try:
        # Load image using OpenCV
        img = cv2.imread(image_path)

        # Preprocessing for better OCR accuracy
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # OCR with Arabic and English support
        custom_config = r'--oem 3 --psm 6'
        extracted_text = pytesseract.image_to_string(gray, lang='ara+eng', config=custom_config).strip()
        
        return extracted_text

    except Exception as e:
        print(f"ERROR: Could not perform OCR on image '{image_path}'. Details: {e}")
        return ""


def create_safe_filename_from_text(text, num_words=2):
    """
    تستخدم الكود الخاص بك لإنشاء اسم ملف آمن من النص.
    """
    if not text:
        return "Document"

    # Extract first few words for file naming
    words = text.split()
    if len(words) >= num_words:
        file_prefix = "_".join(words[:num_words])
    elif words:
        file_prefix = words[0]
    else:
        return "Document"

    # Sanitize file name (remove invalid characters)
    # هذه الطريقة باستخدام re أفضل قليلاً
    file_prefix = re.sub(r'[^\w\s-]', '', file_prefix).strip()
    
    return file_prefix if file_prefix else "Document"