# 🚀 Quickstart: Lernbot-Framework

Willkommen! Diese Anleitung führt dich Schritt für Schritt durch die Erstellung deines ersten Lernassistenz-Bots.

---

## 📋 Übersicht

| Schritt | Was du tust | Ordner | Zeitaufwand |
|---------|-------------|--------|-------------|
| 0 | Projekt anlegen | `projekte/` | 1 Min |
| 1 | Material vorbereiten | `01_material/` | 10-15 Min |
| 2 | Material analysieren | `02_analyse/` | 15-30 Min |
| 3 | Scripts generieren | `03_scripts/` | 30-60 Min |
| 4 | System-Prompt bauen | `04_system_prompt/` | 10-20 Min |
| 5 | Qualität prüfen | `05_quality/` | 10-15 Min |
| 6 | Exportieren | `06_export/` | 5 Min |
| **Gesamt** | | | **~1,5-2,5 Std** |

---

## Schritt 0: Projekt anlegen

### Projekt-Vorlage kopieren

```powershell
# PowerShell
Copy-Item -Recurse "lernbot_framework/projekte/_vorlage" "lernbot_framework/projekte/MEIN_PROJEKT"
```

**Namenskonvention:** `{{DATUM}}_{{FACH}}_{{THEMA}}`
- Beispiel: `2026-01_Gastro_Wareneinkauf`

### Projektstruktur

Nach dem Kopieren hast du:

```
projekte/MEIN_PROJEKT/
├── README.md              ← Projekt-Status & Checkliste
├── 01_material/           ← Hier dein Material ablegen
│   ├── _meta.yaml         ← Bot-Konfiguration ausfüllen
│   └── README.md
├── 02_analyse/            ← Analyse speichern
├── 03_scripts/            ← Scripts speichern
├── 04_system_prompt/      ← Prompt speichern
├── 05_quality/            ← Report speichern
└── 06_export/             ← Finale Version
```

---

## Schritt 1: Material vorbereiten

### Arbeitsordner: `01_material/`

### Was du brauchst
- Unterrichtsmaterial (PDF, Word, Excel, MD, TXT)
- Klare Vorstellung der Lernziele
- 10-15 Minuten Zeit

### So gehst du vor

#### 1.1 Material ablegen

Lege alle relevanten Dateien in `01_material/`:
- Aufgabenblätter
- Rezepte/Formeln/Tabellen
- Hintergrundinformationen
- Bewertungsbögen (falls vorhanden)

#### 1.2 `_meta.yaml` ausfüllen

Öffne `01_material/_meta.yaml` und ersetze alle `{{PLATZHALTER}}`:

```yaml
# === PROJEKT-INFORMATIONEN ===
projekt:
  name: "{{Projektname}}"
  erstellt_am: "{{YYYY-MM-DD}}"
  erstellt_von: "{{Dein Name}}"

# === BOT-KONFIGURATION ===
bot:
  name: "{{Bot-Name, z.B. LernBuddy}}"
  tonalitaet: "freundlich"          # freundlich | formal | motivierend
  sprachniveau: "B1"                # B1 | B2 | C1
  standard_modus: "Schüler*innen-Modus"

# === KURS-INFORMATIONEN ===
kurs:
  fach: "{{Fachbereich}}"
  modul: "{{Modulname}}"
  zielgruppe: "{{z.B. Berufsschüler Gastronomie, 2. Lehrjahr}}"
  voraussetzungen: "{{Benötigtes Vorwissen}}"

# === LERNZIELE ===
lernziele:
  hauptziel: "{{Was sollen die Lernenden am Ende können?}}"
  teilziele:
    - "{{Teilziel 1}}"
    - "{{Teilziel 2}}"
    - "{{Teilziel 3}}"

# === MATERIAL-LISTE ===
materialien:
  - datei: "{{Dateiname.pdf}}"
    typ: "{{Aufgabenblatt|Rezept|Tabelle|Hintergrund}}"
    beschreibung: "{{Kurzbeschreibung}}"
```

### ✅ Checkliste Schritt 1
- [ ] Material in `01_material/` abgelegt
- [ ] `_meta.yaml` vollständig ausgefüllt
- [ ] Alle Platzhalter ersetzt

---

## Schritt 2: Material analysieren

### Arbeitsordner: `02_analyse/`

### Was passiert hier
Der **Material-Analyst** liest dein Material und extrahiert:
- Lernziele
- Aufgaben-Strukturen
- Ressourcen (Tabellen, Rezepte, etc.)
- Bewertungskriterien

### Prompt für Material-Analyst

```markdown
# Auftrag: Material-Analyse

Analysiere das Material im Projektordner und erstelle eine strukturierte Analyse.

## Projektpfad
`lernbot_framework/projekte/MEIN_PROJEKT/`

## Metadaten
Lies: `01_material/_meta.yaml`

## Material
Analysiere alle Dateien in: `01_material/`

---

Erstelle die Analyse nach dem Schema in `agents/material_analyst.md`:
1. Metadaten erfassen
2. Lernziele mit Bloom-Stufen verknüpfen
3. Aufgaben identifizieren
4. Ressourcen katalogisieren
5. Bewertungskriterien erkennen
6. Lücken dokumentieren

Speichere das Ergebnis als: `02_analyse/material_analyse.md`
```

### ✅ Checkliste Schritt 2
- [ ] Material-Analyst ausgeführt
- [ ] `02_analyse/material_analyse.md` gespeichert
- [ ] Lücken dokumentiert

---

## Schritt 3: Scripts generieren

### Arbeitsordner: `03_scripts/`

### Was passiert hier
Der **Script-Generator** wandelt die Analyse in strukturierte Script-Blöcke um.

### Prompt für Script-Generator

```markdown
# Auftrag: Script-Generierung

Generiere alle Script-Blöcke basierend auf der Material-Analyse.

## Eingaben
- Analyse: `02_analyse/material_analyse.md`
- Konfiguration: `01_material/_meta.yaml`

## Ausgabe
Speichere als: `03_scripts/scripts_komplett.md`

---

Generiere:
1. META-Block
2. PHASE-Blöcke
3. RESOURCE-Blöcke
4. TASK-Blöcke (mit Scaffolds)
5. RUBRIC-Blöcke
6. MODEL-Blöcke (optional)
7. DEBRIEF-Block

Verwende das Format aus `templates/script_vorlage_komplett.md`
```

### ✅ Checkliste Schritt 3
- [ ] Script-Generator ausgeführt
- [ ] `03_scripts/scripts_komplett.md` gespeichert
- [ ] Alle Block-Typen vorhanden
- [ ] IDs eindeutig, Referenzen gültig

---

## Schritt 4: System-Prompt bauen

### Arbeitsordner: `04_system_prompt/`

### Was passiert hier
Der **Prompt-Builder** kombiniert alle Scripts zu einem finalen System-Prompt.

### Prompt für Prompt-Builder

```markdown
# Auftrag: System-Prompt Assembly

Kombiniere die Scripts zu einem finalen System-Prompt.

## Eingaben
- Scripts: `03_scripts/scripts_komplett.md`
- Konfiguration: `01_material/_meta.yaml`
- Basis-Template: `templates/scripts/system_prompt_base.md`

## Ausgabe
Speichere als: `04_system_prompt/system_prompt.md`

---

Der Output soll direkt in eine LLM-Plattform kopierbar sein.
Ersetze alle {{PLATZHALTER}} mit Werten aus der Konfiguration.
```

### ✅ Checkliste Schritt 4
- [ ] Prompt-Builder ausgeführt
- [ ] `04_system_prompt/system_prompt.md` gespeichert
- [ ] Keine `{{PLATZHALTER}}` mehr vorhanden

---

## Schritt 5: Qualität prüfen

### Arbeitsordner: `05_quality/`

### Was passiert hier
Der **Quality-Checker** validiert den System-Prompt vor dem Einsatz.

### Prompt für Quality-Checker

```markdown
# Auftrag: Quality-Check

Prüfe den System-Prompt auf Qualität und Konsistenz.

## Eingaben
- System-Prompt: `04_system_prompt/system_prompt.md`
- Scripts: `03_scripts/scripts_komplett.md`
- Original-Material: `01_material/`

## Ausgabe
Speichere als: `05_quality/quality_report.md`

---

Prüfe:
1. Strukturelle Konsistenz (IDs, Referenzen, Block-Syntax)
2. Didaktische Qualität (Lernziele, Scaffolds, Feedback)
3. Inhaltliche Korrektheit
4. Technische Qualität (Formatierung, Token-Limit)

Erstelle einen Report mit Freigabe-Empfehlung.
```

### Freigabe-Stufen

| Status | Bedeutung | Aktion |
|--------|-----------|--------|
| ✅ FREIGEGEBEN | Keine kritischen Fehler | → Schritt 6 |
| ⚠️ ÜBERARBEITUNG | Behebbare Fehler | → Zurück zu Schritt 3/4 |
| ❌ ABGELEHNT | Fundamentale Probleme | → Zurück zu Schritt 1/2 |

### ✅ Checkliste Schritt 5
- [ ] Quality-Checker ausgeführt
- [ ] `05_quality/quality_report.md` gespeichert
- [ ] Freigabe erhalten

---

## Schritt 6: Exportieren

### Arbeitsordner: `06_export/`

### Was passiert hier
Du erstellst die finale Version für den produktiven Einsatz.

### So gehst du vor

1. **Kopieren**: System-Prompt aus `04_system_prompt/` kopieren
2. **Bereinigen**: Falls nötig, Markdown-Formatierungen anpassen
3. **Testen**: In LLM-Plattform einfügen und Testdialog durchführen
4. **Dokumentieren**: Einsatznotizen in `06_export/README.md`

### ✅ Checkliste Schritt 6
- [ ] `FINAL_system_prompt.txt` erstellt
- [ ] In LLM-Plattform getestet
- [ ] Projekt-README aktualisiert (Status: ✅ Fertig)

---

## 🎉 Fertig!

Dein Lernbot ist einsatzbereit!

### Projekt-Artefakte

```
projekte/MEIN_PROJEKT/
├── 01_material/
│   ├── _meta.yaml          ✓ Konfiguration
│   └── {{material}}        ✓ Original-Material
├── 02_analyse/
│   └── material_analyse.md ✓ Analyse
├── 03_scripts/
│   └── scripts_komplett.md ✓ Scripts
├── 04_system_prompt/
│   └── system_prompt.md    ✓ Prompt
├── 05_quality/
│   └── quality_report.md   ✓ Report
└── 06_export/
    └── FINAL_system_prompt.txt ✓ EINSATZBEREIT
```

---

## 📚 Weiterführende Dokumentation

| Dokument | Pfad |
|----------|------|
| Agenten-Beschreibungen | `lernbot_framework/agents/` |
| Script-Templates | `lernbot_framework/templates/scripts/` |
| Vollständige Vorlage | `templates/script_vorlage_komplett.md` |
| Workflow-Details | `processes/bot_creation.md` |
| Beispielprojekt | `projekte/Beispiel_Tagung_Dock03/` |

---

## ❓ Häufige Fragen

### Wie lange dauert die Erstellung?
- Erstes Mal: 2-3 Stunden
- Mit Übung: 1-1,5 Stunden
- Bei ähnlichem Material: 30-60 Minuten

### Was, wenn Material fehlt?
Der Material-Analyst markiert Lücken mit `{{PLACEHOLDER}}`. Du kannst:
1. Material nachliefern
2. Platzhalter manuell ausfüllen
3. Scripts ohne diese Teile generieren

### Kann ich den Bot anpassen?
Ja! Ändere:
- Tonalität in `_meta.yaml`
- Scaffolds in TASK-Blöcken
- Kriterien in RUBRIC-Blöcken
- Reflexionsfragen in DEBRIEF-Block

### Wo finde ich ein Beispiel?
Schau dir das Beispielprojekt an:
```
lernbot_framework/projekte/Beispiel_Tagung_Dock03/
```
