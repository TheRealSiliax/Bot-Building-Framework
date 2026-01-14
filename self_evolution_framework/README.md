# Self-Evolution Framework

Ein evidenzbasiertes Framework für persönliche Entwicklung, Selbstreflexion und das systematische Durchbrechen von Negativspiralen.

## Zweck

Dieses Framework unterstützt dich dabei:
- **Selbstreflexion** strukturiert und regelmäßig durchzuführen
- **Negativspiralen** zu erkennen und systematisch zu durchbrechen
- **Evidenzbasierte Strategien** für persönliches Wachstum anzuwenden
- **Karriere und Leben** zielgerichtet zu navigieren

## Wissenschaftliche Grundlagen

Das Framework basiert auf bewährten wissenschaftlichen Ansätzen:
- Kognitive Verhaltenstherapie (CBT)
- Akzeptanz- und Commitment-Therapie (ACT)
- Positive Psychologie (Seligman, Csikszentmihalyi)
- Habit Formation Research (Clear, Fogg)
- Neurowissenschaftliche Erkenntnisse zur Verhaltensänderung
- **Leadership Frameworks** (Transformational Leadership, AIIR, Emotional Intelligence)

## Leadership & Management Integration

Das Framework integriert drei Führungsebenen für Karriereentwicklung:

### Leading Yourself (Selbstführung)
- Selbstbewusstsein, Selbstregulation
- Persönliches Wachstum, Accountability
- Werte & Purpose

### Leading Others (Menschenführung)
- Kommunikation, Motivation
- Entwicklung anderer, Team-Building
- Konfliktlösung

### Leading Organization (Strategische Führung)
- Vision & Strategie
- Change Management
- Kultur-Building

> "Bevor du andere führen kannst, musst du dich selbst führen."

## Struktur

```
self_evolution_framework/
├── roles.yaml              # Zentrale Rollenbeschreibungen
├── agents/                 # Spezialisierte Agenten
│   ├── orchestrator.md    # 🎯 Zentraler Koordinator
│   ├── coach.md           # Begleitung & Motivation
│   ├── researcher.md      # Wissenschaftliche Evidenz
│   ├── reflektor.md       # Selbstreflexion
│   ├── pattern_analyst.md # Muster- & Spiralenerkennung
│   ├── stratege.md        # Taktiken & Strategien
│   ├── accountability.md  # Fortschrittskontrolle
│   └── leader.md          # Leadership-Entwicklung
├── processes/              # Entwicklungsprozesse
│   ├── reflection_cycle.md    # Reflexionszyklus
│   ├── spiral_breaker.md      # Negativspiralen durchbrechen
│   ├── evidence_intervention.md # Wissenschaftliche Interventionen
│   ├── growth_loop.md         # Kontinuierliche Verbesserung
│   └── leadership_development.md # 🆕 Führungsentwicklung
├── sops/                   # Standard Operating Procedures
│   ├── daily_reflection.md    # Tägliche Reflexion
│   ├── weekly_review.md       # Wöchentlicher Review
│   ├── crisis_intervention.md # Krisenintervention
│   ├── goal_setting.md        # Zielsetzung (SMART+)
│   ├── pattern_breaking.md    # Muster durchbrechen
│   └── leadership_development.md # 🆕 Führungsentwicklung
├── templates/              # Vorlagen
│   ├── reflection_journal.md  # Reflexionstagebuch
│   ├── goal_canvas.md         # Zielplanung
│   ├── spiral_analysis.md     # Spiralen-Analyse
│   ├── strategy_board.md      # Strategieübersicht
│   ├── evidence_log.md        # Evidenz-Dokumentation
│   └── leadership_canvas.md   # 🆕 Leadership-Entwicklung
├── evidence_base/          # Wissenschaftliche Grundlagen
│   ├── README.md              # Übersicht
│   ├── cbt_principles.md      # CBT-Grundlagen
│   ├── act_principles.md      # ACT-Grundlagen
│   ├── habit_science.md       # Gewohnheitsforschung
│   ├── neuroscience.md        # Neurowissenschaften
│   └── leadership_frameworks.md # 🆕 Leadership-Modelle
├── knowledge_base/         # 📚 PERSÖNLICHE DATENBANK
│   ├── personal/              # Persönliche Dokumente
│   │   ├── notes/            # Notizen & Gedanken
│   │   ├── journals/         # Tagebucheinträge
│   │   └── imported/         # Importierte PDFs/Texte
│   ├── research/              # Recherche-Ergebnisse
│   ├── patterns/              # Erkannte Muster & Spiralen
│   ├── goals/                 # Zieldokumentation
│   └── sessions/              # Sitzungsprotokolle
├── scripts/                # 🔧 TOOLS
│   └── import_to_knowledge_base.py  # PDF/Text-Import
└── tool_registry/          # Tool-Dokumentation
    └── README.md
```

## Quick Start

1. **Starte mit Reflexion**: Nutze `templates/reflection_journal.md` für deine erste Reflexion
2. **Identifiziere Muster**: Analysiere mit `templates/spiral_analysis.md` wiederkehrende Negativspiralen
3. **Setze Ziele**: Erstelle evidenzbasierte Ziele mit `templates/goal_canvas.md`
4. **Wende Strategien an**: Nutze die SOPs für konkrete Handlungsanleitungen

## Daten importieren

### PDFs und Textdateien in die Knowledge Base laden

```bash
# Voraussetzung: pdfminer installieren
pip install pdfminer.six

# PDF importieren
python scripts/import_to_knowledge_base.py --source "mein_buch.pdf" --category research

# Mit Tags
python scripts/import_to_knowledge_base.py --source "notizen.txt" --category personal --tags reflexion arbeit

# Ganzen Ordner importieren
python scripts/import_to_knowledge_base.py --source "dokumente/" --category research --batch
```

### Agenten nutzen die Knowledge Base automatisch
- **Researcher** greift auf `knowledge_base/research/` zu
- **Pattern-Analyst** lädt Muster aus `knowledge_base/patterns/`
- **Coach** referenziert frühere Sessions aus `knowledge_base/sessions/`
- **Accountability** trackt Ziele in `knowledge_base/goals/`

## Philosophie

> "Zwischen Reiz und Reaktion liegt ein Raum. In diesem Raum liegt unsere Macht zur Wahl unserer Reaktion. In unserer Reaktion liegen unsere Entwicklung und unsere Freiheit."
> — Viktor Frankl

Dieses Framework gibt dir die Werkzeuge, diesen Raum bewusst zu nutzen.
