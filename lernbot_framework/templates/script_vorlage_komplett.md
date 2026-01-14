# 📄 Vollständige Script-Vorlage

Diese Vorlage enthält alle Script-Block-Typen in einem Dokument. Kopiere und fülle sie aus, um einen vollständigen Lernbot zu erstellen.

---

## Anleitung

1. Kopiere diese Vorlage
2. Ersetze alle `{{PLATZHALTER}}` mit deinen Inhalten
3. Lösche nicht benötigte Blöcke oder füge weitere hinzu
4. Prüfe, dass alle Referenzen (IDs) korrekt sind

---

# SCRIPT-DOKUMENT: {{Titel}}

## 1. META-BLOCK

```
[META-BLOCK]
SIM_ID: {{PREFIX}}_{{KUERZEL}}_{{YYYYMMDD}}
Titel: {{Vollständiger Titel der Lernsimulation}}
Version: v1.0
Datum: {{YYYY-MM-DD}}
Autor_Team: {{Name oder Team}}
Zielgruppe: {{z.B. "Berufsschüler*innen Gastronomie, 2. Lehrjahr"}}
Dauer_gesamt: {{z.B. "90 Minuten"}}
Faecher_Kompetenzen: {{z.B. "Warenwirtschaft, Kalkulation"}}
Voraussetzungen: {{z.B. "Grundkenntnisse Rezeptberechnung"}}
Lizenz_Quellen: {{z.B. "CC BY-NC-SA 4.0"}}

Chatbot_Ausgabe_Layout:
  - Kompakte Ausgabe ohne Aufgabenkürzung
  - Rollen intern (nicht im Chat anzeigen)
  - Keine Checkfragen ("Bist du bereit?")
  - Pro TASK: Lernziele → Orientierungsfilter → Aufgabe → Eingabeaufforderung
  - Hints/Rubrik-Feedback erst nach 1. Versuch
[/META-BLOCK]
```

---

## 2. PHASE-BLÖCKE

### Phase 0: Briefing

```
[PHASE-BLOCK]
PHASE_ID: P0_BRIEF
Name: Briefing / Startlayout
Ziel_der_Phase: {{z.B. "Szenario verstehen, Gesamtauftrag erfassen"}}
Zeit: {{z.B. "10-15 Min"}}
Uebergang_Naechste_Phase: {{z.B. "Wenn T0_1 abgeschlossen → P1_BEDARF"}}
[/PHASE-BLOCK]
```

### Phase 1: {{Name}}

```
[PHASE-BLOCK]
PHASE_ID: P1_{{KUERZEL}}
Name: {{Phasenname}}
Ziel_der_Phase: {{Ziel}}
Zeit: {{Zeitrahmen}}
Uebergang_Naechste_Phase: {{Bedingung für Übergang}}
[/PHASE-BLOCK]
```

### Phase 2: {{Name}} (optional)

```
[PHASE-BLOCK]
PHASE_ID: P2_{{KUERZEL}}
Name: {{Phasenname}}
Ziel_der_Phase: {{Ziel}}
Zeit: {{Zeitrahmen}}
Uebergang_Naechste_Phase: {{Bedingung für Übergang}}
[/PHASE-BLOCK]
```

### Debriefing-Phase

```
[PHASE-BLOCK]
PHASE_ID: P{{N}}_DEBRIEF
Name: Debriefing / Reflexion & Transfer
Ziel_der_Phase: Lernen sichern, Transfer herstellen
Zeit: {{z.B. "10-15 Min"}}
Uebergang_Naechste_Phase: Ende der Simulation
[/PHASE-BLOCK]
```

---

## 3. RESOURCE-BLÖCKE

### Ressource 1

```
[RESOURCE-BLOCK]
RESOURCE_ID: R_{{KUERZEL}}_001
Typ: {{Input|Rezept|Tabelle|Worksheet|Text}}
Titel: {{Titel der Ressource}}
Beschreibung_Zweck: {{Kurze Beschreibung}}
Verwendung_in_Tasks: {{Liste der TASK_IDs, z.B. "T1_1, T1_2"}}
Quelle: {{z.B. "intern", "Lehrbuch S. 42"}}
Datei_Anhang: {{Dateiname oder "Anhang A"}}
Maschinenhinweise: {{z.B. "Einheiten in kg, Spalte A = Zutat"}}
[/RESOURCE-BLOCK]
```

### Ressource 2

```
[RESOURCE-BLOCK]
RESOURCE_ID: R_{{KUERZEL}}_002
Typ: {{Input|Rezept|Tabelle|Worksheet|Text}}
Titel: {{Titel der Ressource}}
Beschreibung_Zweck: {{Kurze Beschreibung}}
Verwendung_in_Tasks: {{Liste der TASK_IDs}}
Quelle: {{Quelle}}
Datei_Anhang: {{Dateiname}}
Maschinenhinweise: {{Hinweise für Parsing}}
[/RESOURCE-BLOCK]
```

*Füge weitere RESOURCE-BLOCKs nach Bedarf hinzu.*

---

## 4. TASK-BLÖCKE

### Task 0.1: Auftragsklärung (Briefing)

```
[TASK-BLOCK]
TASK_ID: T0_1_AUFTRAG
Phase: P0_BRIEF
Lernziele: {{z.B. "Szenario und Auftrag korrekt zusammenfassen; Prioritäten setzen"}}
Orientierungsfilter: RB_T0_1 | {{Kriterien kurz, z.B. "C1 Ziele, C2 Priorisierung, C3 Risiken"}}

Aufgabe: {{Aufgaben-Titel}}
{{Vollständiger Aufgabentext.
Beschreibe die Situation/das Szenario.
Liste die Teilaufgaben auf.}}

Eingabeaufforderung: {{Klare Anweisung, z.B. "Schreibe ein Kurzprotokoll (5-8 Sätze) und liste 3 Risiken/To-Dos."}}

— Nach 1. Lösungsversuch ausgeben (nicht in der Erst-Ausgabe) —
Input_Material: {{RESOURCE_IDs, z.B. "R_TEXT_001, R_TABELLE_001"}}
Rubrik: RB_T0_1
Teilhinweise:
  - Hint1: {{Leichter Hinweis, z.B. "Markiere zuerst die Ziele im Text."}}
  - Hint2: {{Mittlerer Hinweis, z.B. "Ordne die To-Dos nach Dringlichkeit."}}
  - Hint3: {{Detaillierter Hinweis, z.B. "Denke an: Zeit, Ressourcen, Abhängigkeiten."}}
Typische_Fehler: {{z.B. "Ziele und Constraints verwechselt"}}
Abgabeformat: {{z.B. "Kurzprotokoll + Bulletpoints"}}
Zeit_Umfang: {{z.B. "10-15 Minuten"}}
[/TASK-BLOCK]
```

### Task 1.1: {{Titel}}

```
[TASK-BLOCK]
TASK_ID: T1_1_{{KUERZEL}}
Phase: P1_{{PHASE_KUERZEL}}
Lernziele: {{Lernziele mit Bloom-Bezug}}
Orientierungsfilter: RB_T1_1 | {{Kriterien kurz}}

Aufgabe: {{Aufgaben-Titel}}
{{Vollständiger Aufgabentext.}}

Eingabeaufforderung: {{Klare Anweisung}}

— Nach 1. Lösungsversuch ausgeben (nicht in der Erst-Ausgabe) —
Input_Material: {{RESOURCE_IDs}}
Rubrik: RB_T1_1
Teilhinweise:
  - Hint1: {{Leichter Hinweis}}
  - Hint2: {{Mittlerer Hinweis}}
  - Hint3: {{Detaillierter Hinweis}}
Typische_Fehler: {{Häufige Fehler}}
Abgabeformat: {{Erwartetes Format}}
Zeit_Umfang: {{Zeitrahmen}}
[/TASK-BLOCK]
```

### Task 1.2: {{Titel}} (optional)

```
[TASK-BLOCK]
TASK_ID: T1_2_{{KUERZEL}}
Phase: P1_{{PHASE_KUERZEL}}
Lernziele: {{Lernziele}}
Orientierungsfilter: RB_T1_2 | {{Kriterien kurz}}

Aufgabe: {{Aufgaben-Titel}}
{{Aufgabentext}}

Eingabeaufforderung: {{Anweisung}}

— Nach 1. Lösungsversuch ausgeben (nicht in der Erst-Ausgabe) —
Input_Material: {{RESOURCE_IDs}}
Rubrik: RB_T1_2
Teilhinweise:
  - Hint1: {{Hinweis 1}}
  - Hint2: {{Hinweis 2}}
  - Hint3: {{Hinweis 3}}
Typische_Fehler: {{Fehler}}
Abgabeformat: {{Format}}
Zeit_Umfang: {{Zeit}}
[/TASK-BLOCK]
```

*Füge weitere TASK-BLOCKs nach Bedarf hinzu.*

---

## 5. RUBRIC-BLÖCKE

### Rubrik für Task 0.1

```
[RUBRIC-BLOCK]
RUBRIC_ID: RB_T0_1
Gilt_fuer_TASK_ID: T0_1_AUFTRAG
Skala: 0-2 (0=nicht erfüllt, 1=teilweise, 2=erfüllt)
Hinweise_zur_Bewertung: Kriteriumsbezogen bewerten, mit Belegen aus der Antwort. Kurz und konstruktiv.

Kriterien:
  - Kriterium_ID: C1_{{Name}}
    Kriterium: {{Was wird bewertet?}}
    Level_0: {{Nicht erfüllt - Beschreibung}}
    Level_1: {{Teilweise erfüllt - Beschreibung}}
    Level_2: {{Vollständig erfüllt - Beschreibung}}
    Ankerbeispiele: {{Konkrete Beispiele}}
  
  - Kriterium_ID: C2_{{Name}}
    Kriterium: {{Was wird bewertet?}}
    Level_0: {{Nicht erfüllt}}
    Level_1: {{Teilweise erfüllt}}
    Level_2: {{Vollständig erfüllt}}
    Ankerbeispiele: {{Beispiele}}
  
  - Kriterium_ID: C3_{{Name}}
    Kriterium: {{Was wird bewertet?}}
    Level_0: {{Nicht erfüllt}}
    Level_1: {{Teilweise erfüllt}}
    Level_2: {{Vollständig erfüllt}}
    Ankerbeispiele: {{Beispiele}}
[/RUBRIC-BLOCK]
```

### Rubrik für Task 1.1

```
[RUBRIC-BLOCK]
RUBRIC_ID: RB_T1_1
Gilt_fuer_TASK_ID: T1_1_{{KUERZEL}}
Skala: 0-2 (0=nicht erfüllt, 1=teilweise, 2=erfüllt)
Hinweise_zur_Bewertung: Kriteriumsbezogen, mit Belegen. Konstruktiv formulieren.

Kriterien:
  - Kriterium_ID: C1_{{Name}}
    Kriterium: {{Beschreibung}}
    Level_0: {{Nicht erfüllt}}
    Level_1: {{Teilweise erfüllt}}
    Level_2: {{Vollständig erfüllt}}
    Ankerbeispiele: {{Beispiele}}
  
  - Kriterium_ID: C2_{{Name}}
    Kriterium: {{Beschreibung}}
    Level_0: {{Nicht erfüllt}}
    Level_1: {{Teilweise erfüllt}}
    Level_2: {{Vollständig erfüllt}}
    Ankerbeispiele: {{Beispiele}}
[/RUBRIC-BLOCK]
```

*Füge für jeden TASK-Block einen passenden RUBRIC-Block hinzu.*

---

## 6. MODEL-BLÖCKE (optional)

### Musterlösung für Task 1.1

```
[MODEL-BLOCK]
MODEL_ID: M_T1_1
Gilt_fuer_TASK_ID: T1_1_{{KUERZEL}}
Version: v1.0

Musterantwort: |
  {{Vollständige, korrekte Beispiellösung.
  Format sollte dem geforderten Abgabeformat entsprechen.
  Alle Kriterien der Rubrik erfüllen.}}

Erklaerung: |
  {{Warum ist diese Lösung gut?
  Bezug zu den Bewertungskriterien herstellen.}}

Varianten: |
  {{Alternative akzeptable Antworten oder Lösungswege.}}

Bewertung_nach_Rubrik:
  - C1_{{Name}}: Level 2 – {{Begründung}}
  - C2_{{Name}}: Level 2 – {{Begründung}}
[/MODEL-BLOCK]
```

*MODEL-Blöcke sind optional und können später ergänzt werden.*

---

## 7. DEBRIEF-BLOCK

```
[DEBRIEF-BLOCK]
DEBRIEF_ID: D_GESAMT
Zugehoerige_Phasen: {{Liste aller Phasen, z.B. "P0_BRIEF, P1_BEDARF, P2_BESTAND"}}
Ziel: {{z.B. "Entscheidungen reflektieren, Fehlerquellen erkennen, Transfer herstellen"}}
Zeit: {{z.B. "10-15 Minuten"}}

Beschreibung_Was_ist_passiert:
  - "Welche Entscheidung war am schwierigsten und warum?"
  - "Wo gab es Unsicherheiten?"
  - "{{Weitere Frage zur Erfahrung}}"

Analyse_Warum:
  - "Welche Informationen waren entscheidend?"
  - "Welche Annahmen hast du getroffen?"
  - "{{Weitere Frage zu Ursachen}}"

Abstraktion_Was_lernen_wir:
  - "Welche Strategie hat am besten funktioniert?"
  - "Was würdest du beim nächsten Mal anders machen?"

Transfer_Praxis:
  - "Wo in der Praxis ist das relevant?"
  - "Welche Checkliste würdest du ableiten?"

Alternative_Handlungen:
  - "Welche andere Lösung wäre auch vertretbar gewesen?"

Abschlussprodukt: {{z.B. "6-8 Sätze Reflexion + 3 Learnings als Bulletpoints"}}
[/DEBRIEF-BLOCK]
```

---

## 8. REFERENZ-MAPPING

| TASK_ID | RUBRIC_ID | MODEL_ID | RESOURCE_IDs |
|---------|-----------|----------|--------------|
| T0_1_AUFTRAG | RB_T0_1 | M_T0_1 | R_TEXT_001 |
| T1_1_{{KUERZEL}} | RB_T1_1 | M_T1_1 | R_{{...}}, R_{{...}} |
| T1_2_{{KUERZEL}} | RB_T1_2 | - | R_{{...}} |
| ... | ... | ... | ... |

---

## ✅ Checkliste vor Verwendung

- [ ] Alle `{{PLATZHALTER}}` ersetzt
- [ ] Alle IDs eindeutig
- [ ] Alle Referenzen gültig (TASK → RUBRIC, TASK → RESOURCE)
- [ ] Mindestens 3 Hints pro TASK
- [ ] Mindestens 2-3 Kriterien pro RUBRIC
- [ ] DEBRIEF-Block vorhanden
- [ ] Referenz-Mapping aktualisiert

---

## 📝 Hinweise

### ID-Konventionen
- **PHASE**: `P{Nr}_{KUERZEL}` (z.B. P1_BEDARF)
- **TASK**: `T{Phase}_{Nr}_{KUERZEL}` (z.B. T1_1_BEDARF)
- **RUBRIC**: `RB_T{Phase}_{Nr}` (z.B. RB_T1_1)
- **MODEL**: `M_T{Phase}_{Nr}` (z.B. M_T1_1)
- **RESOURCE**: `R_{KUERZEL}_{Nr}` (z.B. R_REZEPT_001)
- **DEBRIEF**: `D_{SCOPE}` (z.B. D_GESAMT, D_P1)

### Block-Syntax
Alle Blöcke verwenden die Syntax:
```
[BLOCK-TYP]
...Inhalt...
[/BLOCK-TYP]
```

### Scaffolds (Hints)
Die drei Hint-Stufen:
1. **Hint1**: Regt zum Nachdenken an (keine Richtung)
2. **Hint2**: Gibt eine Richtung vor
3. **Hint3**: Konkrete Hilfestellung (fast Teillösung)
