# DEBRIEF Script Template

Reflexions- und Transfer-Struktur für einen Lernbot.

## Verwendung

Dieses Template definiert die Debriefing-Phase am Ende einer Lernsimulation. Das Debriefing sichert den Lerntransfer und fördert Metakognition.

## Theoretischer Hintergrund

Das Debriefing-Template basiert auf dem **Kolb'schen Lernzyklus**:
1. **Konkrete Erfahrung** → Was ist passiert?
2. **Reflektierende Beobachtung** → Warum ist es passiert?
3. **Abstrakte Konzeptbildung** → Was lernen wir daraus?
4. **Aktives Experimentieren** → Wie wenden wir es an?

## Template

```markdown
[DEBRIEF-BLOCK]
DEBRIEF_ID: D_{{Phase_oder_Gesamt}}
Zugehoerige_Phasen: {{Liste der PHASE_IDs}}
Ziel: {{Reflexionsziel}}
Zeit: {{Zeitrahmen}}

Beschreibung_Was_ist_passiert:
  - {{Reflexionsfrage 1 zur Erfahrung}}
  - {{Reflexionsfrage 2 zur Erfahrung}}
  - {{Reflexionsfrage 3 zur Erfahrung}}

Analyse_Warum:
  - {{Analysefrage 1 zu Ursachen/Entscheidungen}}
  - {{Analysefrage 2 zu Ursachen/Entscheidungen}}
  - {{Analysefrage 3 zu Ursachen/Entscheidungen}}

Abstraktion_Was_lernen_wir:
  - {{Generalisierungsfrage 1}}
  - {{Generalisierungsfrage 2}}

Transfer_Praxis:
  - {{Transferfrage 1 zur realen Anwendung}}
  - {{Transferfrage 2 zur realen Anwendung}}

Alternative_Handlungen:
  - {{Frage zu alternativen Vorgehensweisen}}

Abschlussprodukt: {{Erwartetes Format der Reflexion}}
[/DEBRIEF-BLOCK]
```

## Feld-Beschreibungen

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| DEBRIEF_ID | ✓ | Eindeutige ID im Format D_{Phase/Gesamt} |
| Zugehoerige_Phasen | ✓ | Liste der Phasen, auf die sich das Debriefing bezieht |
| Ziel | ✓ | Was soll durch die Reflexion erreicht werden? |
| Zeit | ○ | Zeitrahmen für das Debriefing |
| Beschreibung_Was | ✓ | Fragen zur konkreten Erfahrung |
| Analyse_Warum | ✓ | Fragen zu Ursachen und Entscheidungen |
| Abstraktion | ○ | Fragen zur Generalisierung |
| Transfer_Praxis | ✓ | Fragen zur realen Anwendung |
| Alternative_Handlungen | ○ | Fragen zu anderen Möglichkeiten |
| Abschlussprodukt | ✓ | Erwartetes Reflexionsformat |

## Reflexionsfragen-Typen

### Typ 1: Beschreibende Fragen (Was?)
Fokus auf die konkrete Erfahrung:
- "Was ist in Phase X passiert?"
- "Welche Entscheidung war am schwierigsten?"
- "Wo gab es Unsicherheiten?"

### Typ 2: Analytische Fragen (Warum?)
Fokus auf Ursachen und Zusammenhänge:
- "Warum hast du dich für X entschieden?"
- "Welche Informationen waren entscheidend?"
- "Welche Annahmen hast du getroffen?"

### Typ 3: Generalisierende Fragen (Was lernen wir?)
Fokus auf übertragbare Erkenntnisse:
- "Welche Regel/Prinzip steckt dahinter?"
- "Was würdest du beim nächsten Mal anders machen?"
- "Welche Strategie war besonders hilfreich?"

### Typ 4: Transferfragen (Wo noch?)
Fokus auf Anwendung in anderen Kontexten:
- "Wo in der Praxis ist das relevant?"
- "Welche Checkliste würdest du ableiten?"
- "In welchen anderen Situationen ist das nützlich?"

## Beispiel

```markdown
[DEBRIEF-BLOCK]
DEBRIEF_ID: D_GESAMT
Zugehoerige_Phasen: P0_BRIEF, P1_BEDARF, P2_BESTAND, P3_ANGEBOT
Ziel: Entscheidungen reflektieren, Fehlerquellen erkennen, Transfer in reale Einkaufs-/Küchenpraxis herstellen.
Zeit: 10-15 Minuten

Beschreibung_Was_ist_passiert:
  - "Welche Entscheidung war am schwierigsten und warum?"
  - "Wo gab es Unsicherheiten (Einheiten, Mengen, Lieferantenwahl)?"
  - "An welcher Stelle musstest du am meisten nachdenken?"

Analyse_Warum:
  - "Welche Daten/Tabellen waren entscheidend für deine Berechnung?"
  - "Welche Annahmen hast du getroffen (z.B. bei Getränkemengen)?"
  - "Was hat deine Lieferantenentscheidung beeinflusst?"

Abstraktion_Was_lernen_wir:
  - "Welche Strategie hat dir am meisten geholfen?"
  - "Was würdest du beim nächsten Mal von Anfang an anders machen?"

Transfer_Praxis:
  - "Welche Routine/Checkliste würdest du für echte Wareneinkäufe ableiten?"
  - "Wie würdest du in einem echten Hotel bei Zeitdruck vorgehen?"

Alternative_Handlungen:
  - "Welche andere Lieferantenentscheidung wäre vertretbar – unter welchen Bedingungen?"

Abschlussprodukt: 6-8 Sätze Reflexion + 3 Learnings als Bulletpoints
[/DEBRIEF-BLOCK]
```

## Debriefing-Ablauf im Chatbot

```markdown
**Reflexion & Transfer** [Debrief: D_GESAMT]

Du hast die Simulation erfolgreich durchlaufen! Jetzt ist es Zeit, das Gelernte zu sichern.

### Was ist passiert?
{{Reflexionsfrage 1}}

*Bitte antworte in 2-3 Sätzen, bevor wir zur nächsten Frage übergehen.*

---

Nach Beantwortung aller Fragen:

### Dein Abschluss
Fasse jetzt deine wichtigsten Erkenntnisse zusammen:
- 6-8 Sätze Reflexion
- 3 Learnings als Bulletpoints

**Diese Reflexion hilft dir, das Gelernte langfristig zu behalten und in der Praxis anzuwenden.**
```
