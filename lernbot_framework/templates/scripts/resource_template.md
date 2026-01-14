# RESOURCE-Block Template

Template für die Definition von Lernressourcen im Bot-Script.

---

## Syntax

```yaml
# RESOURCE-BLOCK
RESOURCE_ID: "R{{NUMMER}}"
RESOURCE_NAME: "{{Bezeichnung}}"
RESOURCE_TYP: "{{text|tabelle|bild|video|link|datei}}"
PHASE_REF: "P{{NUMMER}}"  # In welcher Phase verwendet

FORMAT: "{{markdown|plain|html}}"
SICHTBARKEIT: "{{immer|bei_bedarf|lehrkraft_only}}"

INHALT: |
  {{Der eigentliche Ressourceninhalt}}

VERWENDUNG:
  kontext: "{{Wann/wie wird die Ressource eingesetzt}}"
  trigger: "{{Was löst die Anzeige aus}}"

METADATEN:
  quelle: "{{Quellenangabe falls extern}}"
  lizenz: "{{Lizenzinfo falls relevant}}"
  version: "{{Versionsnummer}}"
```

---

## Beispiel: Fallbeispiel-Text

```yaml
# RESOURCE-BLOCK
RESOURCE_ID: "R01"
RESOURCE_NAME: "Fallbeispiel: Kundenbeschwerde im Restaurant"
RESOURCE_TYP: "text"
PHASE_REF: "P02"

FORMAT: "markdown"
SICHTBARKEIT: "immer"

INHALT: |
  ## Situation
  
  Es ist Samstagabend, 19:30 Uhr. Das Restaurant ist zu 80% ausgelastet.
  
  Herr Müller (45) kommt mit seiner Frau zum Abendessen. Sie haben vor 
  zwei Wochen einen Tisch für 19:00 Uhr reserviert. Als sie ankommen, 
  ist ihr Tisch jedoch noch von anderen Gästen besetzt.
  
  **Herr Müller (verärgert):**
  > "Das kann doch nicht sein! Wir haben extra reserviert und jetzt 
  > sollen wir warten? Das ist eine Frechheit!"
  
  Die Gäste am Tisch scheinen gerade erst ihr Dessert bestellt zu haben.
  
  **Verfügbare Optionen:**
  - Ein anderer Tisch in der Nähe der Küchentür ist frei
  - Die Bar hat Plätze, Wartezeit ca. 15 Minuten
  - Ein Nachbar-Restaurant hätte Plätze

VERWENDUNG:
  kontext: "Wird zu Beginn der Aufgabenphase präsentiert"
  trigger: "Automatisch bei Phase P02"

METADATEN:
  quelle: "Eigene Entwicklung"
  lizenz: "Intern"
  version: "1.0"
```

---

## Beispiel: Informationstabelle

```yaml
# RESOURCE-BLOCK
RESOURCE_ID: "R02"
RESOURCE_NAME: "Kommunikationstechniken bei Beschwerden"
RESOURCE_TYP: "tabelle"
PHASE_REF: "P02"

FORMAT: "markdown"
SICHTBARKEIT: "bei_bedarf"

INHALT: |
  | Technik | Beschreibung | Beispiel |
  |---------|--------------|----------|
  | Aktives Zuhören | Aufmerksamkeit zeigen, Verständnis signalisieren | "Ich verstehe, dass Sie verärgert sind." |
  | Ich-Botschaften | Eigene Wahrnehmung kommunizieren | "Ich sehe, dass die Situation unangenehm ist." |
  | Lösungsorientierung | Auf Lösungen fokussieren | "Lassen Sie uns gemeinsam eine Lösung finden." |
  | Empathie zeigen | Gefühle anerkennen | "Das wäre mir auch unangenehm." |
  | Konkret werden | Praktische Optionen anbieten | "Ich kann Ihnen folgendes anbieten..." |

VERWENDUNG:
  kontext: "Als Hilfestellung während der Aufgabenbearbeitung"
  trigger: "Wenn Lernender nach Hilfe fragt oder unsicher wirkt"

METADATEN:
  quelle: "Schulungsmaterial Beschwerdemanagement"
  lizenz: "Intern"
  version: "1.0"
```

---

## Beispiel: Checkliste

```yaml
# RESOURCE-BLOCK
RESOURCE_ID: "R03"
RESOURCE_NAME: "Checkliste: Professioneller Umgang mit Beschwerden"
RESOURCE_TYP: "text"
PHASE_REF: "P02"

FORMAT: "markdown"
SICHTBARKEIT: "bei_bedarf"

INHALT: |
  ### Checkliste: Beschwerdemanagement
  
  **Sofort-Reaktion:**
  - [ ] Ruhe bewahren
  - [ ] Blickkontakt halten
  - [ ] Aktiv zuhören
  - [ ] Nicht unterbrechen
  
  **Verständnis zeigen:**
  - [ ] Gefühle anerkennen
  - [ ] Problem in eigenen Worten wiederholen
  - [ ] Für Unannehmlichkeiten entschuldigen
  
  **Lösung finden:**
  - [ ] Optionen anbieten (mind. 2)
  - [ ] Gast wählen lassen
  - [ ] Konkrete nächste Schritte nennen
  
  **Nachbereitung:**
  - [ ] Lösung umsetzen
  - [ ] Nachfragen, ob zufrieden
  - [ ] Aus Situation lernen

VERWENDUNG:
  kontext: "Als Orientierungshilfe und zur Selbstkontrolle"
  trigger: "Auf Anfrage oder nach erstem Lösungsversuch"

METADATEN:
  quelle: "Eigene Entwicklung basierend auf IHK-Standards"
  lizenz: "Intern"
  version: "1.0"
```

---

## Beispiel: Externer Link

```yaml
# RESOURCE-BLOCK
RESOURCE_ID: "R04"
RESOURCE_NAME: "Vertiefung: DEHOGA Leitfaden Beschwerdemanagement"
RESOURCE_TYP: "link"
PHASE_REF: "P04"

FORMAT: "plain"
SICHTBARKEIT: "bei_bedarf"

INHALT: |
  https://www.dehoga.de/beschwerdemanagement-leitfaden

VERWENDUNG:
  kontext: "Für Lernende, die tiefer einsteigen möchten"
  trigger: "Im Debriefing als weiterführende Ressource"

METADATEN:
  quelle: "DEHOGA Bundesverband"
  lizenz: "Extern"
  version: "Stand 2025"
```

---

## Ressourcentypen

| Typ | Beschreibung | Verwendung |
|-----|--------------|------------|
| `text` | Fließtext, Fallbeispiele | Hauptinhalte, Szenarien |
| `tabelle` | Strukturierte Daten | Übersichten, Vergleiche |
| `bild` | Bildmaterial | Visualisierungen |
| `video` | Video-Ressourcen | Erklärvideos |
| `link` | Externe URLs | Weiterführende Infos |
| `datei` | Downloadbare Dateien | Arbeitsblätter |

---

## Sichtbarkeitsoptionen

| Option | Beschreibung |
|--------|--------------|
| `immer` | Wird automatisch angezeigt |
| `bei_bedarf` | Wird auf Anfrage oder bei Trigger angezeigt |
| `lehrkraft_only` | Nur im Lehrkraft-Modus sichtbar |

---

## Best Practices

1. **Eindeutige IDs**: Jede Ressource braucht eine einzigartige ID
2. **Phase verknüpfen**: Klare Zuordnung zu Lernphasen
3. **Trigger definieren**: Wann soll die Ressource erscheinen?
4. **Kompakt halten**: Ressourcen sollten überschaubar sein
5. **Quellen angeben**: Besonders bei externen Inhalten
