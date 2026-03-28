from pathlib import Path
import sys

TEXT_EXTS = {".txt", ".md", ".json", ".csv", ".xml", ".yaml", ".yml", ".log"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".tiff"}


def read_text_file(path):
    return path.read_text(encoding="utf-8", errors="ignore")


def read_docx(path):
    from docx import Document
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)


def read_pdf(path):
    from pypdf import PdfReader
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def read_image(path):
    try:
        import pytesseract
        from PIL import Image
        return pytesseract.image_to_string(Image.open(path))
    except Exception:
        return "OCR not available"


def main():
    if len(sys.argv) < 2:
        print("Usage: extract_doc.py <file>")
        return

    file = Path(sys.argv[1])
    ext = file.suffix.lower()

    if ext in TEXT_EXTS:
        content = read_text_file(file)
    elif ext == ".docx":
        content = read_docx(file)
    elif ext == ".pdf":
        content = read_pdf(file)
    elif ext in IMAGE_EXTS:
        content = read_image(file)
    else:
        content = "Unsupported file type"

    out_dir = Path("_extracted")
    out_dir.mkdir(exist_ok=True)

    out_file = out_dir / f"{file.stem}.txt"
    out_file.write_text(content, encoding="utf-8")

    print(f"Saved: {out_file}")


if __name__ == "__main__":
    main()
