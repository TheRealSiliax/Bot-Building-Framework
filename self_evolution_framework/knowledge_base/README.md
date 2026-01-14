# Knowledge Base

## Übersicht

Die Knowledge Base ist der zentrale Ort für persönliche Daten, Dokumente und Erkenntnisse, auf die alle Agenten zugreifen können.

## Struktur

```
knowledge_base/
├── README.md                 # Diese Datei
├── personal/                 # Persönliche Dokumente
│   ├── notes/               # Notizen, Gedanken, Reflexionen
│   ├── journals/            # Tagebucheinträge
│   └── imported/            # Importierte Dokumente (PDFs, etc.)
├── research/                 # Recherche-Ergebnisse
│   ├── articles/            # Extrahierte Artikel
│   ├── books/               # Buchnotizen & Zusammenfassungen
│   └── studies/             # Wissenschaftliche Studien
├── patterns/                 # Erkannte Muster
│   ├── spirals/             # Dokumentierte Negativspiralen
│   ├── triggers/            # Bekannte Trigger
│   └── successes/           # Erfolgreiche Strategien
├── goals/                    # Zieldokumentation
│   ├── active/              # Aktive Ziele
│   ├── completed/           # Erreichte Ziele
│   └── archived/            # Archivierte Ziele
└── sessions/                 # Sitzungsprotokolle
    └── YYYY-MM-DD_topic.md  # Einzelne Sessions
```

## Wie Agenten auf Daten zugreifen

### Für den Researcher
Der Researcher kann auf `research/` zugreifen, um:
- Bereits gesammelte Evidenz zu nutzen
- Neue Erkenntnisse hinzuzufügen
- Quellen zu verknüpfen

### Für den Pattern-Analyst
Der Pattern-Analyst nutzt `patterns/` um:
- Bekannte Spiralen zu referenzieren
- Neue Muster zu dokumentieren
- Verbindungen zwischen Mustern zu finden

### Für den Coach
Der Coach greift auf `personal/` zu, um:
- Kontext aus früheren Reflexionen zu verstehen
- Fortschritte über Zeit zu erkennen
- Personalisierte Fragen zu stellen

### Für den Accountability-Partner
Nutzt `goals/` und `sessions/` für:
- Fortschrittstracking
- Commitment-Überprüfung
- Historische Vergleiche

## Daten importieren

### PDFs importieren
Nutze das Import-Tool:
```bash
python scripts/import_to_knowledge_base.py --type pdf --source "path/to/file.pdf"
```

### Textdateien importieren
```bash
python scripts/import_to_knowledge_base.py --type text --source "path/to/file.txt"
```

### Manuell hinzufügen
Erstelle einfach eine `.md` Datei im passenden Unterordner.

## Dateinamen-Konvention

```
YYYY-MM-DD_kategorie_beschreibung.md
```

**Beispiele:**
- `2024-01-15_reflexion_arbeitsstress.md`
- `2024-01-20_spiral_prokrastination.md`
- `2024-02-01_goal_fitness.md`

## Metadaten-Header

Jede Datei sollte einen YAML-Header haben:

```yaml
---
date: 2024-01-15
type: reflection | pattern | goal | research | note
tags: [stress, arbeit, selbstzweifel]
related: [2024-01-10_reflexion_konflikt.md]
status: active | resolved | archived
---
```

## Datenschutz-Hinweis

⚠️ Diese Daten sind **persönlich und vertraulich**.
- Speichere keine sensiblen Daten in Cloud-Diensten ohne Verschlüsselung
- Nutze lokale Backups
- Teile diese Daten nur bewusst
