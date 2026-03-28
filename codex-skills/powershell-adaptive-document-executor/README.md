# PowerShell Adaptive Document Executor (Codex Skill)

This folder contains a ready-to-use Codex skill for deterministic PowerShell execution with document processing capabilities.

## Installation

Copy this entire folder to your local Codex skills directory:

```
C:\Users\rodrigo.costa\.codex\skills\powershell-adaptive-document-executor
```

## Required structure

```
powershell-adaptive-document-executor
│
├── SKILL.md
├── tools
├── _extracted
```

Create missing folders if needed.

## Dependencies

Install Python packages:

```
pip install pymupdf pypdf pillow python-docx pandas python-pptx
```

## OCR (optional but recommended)

Install Tesseract OCR:

https://github.com/tesseract-ocr/tesseract

Ensure it is added to PATH.

## Usage Example

Inside Codex:

```
Use the skill powershell-adaptive-document-executor.

Extract and analyze:
".\\Logo Ponta Negra - Manual da Marca.pdf"
```

## Notes

- This skill enforces PowerShell-only execution
- Avoid mixing WSL or bash
- Ensure Python is accessible in PATH
