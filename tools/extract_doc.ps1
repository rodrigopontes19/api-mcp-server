param(
    [Parameter(Mandatory=$true)]
    [string]$Path
)

python .\tools\extract_doc.py $Path
