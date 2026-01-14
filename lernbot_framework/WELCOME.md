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
| **Bot testen** | Testszenarien durchführen |

---

## 🚀 Schnellstart

### Option A: Neues Projekt starten

**1. Projekt anlegen:**
```powershell
.\scripts\new_project.ps1 -Name "2026-01_Mein_Lernbot"
```

**2. Material ablegen und `_meta.yaml` ausfüllen**

**3. Analyse starten (★ STANDARD-EINSTIEG):**
> "Analysiere das Material in `projekte/2026-01_Mein_Lernbot/01_material/`"

### Option B: Bestehendes Projekt fortsetzen

Sage:
> "Analysiere das Projekt in `projekte/{{PROJEKT_NAME}}/`"

Ich prüfe den Status und setze beim nächsten Schritt fort.

### Option C: Beispielprojekt ansehen

Sage:
> "Zeige mir das Beispielprojekt."

Du siehst die Struktur von: `projekte/Beispiel_Tagung_Dock03/`

---

## ★ Standard-Einstieg: Material-Analyst

> **Nach dem Ablegen des Materials beginnst du IMMER mit dem Material-Analyst!**

Sage einfach:
```
"Analysiere das Material in projekte/PROJEKT_NAME/01_material/"
```

Der Material-Analyst:
- Extrahiert Lernziele (mit Bloom-Taxonomie)
- Identifiziert Aufgaben
- Katalogisiert Ressourcen
- Erkennt Bewertungskriterien
- Dokumentiert Lücken

---

## 📁 Projektstruktur

Jedes Bot-Projekt hat dieselbe Struktur:

```
projekte/MEIN_PROJEKT/
├── README.md              ← Projekt-Status
├── 01_material/           ← Unterrichtsmaterial + _meta.yaml
├── 02_analyse/            ← Material-Analyse (Material-Analyst)
├── 03_scripts/            ← Generierte Scripts (Script-Generator)
├── 04_system_prompt/      ← Finaler Prompt (Prompt-Builder)
├── 05_quality/            ← Quality-Report (Quality-Checker)
├── 06_export/             ← Einsatzbereite Version
└── 07_test/               ← Test-Dokumentation
```

---

## 📋 Workflow-Übersicht

```
01_material/  →  02_analyse/  →  03_scripts/  →  04_system_prompt/  →  05_quality/  →  06_export/  →  07_test/
   Material       Analyse        Scripts          Prompt              Report          Export         Test
```

| Phase | Agent | Eingabe | Ausgabe |
|-------|-------|---------|---------|
| 1 | - | Material | `_meta.yaml` |
| 2 | **Material-Analyst** ★ | `01_material/` | `analyse.md` |
| 3 | Script-Generator | `02_analyse/` | Script-Blöcke |
| 4 | Prompt-Builder | `03_scripts/` | `system_prompt.md` |
| 5 | Quality-Checker | `04_system_prompt/` | `quality_report.md` |
| 6 | - | `05_quality/` | Export-Ready |
| 7 | - | `06_export/` | Testergebnisse |

---

## 💡 Beispiel-Befehle

```
"Erstelle ein neues Projekt für [Fach/Thema]"
"Analysiere das Material in projekte/[PROJEKT]/01_material/"
"Generiere Scripts für das Projekt [PROJEKT]"
"Baue den System-Prompt für [PROJEKT]"
"Prüfe die Qualität von [PROJEKT]"
"Teste den Bot für [PROJEKT]"
"Zeige mir die Quickstart-Anleitung"
```

---

## 📚 Dokumentation

| Dokument | Beschreibung |
|----------|--------------|
| [Quickstart](guides/quickstart.md) | Schritt-für-Schritt-Anleitung |
| [Glossar](guides/glossar.md) | Begriffsdefinitionen |
| [Script-Vorlage](templates/script_vorlage_komplett.md) | Alle Templates in einem Dokument |
| [Workflow](processes/bot_creation.md) | Detaillierter Prozess |
| [Beispielprojekt](projekte/Beispiel_Tagung_Dock03/) | Vollständiges Beispiel |

### Templates

| Template | Beschreibung |
|----------|--------------|
| [META](templates/scripts/meta_template.md) | Metadaten-Block |
| [PHASE](templates/scripts/phase_template.md) | Lernphasen |
| [RESOURCE](templates/scripts/resource_template.md) | Ressourcen |
| [TASK](templates/scripts/task_template.md) | Aufgaben |
| [RUBRIC](templates/scripts/rubric_template.md) | Bewertungskriterien |
| [MODEL](templates/scripts/model_template.md) | Musterlösungen |
| [DEBRIEF](templates/scripts/debrief_template.md) | Reflexion |
| [Testplan](templates/scripts/testplan_template.md) | Test-Vorlage |

---

**Womit möchtest du starten?** 🎯

> 💡 **Tipp:** Beginne mit dem Material-Analyst, nachdem du dein Material hochgeladen hast!
