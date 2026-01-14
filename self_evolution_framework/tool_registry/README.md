# Tool-Registry — Self-Evolution Framework

Verzeichnis der verfügbaren Tools und Integrationen für das Self-Evolution Framework.

---

## Knowledge Base Import Tool

### Übersicht
- **Name**: `import_to_knowledge_base`
- **Zweck**: Importiert externe Dokumente (PDFs, Textdateien) in die Knowledge Base
- **Pfad**: `scripts/import_to_knowledge_base.py`

### Unterstützte Formate
- PDF-Dateien (`.pdf`)
- Textdateien (`.txt`, `.md`, `.text`)

### Verwendung

**Einzelne Datei importieren:**
```bash
python scripts/import_to_knowledge_base.py --source "pfad/zur/datei.pdf" --category personal
```

**Mit Tags:**
```bash
python scripts/import_to_knowledge_base.py --source "buch.pdf" --category research --tags psychologie selbsthilfe
```

**Ganzen Ordner importieren:**
```bash
python scripts/import_to_knowledge_base.py --source "pfad/zum/ordner" --category research --batch
```

### Kategorien
| Kategorie | Beschreibung | Speicherort |
|-----------|--------------|-------------|
| `personal` | Persönliche Dokumente | `knowledge_base/personal/imported/` |
| `research` | Wissenschaftliche Inhalte | `knowledge_base/research/` |
| `patterns` | Muster-Dokumentation | `knowledge_base/patterns/` |
| `goals` | Ziel-Dokumentation | `knowledge_base/goals/` |
| `notes` | Persönliche Notizen | `knowledge_base/personal/notes/` |
| `journals` | Tagebucheinträge | `knowledge_base/personal/journals/` |

### Voraussetzungen
```bash
pip install pdfminer.six
```

### Output
Jede importierte Datei erhält:
- YAML-Metadaten-Header (Datum, Quelle, Tags)
- Automatischer Dateiname: `YYYY-MM-DD_originalname.md`
- Speicherung im entsprechenden Kategorie-Ordner

---

## Knowledge Base Query (Konzept)

### Übersicht
- **Name**: `query_knowledge_base`
- **Zweck**: Durchsucht die Knowledge Base nach relevanten Informationen
- **Status**: Konzept (für zukünftige Implementierung)

### Geplante Features
- Volltextsuche in allen Dokumenten
- Tag-basierte Filterung
- Datum-basierte Filterung
- Semantic Search (optional, mit LLM-Integration)

### Konzeptuelle Verwendung
```bash
# Suche nach Stichwort
python scripts/query_knowledge_base.py --search "Prokrastination"

# Filter nach Tags
python scripts/query_knowledge_base.py --tags stress arbeit

# Filter nach Kategorie
python scripts/query_knowledge_base.py --category patterns
```

---

## Agenten-Zugriff auf Knowledge Base

### Wie Agenten Daten nutzen

#### Researcher
```markdown
Anweisung für Researcher:
- Prüfe zuerst `knowledge_base/research/` auf bereits vorhandene Informationen
- Füge neue Erkenntnisse mit dem Import-Tool hinzu
- Verknüpfe Quellen in `evidence_log.md`
```

#### Pattern-Analyst
```markdown
Anweisung für Pattern-Analyst:
- Lade existierende Spiralen aus `knowledge_base/patterns/`
- Dokumentiere neue Muster mit dem `spiral_analysis.md` Template
- Speichere in `knowledge_base/patterns/spirals/`
```

#### Coach
```markdown
Anweisung für Coach:
- Lese vorherige Sessions aus `knowledge_base/sessions/`
- Referenziere frühere Reflexionen für Kontext
- Beachte dokumentierte Muster und Trigger
```

#### Accountability-Partner
```markdown
Anweisung für Accountability-Partner:
- Verfolge Ziele in `knowledge_base/goals/active/`
- Verschiebe erreichte Ziele nach `goals/completed/`
- Verknüpfe Fortschrittsberichte mit Sessions
```

---

## Datei-Konventionen

### Dateinamen
```
YYYY-MM-DD_kategorie_beschreibung.md
```

### Metadaten-Header
```yaml
---
date: 2024-01-15
type: reflection | pattern | goal | research | note | imported
source: [Quelldatei wenn importiert]
tags: [tag1, tag2]
related: [andere_datei.md]
status: active | resolved | archived
---
```

---

## Zukünftige Tools (Roadmap)

| Tool | Beschreibung | Priorität |
|------|--------------|-----------|
| `query_knowledge_base.py` | Durchsuchen der Knowledge Base | Hoch |
| `export_insights.py` | Exportiert Erkenntnisse als Report | Mittel |
| `link_patterns.py` | Verknüpft verwandte Muster | Mittel |
| `backup_knowledge_base.py` | Sichert Knowledge Base | Hoch |
| `sync_with_notion.py` | Notion-Integration | Niedrig |
