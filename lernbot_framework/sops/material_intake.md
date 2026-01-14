# SOP: Material Intake

Schritt-für-Schritt-Anleitung zur Aufnahme von Unterrichtsmaterial in ein Bot-Projekt.

## Zweck

Diese SOP beschreibt, wie Unterrichtsmaterial für die Lernbot-Erstellung vorbereitet und im Projektordner organisiert wird.

## Voraussetzungen

- Digitales Unterrichtsmaterial (PDF, Word, Excel, etc.)
- Klarheit über Zielgruppe und Lernziele
- Projektordner angelegt (aus `_vorlage/` kopiert)

---

## Schritte

### 1. Projektordner vorbereiten

**Zeitaufwand:** 1 Minute

```powershell
# Vorlage kopieren
Copy-Item -Recurse "lernbot_framework/projekte/_vorlage" "lernbot_framework/projekte/{{PROJEKT_NAME}}"
```

**Namenskonvention:** `{{DATUM}}_{{FACH}}_{{THEMA}}`
- Beispiel: `2026-01_Gastro_Wareneinkauf`

### 2. Material sammeln

**Zeitaufwand:** 5-10 Minuten

Sammle alle relevanten Materialien:
- Aufgabenblätter
- Rezepte/Formeln/Tabellen
- Hintergrundinformationen
- Bestehende Bewertungsbögen (falls vorhanden)

Prüfe die Formate:
- ✅ PDF, DOCX, XLSX, MD, TXT
- ⚠️ Scans → OCR erforderlich
- ❌ Videos → Transkription erforderlich

### 3. Material ablegen

**Zeitaufwand:** 2-5 Minuten

Lege alle Dateien ab in:
```
lernbot_framework/projekte/{{PROJEKT_NAME}}/01_material/
```

**Dateinamen-Konvention** (optional):
```
{{NR}}_{{TYP}}_{{BESCHREIBUNG}}.{{EXT}}
```
Beispiele:
- `01_Aufgabenblatt_Wareneinkauf.docx`
- `02_Rezept_Pannfisch.pdf`
- `03_Tabelle_Lagerbestand.xlsx`

### 4. `_meta.yaml` ausfüllen

**Zeitaufwand:** 10-15 Minuten

Öffne `01_material/_meta.yaml` und ersetze **alle** `{{PLATZHALTER}}`:

```yaml
# === PROJEKT-INFORMATIONEN ===
projekt:
  name: "{{Projektname}}"
  erstellt_am: "{{YYYY-MM-DD}}"
  erstellt_von: "{{Dein Name}}"
  version: "v1.0"

# === BOT-KONFIGURATION ===
bot:
  name: "{{Bot-Name}}"
  tonalitaet: "freundlich"    # freundlich | formal | motivierend
  sprachniveau: "B1"          # B1 | B2 | C1
  standard_modus: "Schüler*innen-Modus"

# === KURS-INFORMATIONEN ===
kurs:
  fach: "{{Fachbereich}}"
  modul: "{{Modulname}}"
  zielgruppe: "{{Beschreibung der Zielgruppe}}"
  voraussetzungen: "{{Benötigtes Vorwissen}}"

# === LERNZIELE ===
lernziele:
  hauptziel: "{{Was sollen die Lernenden am Ende können?}}"
  teilziele:
    - "{{Teilziel 1}}"
    - "{{Teilziel 2}}"
    - "{{Teilziel 3}}"

# === MATERIAL-INVENTAR ===
materialien:
  - datei: "{{Dateiname}}"
    typ: "{{Aufgabenblatt|Rezept|Tabelle|Hintergrund|Bewertung}}"
    beschreibung: "{{Kurzbeschreibung}}"
    wichtigkeit: "{{Kern|Ergänzend|Optional}}"
```

### 5. Qualitäts-Check

**Zeitaufwand:** 5 Minuten

| Kriterium | Status |
|-----------|--------|
| Alle Materialien in `01_material/` vorhanden | ☐ |
| `_meta.yaml` vollständig ausgefüllt | ☐ |
| Keine `{{PLATZHALTER}}` mehr in `_meta.yaml` | ☐ |
| Lernziele mit mind. 3 Teilzielen | ☐ |
| Alle Dateien lesbar/nicht beschädigt | ☐ |

### 6. Projekt-README aktualisieren

**Zeitaufwand:** 2 Minuten

Öffne `projekte/{{PROJEKT_NAME}}/README.md` und aktualisiere:
- Bot-Name
- Fach
- Zielgruppe
- Status Phase 1: ✅ Fertig

---

## Checkliste

```markdown
## Intake-Checkliste für {{PROJEKT_NAME}}

- [ ] Projektordner aus _vorlage/ kopiert
- [ ] Material gesammelt und abgelegt
- [ ] `_meta.yaml` vollständig ausgefüllt
- [ ] Qualitäts-Check bestanden
- [ ] Projekt-README aktualisiert

Abgeschlossen am: {{Datum}}
Bearbeiter: {{Name}}
```

---

## Nächster Schritt

Nach erfolgreichem Intake → **Material-Analyst** aufrufen

Prompt:
```markdown
Analysiere das Material in:
`lernbot_framework/projekte/{{PROJEKT_NAME}}/01_material/`

Speichere die Analyse in:
`lernbot_framework/projekte/{{PROJEKT_NAME}}/02_analyse/material_analyse.md`
```

---

## Häufige Probleme

| Problem | Lösung |
|---------|--------|
| Material nur als Scan | OCR-Tool verwenden (Adobe Acrobat, Tesseract) |
| Unklare Lernziele | Rücksprache mit Fachexperte/Dozent |
| Material zu umfangreich | In mehrere Bot-Projekte aufteilen |
| Fehlende Bewertungskriterien | Script-Generator erstellt diese automatisch |
