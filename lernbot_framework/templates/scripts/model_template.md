# MODEL Script Template

Musterlösungen für einen Lernbot.

## Verwendung

Dieses Template definiert Musterlösungen für Tasks. Musterlösungen werden **nur unter bestimmten Bedingungen** gezeigt:
1. Nach ernsthaftem Versuch der Lernenden
2. Im Lehrkraft-Modus
3. Nach Durchlauf aller Scaffolds (Hint1 → Hint2 → Hint3)

## Template

```markdown
[MODEL-BLOCK]
MODEL_ID: M_{{TASK_REF}}
Gilt_fuer_TASK_ID: {{TASK_ID}}
Version: {{v1.0}}

Musterantwort: |
  {{Vollständige, korrekte Beispiellösung.
  Kann mehrzeilig sein und alle erwarteten Elemente enthalten.
  Format sollte dem geforderten Abgabeformat entsprechen.}}

Erklaerung: |
  {{Erklärung, warum diese Lösung gut ist.
  Bezug zu den Bewertungskriterien herstellen.}}

Varianten: |
  {{Alternative akzeptable Antworten oder Lösungswege.
  Zeigt, dass es nicht nur "die eine richtige Antwort" gibt.}}

Bewertung_nach_Rubrik:
  - {{KRITERIUM_ID}}: Level 2 – {{kurze Begründung}}
  - {{KRITERIUM_ID}}: Level 2 – {{kurze Begründung}}
[/MODEL-BLOCK]
```

## Feld-Beschreibungen

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| MODEL_ID | ✓ | Eindeutige ID im Format M_{TASK_REF} |
| Gilt_fuer_TASK_ID | ✓ | Referenz auf den zugehörigen Task |
| Version | ○ | Versionsnummer der Musterlösung |
| Musterantwort | ✓ | Vollständige, korrekte Beispiellösung |
| Erklaerung | ○ | Warum ist diese Lösung gut? |
| Varianten | ○ | Alternative akzeptable Antworten |
| Bewertung_nach_Rubrik | ○ | Selbstbewertung anhand der Kriterien |

## Prinzipien für gute Musterlösungen

### 1. Vollständigkeit

Die Musterlösung sollte **alle** Anforderungen der Aufgabe erfüllen und als "Level 2" in allen Rubrik-Kriterien bewertet werden können.

### 2. Nachvollziehbarkeit

Die Lösung sollte den Denkprozess zeigen, nicht nur das Ergebnis:
- ❌ "Die Antwort ist 500 kg."
- ✓ "Pannfisch für 5 Personen: 250g Fisch → 50 Personen: 250g × 10 = 2.500g = 2,5 kg"

### 3. Format-Konformität

Die Musterlösung sollte dem geforderten Abgabeformat entsprechen (Tabelle, Liste, Fließtext, etc.).

### 4. Varianten

Wenn mehrere Lösungswege akzeptabel sind, sollten Varianten gezeigt werden. Das fördert Flexibilität im Denken.

## Beispiel

```markdown
[MODEL-BLOCK]
MODEL_ID: M_T1_1_BEDARF
Gilt_fuer_TASK_ID: T1_1_BEDARF
Version: v1.0

Musterantwort: |
  **Warenanforderung für Tagung (50 Personen)**
  
  | Zutat | Menge | Einheit | Quelle |
  |-------|-------|---------|--------|
  | **Möhrensuppe** | | | |
  | Möhren | 5 | kg | chefkoch.de/rezept/moehrensuppe |
  | Zwiebeln | 500 | g | " |
  | Gemüsebrühe | 5 | L | " |
  | Sahne | 500 | ml | " |
  | Croutons | 500 | g | " |
  | **Hamburger Pannfisch** (Rezept ×10) | | | |
  | Kabeljau | 2,5 | kg | Rezept Material |
  | Kartoffeln | 5 | kg | " |
  | Blattspinat | 2,5 | kg | " |
  | Senfsauce | 2 | L | " |
  | **Rote Grütze** (Rezept ×5) | | | |
  | Beeren-Mix | 2,5 | kg | Rezept Material |
  | Zucker | 750 | g | " |
  | Speisestärke | 250 | g | " |
  | Vanilleeis | 50 | Kugeln | " |
  | **Getränke** | | | |
  | Wasser | 25 | L | Schätzung 0,5L/Person |
  | Apfelsaft | 10 | L | Schätzung 0,2L/Person |
  | Kaffee | 100 | Tassen | Schätzung 2 Tassen/Person |

Erklaerung: |
  Diese Lösung erfüllt alle Kriterien:
  - **Skalierung**: Pannfisch ×10 (5→50), Rote Grütze ×5 (10→50)
  - **Vollständigkeit**: Alle drei Gänge + Getränke erfasst
  - **Einheiten**: Konsistent in kg, g, L, ml, Stück
  - **Quelle**: Möhrensuppe mit URL belegt
  
  Die Getränkemengen basieren auf üblichen Schätzwerten für Tagungen.

Varianten: |
  - Möhrensuppe-Rezept kann von anderen Quellen stammen (Kochbuch, anderes Portal)
  - Getränkemengen können variieren je nach Annahmen (0,3-0,7L Wasser/Person akzeptabel)
  - Tabelle kann auch als Liste formatiert sein
  - Einheiten können in anderen Formaten angegeben sein (2500g statt 2,5kg)

Bewertung_nach_Rubrik:
  - C1_Skalierung: Level 2 – Alle Hochrechnungen korrekt mit Faktor
  - C2_Vollstaendigkeit: Level 2 – Alle Kategorien abgedeckt
  - C3_Einheiten: Level 2 – Durchgehend korrekte Einheiten
  - C4_Quelle: Level 2 – Vollständige URL für Möhrensuppe
[/MODEL-BLOCK]
```

## Ausgabe-Regeln

Im Chatbot sollte die Musterlösung wie folgt eingeführt werden:

```markdown
**Beispiellösung** [Model: M_T1_1_BEDARF]

Hier ist eine vollständige Beispiellösung, an der du dich orientieren kannst:

{{Musterantwort}}

**Warum ist das eine gute Lösung?**
{{Erklärung}}

**Hinweis:** Es gibt oft mehrere richtige Wege. Deine Lösung muss nicht identisch sein, 
solange sie die Kriterien erfüllt.
```
