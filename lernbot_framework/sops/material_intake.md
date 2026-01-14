# SOP: Material Intake

Schritt-für-Schritt-Anleitung zur Aufnahme von Unterrichtsmaterial.

## Zweck

Diese SOP beschreibt, wie Unterrichtsmaterial für die Lernbot-Erstellung vorbereitet und dokumentiert wird.

## Voraussetzungen

- Digitales Unterrichtsmaterial (PDF, Word, Excel, etc.)
- Klarheit über Zielgruppe und Lernziele
- Zugang zum Framework-Repository

## Schritte

### 1. Material sammeln

**Zeitaufwand:** 5-10 Minuten

1. Sammle alle relevanten Materialien:
   - Aufgabenblätter
   - Rezepte/Formeln/Tabellen
   - Hintergrundinformationen
   - Bestehende Bewertungsbögen (falls vorhanden)

2. Prüfe die Formate:
   - ✅ PDF, DOCX, XLSX, MD, TXT
   - ⚠️ Scans → OCR erforderlich
   - ❌ Videos → Transkription erforderlich

3. Lege alle Dateien ab in:
   ```
   docs/Vorlagen/{{Projektname}}/
   ```

### 2. Material benennen

**Zeitaufwand:** 2-5 Minuten

Verwende einheitliche Dateinamen:

```
{{NR}}_{{TYP}}_{{BESCHREIBUNG}}_v{{VERSION}}.{{EXT}}
```

Beispiele:
- `01_Aufgabenblatt_Wareneinkauf_v1.docx`
- `02_Rezept_Pannfisch_v1.pdf`
- `03_Tabelle_Lagerbestand_v1.xlsx`

### 3. Metadaten erfassen

**Zeitaufwand:** 10-15 Minuten

Erstelle eine Datei `_meta.yaml` im Projektordner:

```yaml
# Projekt-Metadaten
projekt:
  name: "{{Projektname}}"
  erstellt_am: "{{YYYY-MM-DD}}"
  erstellt_von: "{{Name}}"

# Bot-Konfiguration
bot:
  name: "{{Bot-Name, z.B. SIMcoach}}"
  tonalitaet: "{{formal|freundlich|motivierend}}"
  sprachniveau: "{{B1|B2|C1}}"
  standard_modus: "Schüler*innen-Modus"

# Kurs-Informationen
kurs:
  fach: "{{Fachbereich}}"
  modul: "{{Modulname}}"
  zielgruppe: "{{Beschreibung, z.B. 'Berufsschüler Gastronomie, 2. LJ'}}"
  voraussetzungen: "{{Benötigtes Vorwissen}}"

# Zeitrahmen
zeitrahmen:
  dauer_gesamt: "{{Minuten}}"
  anzahl_phasen: "{{Geschätzt}}"

# Material-Inventar
materialien:
  - datei: "{{Dateiname}}"
    typ: "{{Aufgabe|Rezept|Tabelle|Hintergrund|Bewertung}}"
    beschreibung: "{{Kurzbeschreibung}}"
    wichtigkeit: "{{Kern|Ergänzend|Optional}}"
```

### 4. Lernziele definieren

**Zeitaufwand:** 10-20 Minuten

Erstelle eine Liste der Lernziele in `_lernziele.md`:

```markdown
# Lernziele für {{Projektname}}

## Hauptziel
{{Ein Satz: Was sollen die Lernenden am Ende können?}}

## Teilziele

### Wissen (Bloom 1)
- [ ] {{Die Lernenden können ... benennen/beschreiben}}

### Verstehen (Bloom 2)
- [ ] {{Die Lernenden können ... erklären/interpretieren}}

### Anwenden (Bloom 3)
- [ ] {{Die Lernenden können ... anwenden/berechnen}}

### Analysieren (Bloom 4)
- [ ] {{Die Lernenden können ... vergleichen/unterscheiden}}

### Bewerten (Bloom 5)
- [ ] {{Die Lernenden können ... bewerten/begründen}}

### Erschaffen (Bloom 6)
- [ ] {{Die Lernenden können ... entwickeln/erstellen}}
```

### 5. Qualitäts-Check

**Zeitaufwand:** 5 Minuten

Prüfe vor Abschluss:

| Kriterium | Status |
|-----------|--------|
| Alle Materialien digital vorhanden | ☐ |
| Dateien einheitlich benannt | ☐ |
| `_meta.yaml` vollständig ausgefüllt | ☐ |
| `_lernziele.md` mit min. 3 Teilzielen | ☐ |
| Keine unlesbaren/beschädigten Dateien | ☐ |

### 6. Übergabe an Material-Analyst

**Zeitaufwand:** 1 Minute

Starte Phase 2 mit folgendem Prompt:

```markdown
Analysiere das Material im Ordner `docs/Vorlagen/{{Projektname}}/`.

Metadaten: siehe `_meta.yaml`
Lernziele: siehe `_lernziele.md`

Erstelle eine vollständige Material-Analyse gemäß dem Schema in 
`lernbot_framework/agents/material_analyst.md`.
```

## Checkliste

```markdown
## Intake-Checkliste für {{Projektname}}

- [ ] Material gesammelt und abgelegt
- [ ] Dateien einheitlich benannt
- [ ] `_meta.yaml` erstellt
- [ ] `_lernziele.md` erstellt
- [ ] Qualitäts-Check bestanden
- [ ] Übergabe an Material-Analyst

Abgeschlossen am: {{Datum}}
Bearbeiter: {{Name}}
```

## Häufige Probleme

| Problem | Lösung |
|---------|--------|
| Material nur als Scan | OCR-Tool verwenden (z.B. Adobe Acrobat, Tesseract) |
| Unklare Lernziele | Rücksprache mit Fachexperte/Dozent |
| Material zu umfangreich | In mehrere Lernbots aufteilen |
| Fehlende Bewertungskriterien | In Phase 3 vom Script-Generator generieren lassen |
