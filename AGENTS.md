# AGENTS.md

## Mission
You are operating inside Antigravity and must use the local Windows PowerShell terminal as the primary execution environment.

Your job is to read, extract, transform, compare, summarize, and analyze project files safely and reproducibly.

## Environment
- Primary shell: Windows PowerShell
- Assume the working directory is the project root
- Prefer local commands over speculation
- If a file is binary or semi-structured, extract it to plain text before analysis

## General rules
1. Be explicit and deterministic.
2. Do not invent file contents.
3. If a file cannot be parsed, report the failure clearly.
4. Prefer reading generated `.txt` outputs over trying to reason directly from binary files.
5. Before destructive actions, ask for confirmation.
6. At the end of each task, report:
   - commands executed
   - files read
   - files generated
   - any failures or limitations

## File handling policy

### Read directly
Read directly when the file is plain text or code, including:
- `.txt`
- `.md`
- `.json`
- `.csv`
- `.xml`
- `.yaml`
- `.yml`
- `.log`
- `.ini`
- source code files

### Extract before reading
For these file types, first extract to text:
- `.pdf`
- `.docx`
- image files: `.png`, `.jpg`, `.jpeg`, `.tif`, `.tiff`, `.bmp`, `.webp`

Use this command:

```powershell
.\\tools\\extract_doc.ps1 <FILE_PATH>
```

Then read the corresponding output in:

```text
.\\_extracted\\
```

## Directory policy
If needed, ensure these directories exist:
- `tools`
- `_extracted`

Use:

```powershell
New-Item -ItemType Directory tools -Force | Out-Null
New-Item -ItemType Directory _extracted -Force | Out-Null
```

## Extraction workflow
When the user asks to analyze a PDF, DOCX, or image:

1. Identify the file path
2. Run:
   ```powershell
   .\\tools\\extract_doc.ps1 <FILE_PATH>
   ```
3. Locate the extracted `.txt` file inside `.\\_extracted\\`
4. Read the extracted text
5. Perform the requested task on the extracted text
6. Report what was done

## Comparison workflow
If the user asks to compare files:
1. Extract any binary documents first
2. Read all resulting text files
3. Compare structure, meaning, obligations, dates, risks, numbers, and inconsistencies
4. Present differences clearly

## Summarization workflow
If the user asks for a summary:
1. Extract if needed
2. Read the resulting text
3. Summarize in a structured way
4. Preserve key obligations, values, deadlines, and risks

## OCR and parsing expectations
- If OCR or parsing fails, do not fabricate output
- State exactly what failed
- Show the command attempted
- Suggest the next practical step

## PowerShell behavior
Use PowerShell syntax when running commands.
Prefer commands like:

```powershell
.\\tools\\extract_doc.ps1 .\\docs\\contract.pdf
Get-ChildItem .\\_extracted
Get-Content .\\_extracted\\contract.txt
```

## Safety
- Do not delete source documents unless explicitly asked
- Do not overwrite source files unless explicitly asked
- Write derived outputs into `_extracted` or another clearly named output file

## Response format
When completing a task, answer with:
1. What you did
2. Which files were processed
3. Which commands were run
4. The actual result requested by the user
5. Any limitations

## Dependencies
The extraction scripts expect these tools/libraries when relevant:
- Python 3
- `pymupdf`
- `pypdf`
- `pillow`
- `python-docx`
- Tesseract OCR in `PATH` for scanned PDFs and images

## Examples

### Example 1
User request:
"Summarize .\\docs\\contrato.pdf"

Expected behavior:
1. Run:
   ```powershell
   .\\tools\\extract_doc.ps1 .\\docs\\contrato.pdf
   ```
2. Read the extracted text in `_extracted`
3. Summarize it

### Example 2
User request:
"Compare .\\docs\\proposta.docx with .\\docs\\escopo.txt"

Expected behavior:
1. Extract the DOCX
2. Read both texts
3. Compare them
4. Report differences, gaps, and risks

### Example 3
User request:
"Extract text from .\\docs\\receipt.jpg and create a markdown table"

Expected behavior:
1. Run extraction
2. Read extracted text
3. Convert relevant content into markdown table

## Priority
Follow this AGENTS.md by default.
If the user gives direct instructions that conflict with this file, follow the user.
