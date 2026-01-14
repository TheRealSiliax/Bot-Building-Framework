# TASK Script Template

Aufgaben-Definition für einen Lernbot.

## Verwendung

Dieses Template definiert einzelne Aufgaben/Tasks innerhalb einer Lernsimulation. Jeder Task ist einer Phase zugeordnet und hat eine zugehörige Rubrik.

## Template

```markdown
[TASK-BLOCK]
TASK_ID: T{{Phase}}_{{Nr}}_{{KUERZEL}}
Phase: {{PHASE_ID}}
Lernziele: {{Lernziele mit Bloom-Bezug}}
Orientierungsfilter: {{RUBRIC_ID}} | {{Kriterien kurz, kommasepariert}}

Aufgabe: {{Aufgaben-Titel}}
{{Vollständiger Aufgabentext aus dem Material.
Kann mehrzeilig sein und alle relevanten Informationen enthalten.}}

Eingabeaufforderung: {{Klare Handlungsanweisung für die Lernenden}}

— Nach 1. Lösungsversuch ausgeben (nicht in der Erst-Ausgabe) —
Input_Material: {{RESOURCE_ID_1}}, {{RESOURCE_ID_2}}, ...
Rubrik: {{RUBRIC_ID}}
Teilhinweise:
  - Hint1: {{Leichter Hinweis - regt zum Nachdenken an}}
  - Hint2: {{Mittlerer Hinweis - gibt Richtung vor}}
  - Hint3: {{Detaillierter Hinweis - konkrete Hilfestellung}}
Typische_Fehler: {{Häufige Fehler und Missverständnisse}}
Abgabeformat: {{Erwartetes Format der Abgabe}}
Zeit_Umfang: {{Zeitrahmen für diesen Task}}
[/TASK-BLOCK]
```

## Feld-Beschreibungen

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| TASK_ID | ✓ | Eindeutige ID im Format T{Phase}_{Nr}_{KÜRZEL} |
| Phase | ✓ | Referenz auf PHASE_ID |
| Lernziele | ✓ | Konkrete Lernziele mit Bloom-Taxonomie-Bezug |
| Orientierungsfilter | ✓ | Rubrik-ID und Kurzform der Kriterien |
| Aufgabe | ✓ | Titel und vollständiger Aufgabentext |
| Eingabeaufforderung | ✓ | Klare Anweisung, was die Lernenden tun sollen |
| Input_Material | ○ | Liste der benötigten RESOURCE_IDs |
| Rubrik | ✓ | Referenz auf zugehörige RUBRIC_ID |
| Teilhinweise | ✓ | Gestufte Scaffolds (Hint1 → Hint2 → Hint3) |
| Typische_Fehler | ○ | Bekannte Fehlerquellen |
| Abgabeformat | ○ | Erwartetes Ausgabeformat |
| Zeit_Umfang | ○ | Geschätzte Bearbeitungszeit |

## Scaffold-Prinzipien

Die drei Hint-Stufen folgen dem Prinzip der **graduellen Enthüllung**:

1. **Hint1 (Leicht)**: Regt zum Nachdenken an, ohne Lösungsrichtung
   - "Welche Informationen brauchst du aus der Tabelle?"
   - "Überlege: Was ist das Ziel der Aufgabe?"

2. **Hint2 (Mittel)**: Gibt eine Richtung vor
   - "Beginne mit dem Bestand und vergleiche mit dem Bedarf."
   - "Nutze die Kriterien in Spalte C."

3. **Hint3 (Detailliert)**: Konkrete Hilfestellung, fast Teillösung
   - "Ziehe von jedem Bedarf den Bestand ab: Bedarf - Bestand = zu bestellen"
   - "Die wichtigsten Kriterien sind: Preis, Lieferzeit, Qualität"

## Beispiel

```markdown
[TASK-BLOCK]
TASK_ID: T1_1_BEDARF
Phase: P1_BEDARF
Lernziele: Warenbedarf für 50 Personen korrekt ableiten (Skalierung, Vollständigkeit, Einheiten). Bloom: Anwenden.
Orientierungsfilter: RB_T1_1 | C1 Skalierung, C2 Vollständigkeit, C3 Einheiten, C4 Quelle Möhrensuppe

Aufgabe: Warenanforderung feststellen
Im Folgenden sollst du den Warenbedarf (Lebensmittel und Getränke) für die Tagung im Hotel Dock 03 ermitteln.

Für die Tagung sollen die folgenden Speisen angeboten werden:
- Möhrensuppe mit Croutons (Rezept muss recherchiert werden)
- Hamburger Pannfisch mit Blattspinat und Bratkartoffeln (Rezept für 5 Personen)
- Hamburger Rote Grütze mit Vanilleeis (Rezept für 10 Personen)

Getränke:
- Wasser
- Apfelsaft
- Kaffee

a) Ermittel die Warenanforderung der Tagung und fülle die Tabelle aus.

Eingabeaufforderung: Gib jetzt deine berechnete Warenanforderung ein (als Liste oder Tabelle) inkl. Einheiten und nenne deine Quelle für das Möhrensuppe-Rezept.

— Nach 1. Lösungsversuch ausgeben (nicht in der Erst-Ausgabe) —
Input_Material: R_RECHERCHE_MOEHRENSUPPE, R_REZEPT_PANNFISCH, R_REZEPT_ROTEGRUETZE, R_FUNC_SHEET
Rubrik: RB_T1_1
Teilhinweise:
  - Hint1: Wie viele Personen sind im Original-Rezept? Wie viele brauchst du?
  - Hint2: Rezept auf 50 Personen hochrechnen: Menge × (50 ÷ Original-Portionen)
  - Hint3: Pannfisch: Faktor 10 (50÷5), Rote Grütze: Faktor 5 (50÷10). Prüfe alle Einheiten.
Typische_Fehler: Falscher Skalierungsfaktor, Einheiten vergessen, Möhrensuppe-Quelle nicht angegeben
Abgabeformat: Tabelle mit Spalten: Zutat | Menge | Einheit
Zeit_Umfang: 25-35 Minuten
[/TASK-BLOCK]
```
