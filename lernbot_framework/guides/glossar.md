# Glossar: Lernbot-Framework

Begriffsdefinitionen und Erklärungen für das Bot-Building Framework.

---

## A

### Agent
Ein spezialisierter KI-Akteur mit definiertem Aufgabenbereich. Im Framework gibt es vier Hauptagenten:
- **Material-Analyst**: Analysiert Unterrichtsmaterial
- **Script-Generator**: Generiert Script-Blöcke
- **Prompt-Builder**: Erstellt den System-Prompt
- **Quality-Checker**: Prüft die Qualität

### Assembly
Phase 4 im Workflow. Kombination aller generierten Scripts zu einem finalen System-Prompt.

---

## B

### Block
Ein abgeschlossener Inhaltsbereich im Script-System. Typen:
- META-Block: Metadaten
- PHASE-Block: Lernphasen
- RESOURCE-Block: Ressourcen
- TASK-Block: Aufgaben
- RUBRIC-Block: Bewertungskriterien
- MODEL-Block: Musterlösungen
- DEBRIEF-Block: Reflexion

### Bloom-Taxonomie
Hierarchisches System zur Klassifizierung von Lernzielen:
1. **Erinnern** (Remember)
2. **Verstehen** (Understand)
3. **Anwenden** (Apply)
4. **Analysieren** (Analyze)
5. **Bewerten** (Evaluate)
6. **Erschaffen** (Create)

---

## D

### Debriefing
Strukturierte Reflexionsphase nach Kolb:
1. Was ist passiert? (Konkrete Erfahrung)
2. Warum? (Reflexive Beobachtung)
3. Was lernen wir? (Abstrakte Begriffsbildung)
4. Transfer? (Aktives Experimentieren)

### DEBRIEF-Block
Script-Block für die Reflexionsphase mit Fragen und Transfer-Aufgaben.

---

## F

### Formatives Feedback
Feedback während des Lernprozesses zur Unterstützung (nicht zur Bewertung). Ziel: Lernenden helfen, sich zu verbessern.

---

## H

### Hint (Hinweis)
Gestufter Hinweis bei Schwierigkeiten:
1. Allgemeiner Hinweis
2. Konkreterer Hinweis
3. Scaffold (Gerüst)
4. Teil-Lösung
5. Musterlösung (nur wenn nötig)

---

## I

### Intake
Phase 1 im Workflow. Sammlung aller notwendigen Materialien und Metadaten.

---

## L

### Lernbot
Ein KI-gestützter Assistent für Lernende. Führt durch Aufgaben, gibt Feedback und unterstützt die Reflexion.

### Lernziel
Konkrete, messbare Beschreibung dessen, was Lernende können sollen. Formuliert mit aktivem Verb (z.B. "analysieren", "bewerten").

### LLM (Large Language Model)
Großes Sprachmodell wie GPT, Claude, Llama etc. Basis für den Lernbot.

---

## M

### META-Block
Script-Block mit Metadaten zur Lerneinheit (Titel, Dauer, Zielgruppe, Lernziele).

### MODEL-Block
Script-Block mit Musterlösungen zu Aufgaben. Wird nicht direkt gezeigt, sondern für Feedback verwendet.

### Model Answer
Siehe MODEL-Block. Beispielhafte Lösung einer Aufgabe.

---

## P

### PHASE-Block
Script-Block zur Definition einer Lernphase (Einführung, Hauptteil, Debriefing).

### Prompt
Anweisung an ein LLM. Der System-Prompt definiert das Verhalten des Bots.

---

## Q

### Quality-Checker
Agent zur Qualitätssicherung. Prüft Struktur, Didaktik, Inhalt und Technik.

---

## R

### RESOURCE-Block
Script-Block für Lernressourcen (Texte, Tabellen, Links).

### RUBRIC-Block
Script-Block mit Bewertungskriterien für Aufgaben.

### Rubric
Bewertungsraster mit Kriterien und Qualitätsstufen.

---

## S

### Scaffold (Gerüst)
Strukturierte Hilfestellung, die Lernenden den Einstieg erleichtert. Wird schrittweise reduziert.

### Script
Maschinenlesbares Dokument mit strukturierten Lerninhalt-Blöcken.

### Script-Generator
Agent zur Generierung von Script-Blöcken aus der Material-Analyse.

### SOP (Standard Operating Procedure)
Standardisierter Arbeitsablauf. Im Framework: Dokumentierte Prozesse für wiederkehrende Aufgaben.

### System-Prompt
Die zentrale Anweisung, die das Verhalten des Lernbots definiert. Enthält alle Scripts und Regeln.

---

## T

### TASK-Block
Script-Block zur Definition einer Lernaufgabe mit Kontext, Aufgabenstellung und Hinweisen.

### Template (Vorlage)
Vorgefertigte Struktur zum Ausfüllen. Im Framework: Script-Vorlagen für verschiedene Block-Typen.

### Tonalität
Kommunikationsstil des Bots (formal, freundlich, motivierend).

---

## V

### Validierung
Phase 5 im Workflow. Qualitätsprüfung vor dem Einsatz.

---

## W

### Workflow
Strukturierter Arbeitsablauf. Im Framework: Intake → Analyse → Generierung → Assembly → Validierung → Export → Test.

---

## Y

### YAML
Datenformat für strukturierte Informationen. Wird im Framework für Metadaten und Script-Blöcke verwendet.

---

## Abkürzungen

| Abkürzung | Bedeutung |
|-----------|-----------|
| LLM | Large Language Model |
| SOP | Standard Operating Procedure |
| DSGVO | Datenschutz-Grundverordnung |
| ID | Identifier (eindeutige Kennung) |
| KB | Knowledge Base |
| QA | Quality Assurance |
