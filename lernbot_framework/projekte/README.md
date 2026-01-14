# 📁 Bot-Projekte

Hier werden alle Lernbot-Projekte organisiert abgelegt.

## Struktur

```
projekte/
├── _vorlage/              ← Kopiere diesen Ordner für neue Projekte
├── {{projekt_1}}/         ← Dein erstes Bot-Projekt
├── {{projekt_2}}/         ← Dein zweites Bot-Projekt
└── ...
```

## Neues Projekt anlegen

### Schritt 1: Ordner kopieren
```powershell
# PowerShell
Copy-Item -Recurse "lernbot_framework/projekte/_vorlage" "lernbot_framework/projekte/MEIN_PROJEKT"
```

### Schritt 2: Material ablegen
Lege dein Unterrichtsmaterial in `01_material/` ab.

### Schritt 3: Workflow durchlaufen
Folge der Nummerierung der Ordner:
1. Material → 2. Analyse → 3. Scripts → 4. System-Prompt → 5. Quality → 6. Export

---

## Ordner-Übersicht pro Projekt

| Ordner | Inhalt | Workflow-Schritt |
|--------|--------|------------------|
| `01_material/` | Rohe Unterrichtsmaterialien (PDF, Word, Excel) | Intake |
| `02_analyse/` | Material-Analyse vom Material-Analyst | Analyse |
| `03_scripts/` | Generierte Script-Blöcke (TASK, RUBRIC, etc.) | Generierung |
| `04_system_prompt/` | Finaler System-Prompt | Assembly |
| `05_quality/` | Quality-Reports und Validierung | Validierung |
| `06_export/` | Exportierte/bereinigte Versionen für den Einsatz | Deployment |

---

## Namenskonvention

Benenne Projekte nach diesem Schema:
```
{{DATUM}}_{{FACH}}_{{THEMA}}
```

Beispiele:
- `2026-01_Gastro_Wareneinkauf`
- `2026-02_BWL_Lieferantenauswahl`
- `2026-03_IT_Netzwerke`

---

## Quick Start

1. Kopiere `_vorlage/` → `{{dein_projektname}}/`
2. Fülle `01_material/_meta.yaml` aus
3. Lege Material in `01_material/` ab
4. Starte mit dem Material-Analyst
