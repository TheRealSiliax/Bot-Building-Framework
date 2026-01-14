# Bot-Creation Workflow

Hauptprozess zur Erstellung eines Lernassistenz-Bots.

## Prozess-Übersicht

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         BOT-CREATION WORKFLOW                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 1: INTAKE                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Material sammeln → Metadaten erfassen → Ziele definieren           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  PHASE 2: ANALYSE                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  MATERIAL-ANALYST: Dokumente parsen → Struktur extrahieren          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  PHASE 3: GENERIERUNG                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  SCRIPT-GENERATOR: META → TASKS → RUBRICS → MODELS → DEBRIEF        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  PHASE 4: ASSEMBLY                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  PROMPT-BUILDER: Scripts kombinieren → System-Prompt erstellen      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  PHASE 5: VALIDIERUNG                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  QUALITY-CHECKER: Prüfen → Freigeben oder Iteration                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  OUTPUT: Einsatzbereiter Lernbot-System-Prompt                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

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
| 1.1 | Material in `docs/Vorlagen/` ablegen | Ersteller | Rohmaterial |
| 1.2 | Metadaten-Formular ausfüllen | Ersteller | Metadaten |
| 1.3 | Lernziele definieren/bestätigen | Ersteller | Lernziel-Liste |
| 1.4 | Bot-Konfiguration festlegen | Ersteller | Konfiguration |

### Metadaten-Formular

```yaml
# Bot-Konfiguration
bot_name: "{{Name des Bots}}"
tonalitaet: "{{formal|freundlich|motivierend}}"
sprachniveau: "{{B1|B2|C1}}"

# Kurs-Informationen
fach: "{{Fachbereich}}"
modul: "{{Modulname}}"
zielgruppe: "{{Beschreibung}}"
voraussetzungen: "{{Vorwissen}}"

# Zeitrahmen
dauer_gesamt: "{{Minuten}}"
sessions: "{{Anzahl Sitzungen}}"

# Material-Liste
materialien:
  - datei: "{{Dateiname}}"
    typ: "{{PDF|Word|Excel|MD}}"
    beschreibung: "{{Kurzbeschreibung}}"
```

### Akzeptanzkriterien Phase 1
- [ ] Alle Materialien liegen digital vor
- [ ] Metadaten-Formular vollständig ausgefüllt
- [ ] Lernziele explizit definiert
- [ ] Bot-Name und Tonalität festgelegt

---

## Phase 2: Analyse

### Ziel
Strukturierte Extraktion aller lernrelevanten Informationen aus dem Rohmaterial.

### Agent
**Material-Analyst** (`agents/material_analyst.md`)

### Eingaben
- Rohmaterial aus Phase 1
- Metadaten-Formular

### Aktivitäten

| Schritt | Aktion | Output |
|---------|--------|--------|
| 2.1 | Dokumente parsen (Text extrahieren) | Rohtext |
| 2.2 | Lernziele identifizieren | Lernziel-Liste (YAML) |
| 2.3 | Aufgaben erkennen | Aufgaben-Liste (YAML) |
| 2.4 | Ressourcen katalogisieren | Ressourcen-Inventar (YAML) |
| 2.5 | Bewertungskriterien erkennen | Kriterien-Liste (YAML) |
| 2.6 | Lücken dokumentieren | Lücken-Report |

### Output-Format
Strukturierte Material-Analyse als Markdown mit YAML-Blöcken (siehe `agents/material_analyst.md`).

### Akzeptanzkriterien Phase 2
- [ ] Alle Lernziele mit Bloom-Stufe versehen
- [ ] Alle Aufgaben mit Typ und Ressourcen-Bezug
- [ ] Lücken explizit markiert
- [ ] Analyse-Dokument vollständig

---

## Phase 3: Generierung

### Ziel
Transformation der Analyse in maschinenlesbare Script-Blöcke.

### Agent
**Script-Generator** (`agents/script_generator.md`)

### Eingaben
- Material-Analyse aus Phase 2
- Script-Templates aus `templates/scripts/`

### Aktivitäten

| Schritt | Aktion | Template | Output |
|---------|--------|----------|--------|
| 3.1 | META-Block generieren | `meta_template.md` | META-BLOCK |
| 3.2 | PHASE-Struktur erstellen | - | PHASE-BLOCKs |
| 3.3 | RESOURCE-Blöcke erstellen | - | RESOURCE-BLOCKs |
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

### Akzeptanzkriterien Phase 3
- [ ] Alle Block-Typen generiert
- [ ] IDs eindeutig und konsistent
- [ ] Alle Referenzen gültig
- [ ] Keine unersetzten Platzhalter (außer explizit markiert)

---

## Phase 4: Assembly

### Ziel
Kombination aller Scripts zu einem finalen System-Prompt.

### Agent
**Prompt-Builder** (`agents/prompt_builder.md`)

### Eingaben
- Generierte Scripts aus Phase 3
- Bot-Konfiguration aus Phase 1
- System-Prompt-Basis-Template

### Aktivitäten

| Schritt | Aktion | Output |
|---------|--------|--------|
| 4.1 | Konfiguration laden | Variablen-Set |
| 4.2 | Scripts formatieren | Formatiertes Script-Dokument |
| 4.3 | Platzhalter ersetzen | Prompt ohne Platzhalter |
| 4.4 | Format optimieren | Finaler Prompt |

### Akzeptanzkriterien Phase 4
- [ ] Keine `{{...}}` Platzhalter im Output
- [ ] Alle Script-Blöcke integriert
- [ ] Token-Limit nicht überschritten
- [ ] Prompt ist copy-paste-ready

---

## Phase 5: Validierung

### Ziel
Qualitätssicherung vor dem Einsatz.

### Agent
**Quality-Checker** (`agents/quality_checker.md`)

### Eingaben
- Finaler System-Prompt aus Phase 4
- Generierte Scripts aus Phase 3
- Original-Material aus Phase 1

### Aktivitäten

| Schritt | Aktion | Output |
|---------|--------|--------|
| 5.1 | Strukturelle Konsistenz prüfen | Fehler-/Warnungsliste |
| 5.2 | Didaktische Qualität prüfen | Checklisten-Ergebnis |
| 5.3 | Inhaltliche Korrektheit prüfen | Abgleich-Report |
| 5.4 | Technische Qualität prüfen | Tech-Check-Ergebnis |
| 5.5 | Testlauf (optional) | Test-Protokoll |
| 5.6 | Freigabe-Empfehlung | Quality-Report |

### Freigabe-Stufen

| Stufe | Kriterien | Aktion |
|-------|-----------|--------|
| ✅ FREIGEGEBEN | Keine kritischen Fehler, max. 3 Warnungen | Einsatz möglich |
| ⚠️ ÜBERARBEITUNG | Kritische Fehler vorhanden, aber behebbar | Zurück zu Phase 3 oder 4 |
| ❌ ABGELEHNT | Fundamentale Probleme | Zurück zu Phase 1 oder 2 |

### Akzeptanzkriterien Phase 5
- [ ] Quality-Report vollständig
- [ ] Alle kritischen Fehler behoben (bei Freigabe)
- [ ] Freigabe-Empfehlung dokumentiert

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
| **Gesamt** | **~2-4 Stunden** | - |

Mit Übung und bei ähnlichem Material kann die Zeit auf 1-2 Stunden reduziert werden.

---

## Artefakte

Nach Abschluss liegen folgende Artefakte vor:

```
projekt/
├── docs/
│   └── Vorlagen/
│       └── {{material}}.docx/.pdf
├── lernbot_framework/
│   └── examples/
│       └── {{bot_name}}/
│           ├── 01_material_analyse.md
│           ├── 02_generierte_scripts.md
│           ├── 03_system_prompt.md
│           └── 04_quality_report.md
```
