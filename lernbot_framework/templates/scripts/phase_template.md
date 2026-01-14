# PHASE-Block Template

Template für die Definition von Lernphasen im Bot-Script.

---

## Syntax

```yaml
# PHASE-BLOCK
PHASE_ID: "P{{NUMMER}}"
PHASE_NAME: "{{NAME_DER_PHASE}}"
PHASE_TYP: "{{einfuehrung|hauptteil|abschluss|debriefing}}"
DAUER_MIN: {{MINUTEN}}
POSITION: {{1-n}}  # Reihenfolge

BESCHREIBUNG: |
  {{Kurzbeschreibung der Phase und ihrer Ziele}}

LERNZIELE_PHASE:
  - "{{Lernziel 1 für diese Phase}}"
  - "{{Lernziel 2 für diese Phase}}"

AKTIVITAETEN:
  - typ: "{{input|discussion|task|reflection}}"
    beschreibung: "{{Was passiert}}"
    dauer: {{MINUTEN}}

UEBERGANG_ZU:
  naechste_phase: "P{{NUMMER+1}}"
  bedingung: "{{Wann wird gewechselt}}"
  hinweis: "{{Übergangstext}}"

RESOURCES_PHASE:
  - "R{{NUMMER}}"  # Referenz auf RESOURCE-Block
```

---

## Beispiel: Einführungsphase

```yaml
# PHASE-BLOCK
PHASE_ID: "P01"
PHASE_NAME: "Einführung und Aktivierung"
PHASE_TYP: "einfuehrung"
DAUER_MIN: 10
POSITION: 1

BESCHREIBUNG: |
  Der Bot begrüßt die Lernenden, aktiviert Vorwissen und 
  führt in das Thema ein. Erwartungen werden geklärt.

LERNZIELE_PHASE:
  - "Vorwissen zum Thema aktivieren"
  - "Lernziele der Einheit verstehen"
  - "Motivation für das Thema entwickeln"

AKTIVITAETEN:
  - typ: "input"
    beschreibung: "Bot stellt sich und das Thema vor"
    dauer: 2
  - typ: "discussion"
    beschreibung: "Vorwissen-Abfrage: Was wisst ihr bereits?"
    dauer: 5
  - typ: "input"
    beschreibung: "Lernziele der Einheit präsentieren"
    dauer: 3

UEBERGANG_ZU:
  naechste_phase: "P02"
  bedingung: "Wenn Vorwissen aktiviert und Ziele klar"
  hinweis: "Super, dann starten wir jetzt mit der ersten Aufgabe!"

RESOURCES_PHASE:
  - "R01"  # Einführungstext
```

---

## Beispiel: Hauptphase mit Aufgaben

```yaml
# PHASE-BLOCK
PHASE_ID: "P02"
PHASE_NAME: "Erarbeitung: Fallbeispiel Kundenbeschwerde"
PHASE_TYP: "hauptteil"
DAUER_MIN: 25
POSITION: 2

BESCHREIBUNG: |
  Die Lernenden bearbeiten ein Fallbeispiel zur Kundenbeschwerde.
  Sie analysieren die Situation und entwickeln Lösungsstrategien.

LERNZIELE_PHASE:
  - "Beschwerdesituationen analysieren können"
  - "Angemessene Reaktionsstrategien entwickeln"
  - "Kommunikationstechniken anwenden"

AKTIVITAETEN:
  - typ: "input"
    beschreibung: "Fallbeispiel präsentieren"
    dauer: 3
  - typ: "task"
    beschreibung: "Aufgabe T01: Situation analysieren"
    dauer: 10
  - typ: "task"
    beschreibung: "Aufgabe T02: Lösung entwickeln"
    dauer: 12

UEBERGANG_ZU:
  naechste_phase: "P03"
  bedingung: "Wenn beide Aufgaben bearbeitet"
  hinweis: "Sehr gut! Bevor wir weitermachen, lass uns kurz reflektieren."

RESOURCES_PHASE:
  - "R02"  # Fallbeispiel-Text
  - "R03"  # Kommunikationsleitfaden
```

---

## Beispiel: Debriefing-Phase

```yaml
# PHASE-BLOCK
PHASE_ID: "P04"
PHASE_NAME: "Debriefing und Transfer"
PHASE_TYP: "debriefing"
DAUER_MIN: 15
POSITION: 4

BESCHREIBUNG: |
  Strukturierte Reflexion der Lernerfahrung nach Kolb.
  Transfer des Gelernten auf reale Situationen.

LERNZIELE_PHASE:
  - "Eigene Lernerfahrung reflektieren"
  - "Kernerkenntnisse formulieren"
  - "Transfer in den Berufsalltag planen"

AKTIVITAETEN:
  - typ: "reflection"
    beschreibung: "Was ist passiert? (Konkrete Erfahrung)"
    dauer: 3
  - typ: "reflection"
    beschreibung: "Warum ist das so passiert? (Analyse)"
    dauer: 4
  - typ: "reflection"
    beschreibung: "Was lernen wir daraus? (Abstraktion)"
    dauer: 4
  - typ: "reflection"
    beschreibung: "Wie wende ich das an? (Transfer)"
    dauer: 4

UEBERGANG_ZU:
  naechste_phase: null  # Letzte Phase
  bedingung: "Wenn alle Reflexionsfragen beantwortet"
  hinweis: "Vielen Dank! Du hast die Lerneinheit erfolgreich abgeschlossen."

RESOURCES_PHASE: []
```

---

## Phasentypen

| Typ | Beschreibung | Typische Position |
|-----|--------------|-------------------|
| `einfuehrung` | Begrüßung, Vorwissen, Ziele | Anfang |
| `hauptteil` | Kern-Lernaktivitäten, Aufgaben | Mitte |
| `abschluss` | Zusammenfassung, Ausblick | Ende |
| `debriefing` | Strukturierte Reflexion | Ende |

---

## Aktivitätstypen

| Typ | Beschreibung | Beispiel |
|-----|--------------|----------|
| `input` | Information vom Bot | Erklärung, Fallbeispiel |
| `discussion` | Dialog/Austausch | Vorwissen-Abfrage |
| `task` | Bearbeitungsaufgabe | Referenz auf TASK-Block |
| `reflection` | Reflexionsfrage | Debriefing-Fragen |

---

## Best Practices

1. **Klare Übergänge**: Definiere, wann und wie zwischen Phasen gewechselt wird
2. **Realistische Zeiten**: Schätze Dauer realistisch, eher großzügiger
3. **Lernziel-Bezug**: Jede Phase sollte auf übergeordnete Lernziele einzahlen
4. **Ressourcen verknüpfen**: Alle benötigten Materialien referenzieren
5. **Abwechslung**: Verschiedene Aktivitätstypen für Engagement
