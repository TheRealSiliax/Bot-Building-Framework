# RUBRIC Script Template

Bewertungskriterien für einen Lernbot.

## Verwendung

Dieses Template definiert Bewertungskriterien für einen spezifischen Task. Rubriken werden für formatives Feedback verwendet und erst nach dem ersten Lösungsversuch angewandt.

## Template

```markdown
[RUBRIC-BLOCK]
RUBRIC_ID: RB_{{TASK_REF}}
Gilt_fuer_TASK_ID: {{TASK_ID}}
Skala: {{Skalenbeschreibung, z.B. "0-2 (0=nicht erfüllt, 1=teilweise, 2=erfüllt)"}}
Hinweise_zur_Bewertung: {{Generelle Bewertungshinweise}}

Kriterien:
  - Kriterium_ID: C1_{{Name}}
    Kriterium: {{Was wird bewertet?}}
    Level_0: {{Beschreibung: nicht erfüllt}}
    Level_1: {{Beschreibung: teilweise erfüllt}}
    Level_2: {{Beschreibung: vollständig erfüllt}}
    Ankerbeispiele: {{Konkrete Beispiele für die Levels}}
  
  - Kriterium_ID: C2_{{Name}}
    Kriterium: {{Was wird bewertet?}}
    Level_0: {{Beschreibung: nicht erfüllt}}
    Level_1: {{Beschreibung: teilweise erfüllt}}
    Level_2: {{Beschreibung: vollständig erfüllt}}
    Ankerbeispiele: {{Konkrete Beispiele für die Levels}}
  
  {{... weitere Kriterien ...}}
[/RUBRIC-BLOCK]
```

## Feld-Beschreibungen

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| RUBRIC_ID | ✓ | Eindeutige ID im Format RB_{TASK_REF} |
| Gilt_fuer_TASK_ID | ✓ | Referenz auf den zugehörigen Task |
| Skala | ✓ | Beschreibung der Bewertungsskala |
| Hinweise_zur_Bewertung | ✓ | Generelle Hinweise für die Bewertung |
| Kriterien | ✓ | Liste der Bewertungskriterien |
| Kriterium_ID | ✓ | Eindeutige ID pro Kriterium |
| Kriterium | ✓ | Was genau wird bewertet? |
| Level_0/1/2 | ✓ | Beschreibung der einzelnen Levels |
| Ankerbeispiele | ○ | Konkrete Beispiele zur Verdeutlichung |

## Kriterien-Prinzipien

### SMART-Kriterien für Rubriken

- **S**pezifisch: Klar definiert, was bewertet wird
- **M**essbar: Beobachtbares Verhalten/Output
- **A**ngemessen: Passend zum Lernziel und Schwierigkeitsgrad
- **R**elevant: Wichtig für das Lernziel
- **T**ransparent: Für Lernende nachvollziehbar

### Level-Beschreibungen

Die Levels sollten **distinkt** und **beobachtbar** formuliert sein:

| Level | Charakteristik | Signalwörter |
|-------|---------------|--------------|
| 0 | Nicht erfüllt | fehlt, nicht vorhanden, keine Angabe |
| 1 | Teilweise erfüllt | unvollständig, teilweise, mit Fehlern |
| 2 | Vollständig erfüllt | korrekt, vollständig, nachvollziehbar |

### Typische Kriterien-Kategorien

- **Inhaltliche Richtigkeit**: Korrektheit der Fakten/Berechnungen
- **Vollständigkeit**: Alle geforderten Elemente vorhanden
- **Begründung/Argumentation**: Qualität der Erklärung
- **Formale Aspekte**: Einheiten, Format, Struktur
- **Transfer**: Anwendung auf neue Situationen

## Beispiel

```markdown
[RUBRIC-BLOCK]
RUBRIC_ID: RB_T1_1
Gilt_fuer_TASK_ID: T1_1_BEDARF
Skala: 0-2 (0=nicht erfüllt, 1=teilweise, 2=erfüllt)
Hinweise_zur_Bewertung: Kriteriumsbezogen bewerten, mit konkreten Belegen aus der Schülerantwort. Feedback kurz und konstruktiv formulieren.

Kriterien:
  - Kriterium_ID: C1_Skalierung
    Kriterium: Korrekte Hochrechnung der Rezeptmengen auf 50 Personen
    Level_0: Keine oder falsche Skalierung; Mengen stimmen nicht mit Portionszahl überein.
    Level_1: Skalierung grundsätzlich richtig, aber einzelne Rechenfehler oder unvollständig.
    Level_2: Alle Mengen korrekt auf 50 Personen hochgerechnet, Rechnung nachvollziehbar.
    Ankerbeispiele: "Pannfisch × 10 korrekt, Rote Grütze vergessen" → Level 1

  - Kriterium_ID: C2_Vollstaendigkeit
    Kriterium: Alle Zutaten aus allen Rezepten + Getränke erfasst
    Level_0: Mehr als 30% der Zutaten fehlen.
    Level_1: 10-30% der Zutaten fehlen oder eine Kategorie vergessen.
    Level_2: Alle Zutaten vollständig erfasst (Speisen + Getränke).
    Ankerbeispiele: "Getränke komplett vergessen" → Level 1

  - Kriterium_ID: C3_Einheiten
    Kriterium: Korrekte und konsistente Einheiten (kg, L, Stück, etc.)
    Level_0: Einheiten fehlen durchgehend oder sind falsch.
    Level_1: Einheiten teilweise angegeben, vereinzelt inkonsistent.
    Level_2: Alle Mengen mit korrekten, konsistenten Einheiten versehen.
    Ankerbeispiele: "500 Möhren statt 5 kg Möhren" → Level 0

  - Kriterium_ID: C4_Quelle_Moehrensuppe
    Kriterium: Quelle für das recherchierte Möhrensuppen-Rezept angegeben
    Level_0: Keine Quelle genannt.
    Level_1: Quelle genannt, aber unvollständig (z.B. nur "Internet").
    Level_2: Vollständige Quellenangabe (URL, Kochbuch + Seite, o.ä.).
    Ankerbeispiele: "Rezept von Chefkoch.de" → Level 1, "https://chefkoch.de/rezept/123" → Level 2
[/RUBRIC-BLOCK]
```

## Feedback-Muster

Basierend auf der Rubrik sollte das Feedback folgendem Muster folgen:

```markdown
**Feedback zu deiner Antwort:**

✓ **Was gut ist:**
- [C1_Skalierung, Level 2]: Deine Hochrechnung auf 50 Personen ist korrekt.
- [C2_Vollständigkeit, Level 2]: Alle Zutaten erfasst, inkl. Getränke.

⚠ **Was fehlt/verbessert werden kann:**
- [C3_Einheiten, Level 1]: Bei den Möhren fehlt die Einheit (kg).
- [C4_Quelle, Level 1]: Bitte gib die vollständige URL an.

→ **Nächster Schritt:** Ergänze die fehlenden Einheiten und die vollständige Quelle.
```
