# Lernbot-Framework

Framework zur effizienten Erstellung von Lernassistenz-Bots mit lokalen LLMs für Berufsschulen und Studierende.

> 🚀 **Neu hier?** Starte mit der [Quickstart-Anleitung](guides/quickstart.md) oder schau dir die [vollständige Script-Vorlage](templates/script_vorlage_komplett.md) an!

## Ziel

Minimierung der Erstellungs- und Bearbeitungszeit für didaktisch hochwertige Lernbots durch:
- Strukturierte Script-Vorlagen (maschinenlesbar)
- Spezialisierte Agenten für jeden Arbeitsschritt
- Reproduzierbarer Workflow

## Ordnerstruktur

```
lernbot_framework/
├── WELCOME.md                 # Willkommens-Übersicht (bei fehlender Eingabe)
├── guides/
│   └── quickstart.md          # 🚀 Schritt-für-Schritt-Anleitung
├── agents/                    # Agenten-System-Prompts
│   ├── material_analyst.md    # Analysiert Unterrichtsmaterial
│   ├── script_generator.md    # Generiert strukturierte Scripts
│   ├── prompt_builder.md      # Baut finalen System-Prompt
│   └── quality_checker.md     # Validiert Qualität & Konsistenz
├── templates/
│   ├── script_vorlage_komplett.md  # 📄 Alle Templates in einem Dokument
│   └── scripts/               # Einzelne Script-Vorlagen
├── projekte/                  # 📁 DEINE BOT-PROJEKTE
│   ├── _vorlage/              # Kopierbare Projekt-Vorlage
│   │   ├── 01_material/       # Unterrichtsmaterial ablegen
│   │   ├── 02_analyse/        # Material-Analyse speichern
│   │   ├── 03_scripts/        # Generierte Scripts speichern
│   │   ├── 04_system_prompt/  # Finaler Prompt speichern
│   │   ├── 05_quality/        # Quality-Reports speichern
│   │   └── 06_export/         # Export-Versionen speichern
│   └── {{dein_projekt}}/      # Deine eigenen Projekte
├── processes/                 # Workflow-Definitionen
│   └── bot_creation.md        # Haupt-Erstellungsprozess
├── sops/                      # Schritt-für-Schritt-Anleitungen
│   └── material_intake.md     # Material-Aufnahme
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

**Ausführliche Anleitung:** [guides/quickstart.md](guides/quickstart.md)

### Neues Projekt anlegen

```powershell
# Projekt-Vorlage kopieren
Copy-Item -Recurse "lernbot_framework/projekte/_vorlage" "lernbot_framework/projekte/MEIN_PROJEKT"
```

### Workflow

1. **Material vorbereiten**: In `projekte/MEIN_PROJEKT/01_material/` ablegen + `_meta.yaml` ausfüllen
2. **Analysieren**: Material-Analyst → Ergebnis in `02_analyse/` speichern
3. **Scripts generieren**: Script-Generator → Ergebnis in `03_scripts/` speichern
4. **Prompt bauen**: Prompt-Builder → Ergebnis in `04_system_prompt/` speichern
5. **Validieren**: Quality-Checker → Report in `05_quality/` speichern
6. **Exportieren**: Finalen Prompt in `06_export/` kopieren und einsetzen ✓

### Ressourcen

| Dokument | Zweck |
|----------|-------|
| [WELCOME.md](WELCOME.md) | Orientierung bei fehlender Eingabe |
| [quickstart.md](guides/quickstart.md) | Schritt-für-Schritt-Anleitung |
| [script_vorlage_komplett.md](templates/script_vorlage_komplett.md) | Ausfüllbare Mustervorlage |
| [bot_creation.md](processes/bot_creation.md) | Detaillierter Workflow |

## Lizenz

Intern / Eigene Nutzung
