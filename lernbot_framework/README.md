# Lernbot-Framework

Framework zur effizienten Erstellung von Lernassistenz-Bots mit lokalen LLMs für Berufsschulen und Studierende.

## Ziel

Minimierung der Erstellungs- und Bearbeitungszeit für didaktisch hochwertige Lernbots durch:
- Strukturierte Script-Vorlagen (maschinenlesbar)
- Spezialisierte Agenten für jeden Arbeitsschritt
- Reproduzierbarer Workflow

## Ordnerstruktur

```
lernbot_framework/
├── agents/                    # Agenten-System-Prompts
│   ├── material_analyst.md    # Analysiert Unterrichtsmaterial
│   ├── script_generator.md    # Generiert strukturierte Scripts
│   ├── prompt_builder.md      # Baut finalen System-Prompt
│   └── quality_checker.md     # Validiert Qualität & Konsistenz
├── templates/
│   └── scripts/               # Script-Vorlagen
│       ├── meta_template.md   # Dokument-Metadaten
│       ├── task_template.md   # Aufgaben-Blöcke
│       ├── rubric_template.md # Bewertungskriterien
│       ├── model_template.md  # Musterlösungen
│       └── debrief_template.md# Reflexion/Transfer
├── processes/                 # Workflow-Definitionen
│   └── bot_creation.md        # Haupt-Erstellungsprozess
├── sops/                      # Schritt-für-Schritt-Anleitungen
│   ├── material_intake.md     # Material-Aufnahme
│   ├── script_generation.md   # Script-Erstellung
│   └── prompt_assembly.md     # Prompt-Zusammenbau
├── examples/                  # Beispiel-Outputs
└── roles.yaml                 # Rollendefinitionen
```

## Workflow-Übersicht

```
INPUT (PDF, Word, Excel, MD)
         │
         ▼
┌─────────────────────┐
│  MATERIAL-ANALYST   │  → Extrahiert Lernziele, Struktur, Inhalte
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│  SCRIPT-GENERATOR   │  → Erstellt TASK, RUBRIC, MODEL, DEBRIEF Scripts
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│   PROMPT-BUILDER    │  → Kombiniert Scripts zum finalen System-Prompt
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│  QUALITY-CHECKER    │  → Validiert Konsistenz und didaktische Qualität
└─────────┴───────────┘
          ▼
OUTPUT: Einsatzbereiter Lernbot-System-Prompt
```

## Script-Typen

| Script-Typ | Datei | Zweck |
|------------|-------|-------|
| META | `meta_template.md` | Dokument-Metadaten (ID, Version, Zielgruppe) |
| TASK | `task_template.md` | Aufgaben mit Lernzielen, Scaffolds, Materialreferenzen |
| RUBRIC | `rubric_template.md` | Bewertungskriterien mit Levels und Ankerbeispielen |
| MODEL | `model_template.md` | Musterlösungen (erst nach Versuch zeigen) |
| DEBRIEF | `debrief_template.md` | Reflexions- und Transferfragen |

## Quick Start

1. Material in `docs/Vorlagen/` ablegen
2. `Material-Analyst`-Agent mit Material aufrufen
3. Generierte Analyse an `Script-Generator` übergeben
4. Scripts mit `Prompt-Builder` zum finalen Prompt kombinieren
5. Mit `Quality-Checker` validieren

## Lizenz

Intern / Eigene Nutzung
