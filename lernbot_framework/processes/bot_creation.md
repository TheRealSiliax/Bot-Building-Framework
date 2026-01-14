# Bot-Creation Workflow

Hauptprozess zur Erstellung eines Lernassistenz-Bots.

> **🚀 Standard-Einstieg:** Beginne immer mit dem **Material-Analyst** Agenten!
> Sage einfach: *"Analysiere das Material in `projekte/PROJEKT_NAME/01_material/`"*

## Prozess-Übersicht

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         BOT-CREATION WORKFLOW                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 1: INTAKE                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Projekt anlegen → Material ablegen → _meta.yaml ausfüllen          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  PHASE 2: ANALYSE (★ STANDARD-EINSTIEG)                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  MATERIAL-ANALYST: Dokumente parsen → Struktur extrahieren          │   │
│  │  Input:  projekte/PROJEKT/01_material/                              │   │
│  │  Output: projekte/PROJEKT/02_analyse/                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  PHASE 3: GENERIERUNG                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  SCRIPT-GENERATOR: META → TASKS → RUBRICS → MODELS → DEBRIEF        │   │
│  │  Input:  projekte/PROJEKT/02_analyse/                               │   │
│  │  Output: projekte/PROJEKT/03_scripts/                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  PHASE 4: ASSEMBLY                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  PROMPT-BUILDER: Scripts kombinieren → System-Prompt erstellen      │   │
│  │  Input:  projekte/PROJEKT/03_scripts/                               │   │
│  │  Output: projekte/PROJEKT/04_system_prompt/                         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  PHASE 5: VALIDIERUNG                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  QUALITY-CHECKER: Prüfen → Freigeben oder Iteration                 │   │
│  │  Input:  projekte/PROJEKT/04_system_prompt/                         │   │
│  │  Output: projekte/PROJEKT/05_quality/                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  PHASE 6: EXPORT                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Finaler System-Prompt → Export-Ready Version                       │   │
│  │  Output: projekte/PROJEKT/06_export/                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  PHASE 7: TEST                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Testszenarien durchführen → Ergebnisse dokumentieren               │   │
│  │  Output: projekte/PROJEKT/07_test/                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Projekt-Ordner-Struktur

Jedes Projekt liegt in `lernbot_framework/projekte/` und folgt dieser Struktur:

```
projekte/PROJEKT_NAME/
├── 01_material/           # Eingabe: Rohmaterialien + Metadaten
│   ├── _meta.yaml         # Bot-Konfiguration und Metadaten
│   └── *.pdf/.docx/.md    # Unterrichtsmaterialien
├── 02_analyse/            # Output Material-Analyst
│   └── analyse.md         # Strukturierte Analyse
├── 03_scripts/            # Output Script-Generator
│   ├── meta_block.md
│   ├── phase_blocks.md
│   ├── task_blocks.md
│   ├── rubric_blocks.md
│   ├── model_blocks.md
│   └── debrief_block.md
├── 04_system_prompt/      # Output Prompt-Builder
│   └── system_prompt.md   # Finaler System-Prompt
├── 05_quality/            # Output Quality-Checker
│   └── quality_report.md  # Qualitätsbericht
├── 06_export/             # Export-Ready Version
│   └── bot_export.md      # Copy-Paste-Ready Prompt
└── 07_test/               # Test-Dokumentation
    ├── testplan.md        # Testszenarien
    └── testergebnisse.md  # Ergebnisse
```

---

## Phase 1: Intake

### Ziel
Alle notwendigen Materialien und Informationen für die Bot-Erstellung sammeln.

### Eingaben
- Unterrichtsmaterial (PDF, Word, Excel, MD, TXT)
- Kurs-/Modulinformationen
- Zielgruppen-Definition
- Zeitrahmen

### Aktivitäten

| Schritt | Aktion | Verantwortlich | Output |
|---------|--------|----------------|--------|
| 1.1 | Neues Projekt anlegen | Ersteller | Projektordner |
| 1.2 | Material in `01_material/` ablegen | Ersteller | Rohmaterial |
| 1.3 | `_meta.yaml` ausfüllen | Ersteller | Metadaten |
| 1.4 | Lernziele definieren/bestätigen | Ersteller | Lernziel-Liste |

### Projekt anlegen

**Option A: Automatisiertes Script**
```powershell
.\scripts\new_project.ps1 -Name "2026-01_Gastro_Wareneinkauf"
```

**Option B: Manuell**
```powershell
Copy-Item -Recurse "lernbot_framework/projekte/_vorlage" "lernbot_framework/projekte/MEIN_PROJEKT"
```

### Akzeptanzkriterien Phase 1
- [ ] Projekt-Ordner angelegt
- [ ] Alle Materialien in `01_material/`
- [ ] `_meta.yaml` vollständig ausgefüllt
- [ ] Lernziele explizit definiert

---

## Phase 2: Analyse (★ STANDARD-EINSTIEG)

> 🎯 **Dies ist der normale Startpunkt!** Nach dem Material-Upload beginnst du hier.

### Ziel
Strukturierte Extraktion aller lernrelevanten Informationen aus dem Rohmaterial.

### Agent
**Material-Analyst** (`agents/material_analyst.md`)

### So startest du

Sage einfach:
> *"Analysiere das Material in `projekte/PROJEKT_NAME/01_material/`"*

Oder:
> *"@material_analyst Starte die Analyse für Projekt XY"*

### Eingaben
- Rohmaterial aus `projekte/PROJEKT/01_material/`
- `_meta.yaml` Konfiguration

### Aktivitäten

| Schritt | Aktion | Output |
|---------|--------|--------|
| 2.1 | Dokumente parsen (Text extrahieren) | Rohtext |
| 2.2 | Lernziele identifizieren | Lernziel-Liste (YAML) |
| 2.3 | Aufgaben erkennen | Aufgaben-Liste (YAML) |
| 2.4 | Ressourcen katalogisieren | Ressourcen-Inventar (YAML) |
| 2.5 | Bewertungskriterien erkennen | Kriterien-Liste (YAML) |
| 2.6 | Lücken dokumentieren | Lücken-Report |

### Output
Strukturierte Material-Analyse wird gespeichert in:
```
projekte/PROJEKT/02_analyse/analyse.md
```

### Akzeptanzkriterien Phase 2
- [ ] Alle Lernziele mit Bloom-Stufe versehen
- [ ] Alle Aufgaben mit Typ und Ressourcen-Bezug
- [ ] Lücken explizit markiert
- [ ] Analyse-Dokument in `02_analyse/` gespeichert

---

## Phase 3: Generierung

### Ziel
Transformation der Analyse in maschinenlesbare Script-Blöcke.

### Agent
**Script-Generator** (`agents/script_generator.md`)

### Eingaben
- Material-Analyse aus `projekte/PROJEKT/02_analyse/`
- Script-Templates aus `templates/scripts/`

### Aktivitäten

| Schritt | Aktion | Template | Output |
|---------|--------|----------|--------|
| 3.1 | META-Block generieren | `meta_template.md` | META-BLOCK |
| 3.2 | PHASE-Struktur erstellen | `phase_template.md` | PHASE-BLOCKs |
| 3.3 | RESOURCE-Blöcke erstellen | `resource_template.md` | RESOURCE-BLOCKs |
| 3.4 | TASK-Blöcke generieren | `task_template.md` | TASK-BLOCKs |
| 3.5 | RUBRIC-Blöcke generieren | `rubric_template.md` | RUBRIC-BLOCKs |
| 3.6 | MODEL-Blöcke generieren | `model_template.md` | MODEL-BLOCKs |
| 3.7 | DEBRIEF-Block generieren | `debrief_template.md` | DEBRIEF-BLOCK |
| 3.8 | Referenz-Mapping erstellen | - | Mapping-Tabelle |

### Generierungs-Reihenfolge

```
META → PHASE → RESOURCE → TASK → RUBRIC → MODEL → DEBRIEF
```

Jeder Block referenziert die vorherigen (z.B. TASK → PHASE, RUBRIC → TASK).

### Output
Alle generierten Scripts werden gespeichert in:
```
projekte/PROJEKT/03_scripts/
```

### Akzeptanzkriterien Phase 3
- [ ] Alle Block-Typen generiert
- [ ] IDs eindeutig und konsistent
- [ ] Alle Referenzen gültig
- [ ] Scripts in `03_scripts/` gespeichert

---

## Phase 4: Assembly

### Ziel
Kombination aller Scripts zu einem finalen System-Prompt.

### Agent
**Prompt-Builder** (`agents/prompt_builder.md`)

### Eingaben
- Generierte Scripts aus `projekte/PROJEKT/03_scripts/`
- Bot-Konfiguration aus `projekte/PROJEKT/01_material/_meta.yaml`
- System-Prompt-Basis-Template

### Aktivitäten

| Schritt | Aktion | Output |
|---------|--------|--------|
| 4.1 | Konfiguration laden | Variablen-Set |
| 4.2 | Scripts formatieren | Formatiertes Script-Dokument |
| 4.3 | Platzhalter ersetzen | Prompt ohne Platzhalter |
| 4.4 | Format optimieren | Finaler Prompt |

### Output
Finaler System-Prompt wird gespeichert in:
```
projekte/PROJEKT/04_system_prompt/system_prompt.md
```

### Akzeptanzkriterien Phase 4
- [ ] Keine `{{...}}` Platzhalter im Output
- [ ] Alle Script-Blöcke integriert
- [ ] Token-Limit nicht überschritten
- [ ] Prompt in `04_system_prompt/` gespeichert

---

## Phase 5: Validierung

### Ziel
Qualitätssicherung vor dem Einsatz.

### Agent
**Quality-Checker** (`agents/quality_checker.md`)

### Eingaben
- Finaler System-Prompt aus `projekte/PROJEKT/04_system_prompt/`
- Generierte Scripts aus `projekte/PROJEKT/03_scripts/`
- Original-Material aus `projekte/PROJEKT/01_material/`

### Aktivitäten

| Schritt | Aktion | Output |
|---------|--------|--------|
| 5.1 | Strukturelle Konsistenz prüfen | Fehler-/Warnungsliste |
| 5.2 | Didaktische Qualität prüfen | Checklisten-Ergebnis |
| 5.3 | Inhaltliche Korrektheit prüfen | Abgleich-Report |
| 5.4 | Technische Qualität prüfen | Tech-Check-Ergebnis |
| 5.5 | Freigabe-Empfehlung | Quality-Report |

### Output
Qualitätsbericht wird gespeichert in:
```
projekte/PROJEKT/05_quality/quality_report.md
```

### Freigabe-Stufen

| Stufe | Kriterien | Aktion |
|-------|-----------|--------|
| ✅ FREIGEGEBEN | Keine kritischen Fehler, max. 3 Warnungen | Weiter zu Phase 6 |
| ⚠️ ÜBERARBEITUNG | Kritische Fehler vorhanden, aber behebbar | Zurück zu Phase 3 oder 4 |
| ❌ ABGELEHNT | Fundamentale Probleme | Zurück zu Phase 1 oder 2 |

### Akzeptanzkriterien Phase 5
- [ ] Quality-Report vollständig
- [ ] Alle kritischen Fehler behoben (bei Freigabe)
- [ ] Freigabe-Empfehlung dokumentiert

---

## Phase 6: Export

### Ziel
Erstellung einer einsatzbereiten Version des System-Prompts.

### Aktivitäten

| Schritt | Aktion | Output |
|---------|--------|--------|
| 6.1 | System-Prompt finalisieren | Finaler Prompt |
| 6.2 | Export-Format erstellen | Copy-Paste-Ready |
| 6.3 | Dokumentation ergänzen | Nutzungshinweise |

### Output
Export-Ready Version wird gespeichert in:
```
projekte/PROJEKT/06_export/bot_export.md
```

### Akzeptanzkriterien Phase 6
- [ ] System-Prompt ist copy-paste-ready
- [ ] Dokumentation vollständig
- [ ] Keine technischen Artefakte im Export

---

## Phase 7: Test

### Ziel
Validierung des Bots durch praktische Tests.

### Aktivitäten

| Schritt | Aktion | Output |
|---------|--------|--------|
| 7.1 | Testplan erstellen | Testplan |
| 7.2 | Testszenarien durchführen | Test-Logs |
| 7.3 | Ergebnisse dokumentieren | Testergebnisse |
| 7.4 | Bei Bedarf: Iteration | Anpassungen |

### Test-Kategorien

| Kategorie | Beschreibung | Beispiel |
|-----------|--------------|----------|
| **Happy Path** | Normaler Ablauf | Lernender beantwortet korrekt |
| **Edge Cases** | Grenzfälle | Sehr kurze/lange Antworten |
| **Error Handling** | Fehlerverhalten | Unverständliche Eingabe |
| **Robustness** | Prompt-Injection | Umgehungsversuche |

### Output
Test-Dokumentation wird gespeichert in:
```
projekte/PROJEKT/07_test/
├── testplan.md
└── testergebnisse.md
```

### Akzeptanzkriterien Phase 7
- [ ] Alle Test-Kategorien durchgeführt
- [ ] Ergebnisse dokumentiert
- [ ] Kritische Fehler behoben

---

## Iteration

Bei Überarbeitungsbedarf:

```
┌─────────────────────────────────────────────────────┐
│  QUALITY-CHECKER findet Fehler                      │
│                 │                                    │
│                 ▼                                    │
│  ┌─────────────────────────────────────────┐        │
│  │  Fehler in...                            │        │
│  │  - Scripts? → Zurück zu SCRIPT-GENERATOR │        │
│  │  - Assembly? → Zurück zu PROMPT-BUILDER  │        │
│  │  - Material? → Zurück zu MATERIAL-ANALYST│        │
│  │  - Grundlagen? → Zurück zu INTAKE        │        │
│  └─────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────┘
```

---

## Zeitschätzung

| Phase | Geschätzte Zeit | Abhängig von |
|-------|-----------------|--------------|
| 1. Intake | 15-30 Min | Material-Menge |
| 2. Analyse | 30-60 Min | Material-Komplexität |
| 3. Generierung | 45-90 Min | Anzahl Tasks |
| 4. Assembly | 15-30 Min | - |
| 5. Validierung | 20-40 Min | Fehleranzahl |
| 6. Export | 5-10 Min | - |
| 7. Test | 30-60 Min | Test-Umfang |
| **Gesamt** | **~3-5 Stunden** | - |

Mit Übung und bei ähnlichem Material kann die Zeit auf 1.5-2.5 Stunden reduziert werden.
