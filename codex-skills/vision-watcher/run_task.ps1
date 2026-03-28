param(
    [Parameter(Mandatory=$true)]
    [string]$file
)

Write-Host "[ENTRYPOINT] Recebido: $file"

if (!(Test-Path $file)) {
    Write-Host "[ERRO] Arquivo não encontrado"
    exit 1
}

$fullPath = (Resolve-Path $file).Path
Write-Host "[DEBUG] Caminho absoluto: $fullPath"

# Executa analisador
python analisador_universal.py "$fullPath"
