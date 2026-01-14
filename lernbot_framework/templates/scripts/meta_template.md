# META Script Template

Dokument-Metadaten für einen Lernbot.

## Verwendung

Dieses Template definiert die grundlegenden Informationen über die Lernsimulation/den Lernbot.

## Template

```markdown
[META-BLOCK]
SIM_ID: {{PREFIX}}_{{KUERZEL}}_{{DATUM_YYYYMMDD}}
Titel: {{Vollständiger Titel der Lernsimulation}}
Version: v{{X.Y}}
Datum: {{YYYY-MM-DD}}
Autor_Team: {{Name oder Team}}
Zielgruppe: {{Beschreibung der Zielgruppe}}
Dauer_gesamt: {{Zeitrahmen, z.B. "90 Minuten"}}
Faecher_Kompetenzen: {{Fachbereiche und Kompetenzen}}
Voraussetzungen: {{Benötigtes Vorwissen}}
Lizenz_Quellen: {{Lizenz und Quellenangaben}}

Chatbot_Ausgabe_Layout:
  - Kompakte Ausgabe ohne Aufgabenkürzung
  - Rollen intern (nicht im Chat anzeigen)
  - Keine Checkfragen ("Bist du bereit?")
  - Pro TASK: Lernziele → Orientierungsfilter → Aufgabe → Eingabeaufforderung
  - Hints/Rubrik-Feedback erst nach 1. Versuch
[/META-BLOCK]
```

## Feld-Beschreibungen

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| SIM_ID | ✓ | Eindeutige ID im Format PREFIX_KUERZEL_DATUM |
| Titel | ✓ | Vollständiger, beschreibender Titel |
| Version | ✓ | Versionsnummer (Semantic Versioning empfohlen) |
| Datum | ✓ | Erstellungs-/Änderungsdatum |
| Autor_Team | ○ | Ersteller oder verantwortliches Team |
| Zielgruppe | ✓ | Konkrete Beschreibung (z.B. "Berufsschüler Gastronomie, 2. Lehrjahr") |
| Dauer_gesamt | ✓ | Gesamtzeit für die Lernsimulation |
| Faecher_Kompetenzen | ✓ | Fachbereiche und zu fördernde Kompetenzen |
| Voraussetzungen | ○ | Benötigtes Vorwissen der Lernenden |
| Lizenz_Quellen | ○ | Lizenzinformationen und Quellenangaben |
| Chatbot_Ausgabe_Layout | ✓ | Regeln für die Bot-Ausgabe |

## Beispiel

```markdown
[META-BLOCK]
SIM_ID: SIM_TAGUNG_DOCK03_20260114
Titel: Tagung im Hotel Dock 03 – Wareneinkauf und Lieferantenauswahl
Version: v1.1
Datum: 2026-01-14
Autor_Team: Fachbereich Gastronomie
Zielgruppe: Berufsschüler*innen Gastronomie/Hotelwesen, 2. Lehrjahr
Dauer_gesamt: 90-120 Minuten
Faecher_Kompetenzen: Warenwirtschaft, Kalkulation, Lieferantenmanagement
Voraussetzungen: Grundkenntnisse Rezeptberechnung, Excel/Tabellenkalkulation
Lizenz_Quellen: CC BY-NC-SA 4.0, Eigenentwicklung

Chatbot_Ausgabe_Layout:
  - Kompakte Ausgabe ohne Aufgabenkürzung
  - Rollen intern (nicht im Chat anzeigen)
  - Keine Checkfragen ("Bist du bereit?")
  - Pro TASK: Lernziele → Orientierungsfilter → Aufgabe → Eingabeaufforderung
  - Hints/Rubrik-Feedback erst nach 1. Versuch
[/META-BLOCK]
```
