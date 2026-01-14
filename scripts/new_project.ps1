<#
.SYNOPSIS
    Erstellt ein neues Lernbot-Projekt aus der Vorlage.

.DESCRIPTION
    Kopiert die Projektvorlage aus lernbot_framework/projekte/_vorlage
    in einen neuen Projektordner und bereitet ihn für die Nutzung vor.

.PARAMETER Name
    Name des neuen Projekts (z.B. "2026-01_Gastro_Wareneinkauf")

.PARAMETER Description
    Optionale Kurzbeschreibung des Projekts

.EXAMPLE
    .\new_project.ps1 -Name "2026-01_Gastro_Wareneinkauf"
    
.EXAMPLE
    .\new_project.ps1 -Name "2026-01_Gastro_Wareneinkauf" -Description "Lernbot für Wareneingang"

.NOTES
    Bot-Building Framework - Projekt-Automatisierung
#>

param(
    [Parameter(Mandatory=$true)]
    [ValidatePattern('^[a-zA-Z0-9_\-]+$')]
    [string]$Name,
    
    [Parameter(Mandatory=$false)]
    [string]$Description = ""
)

# Konfiguration
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptPath
$templatePath = Join-Path $projectRoot "lernbot_framework\projekte\_vorlage"
$projectsPath = Join-Path $projectRoot "lernbot_framework\projekte"
$newProjectPath = Join-Path $projectsPath $Name

# Prüfe ob Vorlage existiert
if (-not (Test-Path $templatePath)) {
    Write-Host "[FEHLER] Vorlage nicht gefunden: $templatePath" -ForegroundColor Red
    exit 1
}

# Prüfe ob Projekt bereits existiert
if (Test-Path $newProjectPath) {
    Write-Host "[FEHLER] Projekt existiert bereits: $newProjectPath" -ForegroundColor Red
    Write-Host "         Waehle einen anderen Namen oder loesche das bestehende Projekt." -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   NEUES LERNBOT-PROJEKT ERSTELLEN     " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Projektname:    $Name" -ForegroundColor White
Write-Host "  Beschreibung:   $(if($Description) {$Description} else {'(keine)'})" -ForegroundColor White
Write-Host "  Zielpfad:       $newProjectPath" -ForegroundColor White
Write-Host ""

# Kopiere Vorlage
Write-Host "[1/4] Kopiere Projektvorlage..." -ForegroundColor Yellow
try {
    Copy-Item -Path $templatePath -Destination $newProjectPath -Recurse -Force
    Write-Host "      [OK] Vorlage kopiert" -ForegroundColor Green
} catch {
    Write-Host "      [FEHLER] Kopieren fehlgeschlagen: $_" -ForegroundColor Red
    exit 1
}

# Erstelle Projekt-README
Write-Host "[2/4] Erstelle Projekt-README..." -ForegroundColor Yellow
$readmeContent = @"
# Projekt: $Name

$(if($Description) {"**Beschreibung:** $Description`n"})
**Erstellt:** $(Get-Date -Format "yyyy-MM-dd HH:mm")

## Status

- [ ] 01_material - Material abgelegt
- [ ] 01_material - _meta.yaml ausgefuellt
- [ ] 02_analyse - Analyse durchgefuehrt
- [ ] 03_scripts - Scripts generiert
- [ ] 04_system_prompt - Prompt erstellt
- [ ] 05_quality - Qualitaetspruefung bestanden
- [ ] 06_export - Export erstellt
- [ ] 07_test - Tests durchgefuehrt

## Naechste Schritte

1. Lade dein Unterrichtsmaterial in ``01_material/`` hoch
2. Fuege ``_meta.yaml`` aus (Bot-Konfiguration)
3. Starte die Analyse mit:

   > "Analysiere das Material in ``projekte/$Name/01_material/``"

## Notizen

<!-- Hier kannst du Notizen zum Projekt hinterlassen -->
"@
$readmePath = Join-Path $newProjectPath "README.md"
Set-Content -Path $readmePath -Value $readmeContent -Encoding UTF8
Write-Host "      [OK] README erstellt" -ForegroundColor Green

# Aktualisiere _meta.yaml mit Projektnamen
Write-Host "[3/4] Aktualisiere Metadaten..." -ForegroundColor Yellow
$metaPath = Join-Path $newProjectPath "01_material\_meta.yaml"
if (Test-Path $metaPath) {
    $metaContent = Get-Content -Path $metaPath -Raw -Encoding UTF8
    $metaContent = $metaContent -replace 'bot_name: ".*"', "bot_name: `"$Name`""
    $metaContent = $metaContent -replace 'projekt_name: ".*"', "projekt_name: `"$Name`""
    Set-Content -Path $metaPath -Value $metaContent -Encoding UTF8
    Write-Host "      [OK] _meta.yaml aktualisiert" -ForegroundColor Green
} else {
    Write-Host "      [WARNUNG] _meta.yaml nicht gefunden" -ForegroundColor Yellow
}

# Entferne .gitkeep-Dateien (optional)
Write-Host "[4/4] Bereinige Platzhalter-Dateien..." -ForegroundColor Yellow
$gitkeepFiles = Get-ChildItem -Path $newProjectPath -Filter ".gitkeep" -Recurse -Force
foreach ($file in $gitkeepFiles) {
    Remove-Item $file.FullName -Force
}
Write-Host "      [OK] $($gitkeepFiles.Count) .gitkeep-Dateien entfernt" -ForegroundColor Green

# Zusammenfassung
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   PROJEKT ERFOLGREICH ERSTELLT!       " -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Naechste Schritte:" -ForegroundColor White
Write-Host "  1. Lade Material in:" -ForegroundColor White
Write-Host "     $newProjectPath\01_material\" -ForegroundColor Cyan
Write-Host ""
Write-Host "  2. Fuege '_meta.yaml' aus" -ForegroundColor White
Write-Host ""
Write-Host "  3. Starte die Analyse:" -ForegroundColor White
Write-Host "     'Analysiere das Material in projekte/$Name/01_material/'" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Dokumentation:" -ForegroundColor White
Write-Host "     lernbot_framework\guides\quickstart.md" -ForegroundColor Cyan
Write-Host ""
