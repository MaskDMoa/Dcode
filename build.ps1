$ErrorActionPreference = "Stop"

$projectRoot = $PSScriptRoot
$localPython = Join-Path $projectRoot ".venv\Scripts\python.exe"
$parentPython = Join-Path (Split-Path $projectRoot -Parent) ".venv\Scripts\python.exe"

if (Test-Path -LiteralPath $localPython) {
    $python = $localPython
} elseif (Test-Path -LiteralPath $parentPython) {
    $python = $parentPython
} else {
    $python = (Get-Command python -ErrorAction Stop).Source
}

Push-Location $projectRoot
try {
    & $python -m PyInstaller `
        --noconfirm `
        --clean `
        --onefile `
        --windowed `
        --collect-all customtkinter `
        --name Dcode `
        --distpath dist `
        --workpath build `
        --specpath build `
        app.py

    if ($LASTEXITCODE -ne 0) {
        throw "PyInstaller terminou com codigo $LASTEXITCODE."
    }
} finally {
    Pop-Location
}

Write-Host "Executavel criado em: $(Join-Path $projectRoot 'dist\Dcode.exe')"
