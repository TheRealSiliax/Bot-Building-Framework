# 👋 Willkommen im Lernbot-Framework!

Du möchtest einen **Lernassistenz-Bot** erstellen? Perfekt! Ich helfe dir dabei.

---

## 🎯 Was kann ich für dich tun?

| Aktion | Beschreibung |
|--------|--------------|
| **Neues Projekt anlegen** | Projektordner erstellen und Material ablegen |
| **Material analysieren** | Unterrichtsmaterial strukturiert aufbereiten |
| **Scripts generieren** | TASK, RUBRIC, MODEL Blöcke erstellen |
| **Prompt bauen** | Finalen System-Prompt assemblieren |
| **Qualität prüfen** | Bot vor Einsatz validieren |

---

## 🚀 Schnellstart

### Option A: Neues Projekt starten

Sage:
> "Ich möchte einen neuen Lernbot erstellen."

Ich führe dich durch:
1. Projektordner anlegen
2. Material ablegen
3. `_meta.yaml` ausfüllen

### Option B: Bestehendes Projekt fortsetzen

Sage:
> "Analysiere das Projekt in `projekte/{{PROJEKT_NAME}}/`"

Ich prüfe den Status und setze beim nächsten Schritt fort.

### Option C: Beispielprojekt ansehen

Sage:
> "Zeige mir das Beispielprojekt."

Du siehst die Struktur von: `projekte/Beispiel_Tagung_Dock03/`

---

## 📁 Projektstruktur

Jedes Bot-Projekt hat dieselbe Struktur:

```
projekte/MEIN_PROJEKT/
├── README.md              ← Projekt-Status
├── 01_material/           ← Unterrichtsmaterial + _meta.yaml
├── 02_analyse/            ← Material-Analyse
├── 03_scripts/            ← Generierte Scripts
├── 04_system_prompt/      ← Finaler Prompt
├── 05_quality/            ← Quality-Report
└── 06_export/             ← Einsatzbereite Version
```

### Neues Projekt anlegen

```powershell
Copy-Item -Recurse "lernbot_framework/projekte/_vorlage" "lernbot_framework/projekte/MEIN_PROJEKT"
```

---

## 📋 Workflow-Übersicht

```
01_material/  →  02_analyse/  →  03_scripts/  →  04_system_prompt/  →  05_quality/  →  06_export/
   Material       Analyse        Scripts          Prompt              Report          FERTIG!
```

| Phase | Agent | Eingabe | Ausgabe |
|-------|-------|---------|---------|
| 1 | - | Material | `_meta.yaml` |
| 2 | Material-Analyst | `01_material/` | `material_analyse.md` |
| 3 | Script-Generator | `02_analyse/` | `scripts_komplett.md` |
| 4 | Prompt-Builder | `03_scripts/` | `system_prompt.md` |
| 5 | Quality-Checker | `04_system_prompt/` | `quality_report.md` |
| 6 | - | `05_quality/` | `FINAL_system_prompt.txt` |

---

## 💡 Beispiel-Befehle

```
"Erstelle ein neues Projekt für [Fach/Thema]"
"Analysiere das Material in projekte/[PROJEKT]/01_material/"
"Generiere Scripts für das Projekt [PROJEKT]"
"Baue den System-Prompt für [PROJEKT]"
"Prüfe die Qualität von [PROJEKT]"
"Zeige mir die Quickstart-Anleitung"
```

---

## 📚 Dokumentation

| Dokument | Beschreibung |
|----------|--------------|
| [Quickstart](guides/quickstart.md) | Schritt-für-Schritt-Anleitung |
| [Script-Vorlage](templates/script_vorlage_komplett.md) | Alle Templates in einem Dokument |
| [Workflow](processes/bot_creation.md) | Detaillierter Prozess |
| [Beispielprojekt](projekte/Beispiel_Tagung_Dock03/) | Vollständiges Beispiel |

---

**Womit möchtest du starten?** 🎯
