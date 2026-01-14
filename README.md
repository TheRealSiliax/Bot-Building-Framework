# Bot-Building Framework

Framework zur strukturierten Erstellung von **Lernassistenz-Bots** mit lokalen LLMs für Berufsschulen und Studierende.

## 🎯 Ziel

Minimierung der Erstellungs- und Bearbeitungszeit für didaktisch hochwertige Lernbots durch:
- Strukturierte Script-Vorlagen (maschinenlesbar)
- Spezialisierte Agenten für jeden Arbeitsschritt
- Reproduzierbarer, dokumentierter Workflow

## 🚀 Schnellstart

### Neues Projekt anlegen

```powershell
# PowerShell
.\scripts\new_project.ps1 -Name "2026-01_Gastro_Wareneinkauf"
```

Oder manuell:
```powershell
Copy-Item -Recurse "lernbot_framework/projekte/_vorlage" "lernbot_framework/projekte/MEIN_PROJEKT"
```

### Workflow starten

1. **Material ablegen** in `projekte/MEIN_PROJEKT/01_material/`
2. **`_meta.yaml` ausfüllen**
3. **Material-Analyst starten** → Analyse wird erstellt
4. Workflow folgen: Analyse → Scripts → Prompt → Quality → Export

**Detaillierte Anleitung:** [lernbot_framework/guides/quickstart.md](lernbot_framework/guides/quickstart.md)

## 📁 Projektstruktur

```
Bot-Building-Framework/
├── lernbot_framework/         # 🎓 LERNBOT-FRAMEWORK
│   ├── projekte/              # Deine Bot-Projekte
│   │   ├── _vorlage/          # Kopierbare Vorlage
│   │   └── Beispiel_Tagung_Dock03/  # Beispielprojekt
│   ├── agents/                # Agenten-Definitionen
│   ├── templates/             # Script-Vorlagen
│   ├── guides/                # Anleitungen
│   └── processes/             # Workflow-Dokumentation
├── framework/                 # 🔧 Basis-Framework (generisch)
├── scripts/                   # Utility-Scripts
└── docs/                      # Dokumentation
```

## 🤖 Agenten-Übersicht

| Agent | Aufgabe | Eingabe | Ausgabe |
|-------|---------|---------|---------|
| **Material-Analyst** | Analysiert Unterrichtsmaterial | `01_material/` | `02_analyse/` |
| **Script-Generator** | Generiert Script-Blöcke | `02_analyse/` | `03_scripts/` |
| **Prompt-Builder** | Assembliert System-Prompt | `03_scripts/` | `04_system_prompt/` |
| **Quality-Checker** | Validiert Qualität | `04_system_prompt/` | `05_quality/` |

## 📋 Workflow

```
01_material/  →  02_analyse/  →  03_scripts/  →  04_system_prompt/  →  05_quality/  →  06_export/  →  07_test/
   Material       Analyse        Scripts          Prompt              Report          Export        Test
```

## 🔗 GitHub

- **Repository**: [github.com/TheRealSiliax/Bot-Building-Framework](https://github.com/TheRealSiliax/Bot-Building-Framework)
- **SSH**: `git@github.com:TheRealSiliax/Bot-Building-Framework.git`

### Backup erstellen

```bash
python scripts/github_backup.py
```

Oder sage einfach: "Backup erstellen" / "Zu GitHub sichern"

## 📚 Dokumentation

| Dokument | Beschreibung |
|----------|--------------|
| [Quickstart](lernbot_framework/guides/quickstart.md) | Schritt-für-Schritt-Anleitung |
| [Glossar](lernbot_framework/guides/glossar.md) | Begriffsdefinitionen |
| [Bot-Creation Workflow](lernbot_framework/processes/bot_creation.md) | Detaillierter Prozess |
| [Script-Vorlage](lernbot_framework/templates/script_vorlage_komplett.md) | Alle Templates |

## 📄 Lizenz

Intern / Eigene Nutzung
