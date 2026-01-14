# 🚀 Quickstart: Lernbot-Framework

Willkommen! Diese Anleitung führt dich Schritt für Schritt durch die Erstellung deines ersten Lernassistenz-Bots.

---

## 📋 Übersicht

| Schritt | Was du tust | Zeitaufwand |
|---------|-------------|-------------|
| 1 | Material vorbereiten | 10-15 Min |
| 2 | Material analysieren | 15-30 Min |
| 3 | Scripts generieren | 30-60 Min |
| 4 | System-Prompt bauen | 10-20 Min |
| 5 | Qualität prüfen | 10-15 Min |
| **Gesamt** | | **~1,5-2,5 Std** |

---

## Schritt 1: Material vorbereiten

### Was du brauchst
- Unterrichtsmaterial (PDF, Word, Excel, MD, TXT)
- Klare Vorstellung der Lernziele
- 10-15 Minuten Zeit

### So gehst du vor

#### 1.1 Ordner erstellen
```
docs/Vorlagen/{{dein-projekt-name}}/
```

#### 1.2 Material ablegen
Lege alle relevanten Dateien in den Ordner:
- Aufgabenblätter
- Rezepte/Formeln/Tabellen
- Hintergrundinformationen
- Bewertungsbögen (falls vorhanden)

#### 1.3 Metadaten-Datei erstellen

Erstelle `_meta.yaml` im Projektordner:

```yaml
# === BOT-KONFIGURATION ===
bot:
  name: "{{Bot-Name, z.B. LernBuddy}}"
  tonalitaet: "freundlich"          # freundlich | formal | motivierend
  sprachniveau: "B1"                # B1 | B2 | C1
  standard_modus: "Schüler*innen-Modus"

# === KURS-INFORMATIONEN ===
kurs:
  fach: "{{Fachbereich}}"
  modul: "{{Modulname}}"
  zielgruppe: "{{z.B. Berufsschüler Gastronomie, 2. Lehrjahr}}"
  voraussetzungen: "{{Benötigtes Vorwissen}}"

# === ZEITRAHMEN ===
zeitrahmen:
  dauer_gesamt: "{{Minuten, z.B. 90}}"

# === MATERIAL-LISTE ===
materialien:
  - datei: "{{Dateiname.pdf}}"
    beschreibung: "{{Kurzbeschreibung}}"
```

#### 1.4 Lernziele definieren

Erstelle `_lernziele.md`:

```markdown
# Lernziele

## Hauptziel
{{Was sollen die Lernenden am Ende können?}}

## Teilziele
- [ ] {{Lernziel 1 - z.B. "Mengen für 50 Personen berechnen"}}
- [ ] {{Lernziel 2}}
- [ ] {{Lernziel 3}}
```

### ✅ Checkliste Schritt 1
- [ ] Ordner erstellt
- [ ] Material abgelegt
- [ ] `_meta.yaml` ausgefüllt
- [ ] `_lernziele.md` erstellt

---

## Schritt 2: Material analysieren

### Was passiert hier
Der **Material-Analyst** liest dein Material und extrahiert:
- Lernziele
- Aufgaben-Strukturen
- Ressourcen (Tabellen, Rezepte, etc.)
- Bewertungskriterien

### So gehst du vor

#### 2.1 Material-Analyst aufrufen

Kopiere diesen Prompt und füge dein Material ein:

```markdown
# Auftrag: Material-Analyse

Analysiere das folgende Unterrichtsmaterial und erstelle eine strukturierte Analyse.

## Metadaten
- Fach: {{aus _meta.yaml}}
- Zielgruppe: {{aus _meta.yaml}}
- Dauer: {{aus _meta.yaml}}

## Lernziele
{{aus _lernziele.md}}

## Material
{{Hier das Material einfügen oder Datei referenzieren}}

---

Erstelle die Analyse nach dem Schema:
1. Metadaten erfassen
2. Lernziele mit Bloom-Stufen verknüpfen
3. Aufgaben identifizieren (mit Typ und Schwierigkeit)
4. Ressourcen katalogisieren
5. Bewertungskriterien erkennen
6. Lücken dokumentieren

Verwende YAML-Blöcke für strukturierte Daten.
Markiere fehlende Informationen mit {{PLACEHOLDER}}.
```

#### 2.2 Analyse speichern

Speichere die Analyse als:
```
lernbot_framework/examples/{{projekt}}/01_material_analyse.md
```

### ✅ Checkliste Schritt 2
- [ ] Material-Analyst Prompt ausgeführt
- [ ] Analyse erhalten und gespeichert
- [ ] Lücken notiert (falls vorhanden)

---

## Schritt 3: Scripts generieren

### Was passiert hier
Der **Script-Generator** wandelt die Analyse in strukturierte Script-Blöcke um:
- META-Block
- PHASE-Blöcke
- TASK-Blöcke
- RUBRIC-Blöcke
- MODEL-Blöcke (optional)
- DEBRIEF-Block

### So gehst du vor

#### 3.1 Script-Generator aufrufen

```markdown
# Auftrag: Script-Generierung

Basierend auf der folgenden Material-Analyse, generiere alle Script-Blöcke.

## Material-Analyse
{{Hier die Analyse aus Schritt 2 einfügen}}

---

Generiere:
1. META-Block (Dokument-Metadaten)
2. PHASE-Blöcke (Ablauf-Phasen)
3. RESOURCE-Blöcke (Material-Referenzen)
4. TASK-Blöcke (Aufgaben mit Scaffolds)
5. RUBRIC-Blöcke (Bewertungskriterien)
6. MODEL-Blöcke (Musterlösungen, falls möglich)
7. DEBRIEF-Block (Reflexion)

Verwende die Block-Syntax: [BLOCK]...[/BLOCK]
Stelle sicher, dass alle IDs eindeutig und Referenzen gültig sind.
```

#### 3.2 Scripts prüfen

Prüfe die generierten Scripts auf:
- [ ] Alle Block-Typen vorhanden?
- [ ] IDs eindeutig?
- [ ] Referenzen stimmen?
- [ ] Keine `{{PLACEHOLDER}}` mehr (außer gewollt)?

#### 3.3 Scripts speichern

Speichere als:
```
lernbot_framework/examples/{{projekt}}/02_generierte_scripts.md
```

### ✅ Checkliste Schritt 3
- [ ] Script-Generator Prompt ausgeführt
- [ ] Alle Block-Typen generiert
- [ ] Scripts geprüft und gespeichert

---

## Schritt 4: System-Prompt bauen

### Was passiert hier
Der **Prompt-Builder** kombiniert alle Scripts zu einem finalen System-Prompt.

### So gehst du vor

#### 4.1 Prompt-Builder aufrufen

```markdown
# Auftrag: System-Prompt Assembly

Kombiniere die folgenden Scripts zu einem finalen System-Prompt.

## Bot-Konfiguration
- Name: {{aus _meta.yaml}}
- Tonalität: {{freundlich|formal|motivierend}}
- Sprachniveau: {{B1|B2|C1}}

## Generierte Scripts
{{Hier die Scripts aus Schritt 3 einfügen}}

---

Erstelle den finalen System-Prompt nach der Vorlage in:
`lernbot_framework/templates/scripts/system_prompt_base.md`

Der Output soll direkt kopierbar sein.
```

#### 4.2 System-Prompt speichern

Speichere als:
```
lernbot_framework/examples/{{projekt}}/03_system_prompt.md
```

### ✅ Checkliste Schritt 4
- [ ] Prompt-Builder Prompt ausgeführt
- [ ] System-Prompt erhalten
- [ ] Keine Platzhalter mehr vorhanden

---

## Schritt 5: Qualität prüfen

### Was passiert hier
Der **Quality-Checker** validiert den System-Prompt vor dem Einsatz.

### So gehst du vor

#### 5.1 Quality-Checker aufrufen

```markdown
# Auftrag: Quality-Check

Prüfe den folgenden System-Prompt auf Qualität und Konsistenz.

## System-Prompt
{{Hier den System-Prompt aus Schritt 4 einfügen}}

---

Prüfe:
1. Strukturelle Konsistenz (IDs, Referenzen, Block-Syntax)
2. Didaktische Qualität (Lernziele, Scaffolds, Feedback)
3. Inhaltliche Korrektheit (Fakten, Musterlösungen)
4. Technische Qualität (Formatierung, Token-Limit)

Erstelle einen Quality-Report mit Freigabe-Empfehlung.
```

#### 5.2 Fehler beheben (falls nötig)

Bei Fehlern:
- Kritische Fehler → Zurück zu Schritt 3
- Warnungen → Optional beheben

#### 5.3 Report speichern

```
lernbot_framework/examples/{{projekt}}/04_quality_report.md
```

### ✅ Checkliste Schritt 5
- [ ] Quality-Check durchgeführt
- [ ] Report erhalten
- [ ] Freigabe: ✅ FREIGEGEBEN

---

## 🎉 Fertig!

Dein Lernbot ist einsatzbereit!

### Nächste Schritte

1. **System-Prompt kopieren** in deine LLM-Plattform
2. **Testen** mit verschiedenen Schüler-Antworten
3. **Iterieren** basierend auf Feedback

### Tipps für den Einsatz

| Situation | Empfehlung |
|-----------|------------|
| Bot gibt zu schnell Lösungen | Scaffolds in TASK-Blöcken anpassen |
| Feedback zu hart/weich | Tonalität in System-Prompt ändern |
| Aufgaben zu schwer/leicht | Bloom-Stufen anpassen |
| Rubrik-Feedback ungenau | Kriterien in RUBRIC-Blöcken verfeinern |

---

## 📚 Weiterführende Dokumentation

- **Detaillierte Agenten-Beschreibungen**: `lernbot_framework/agents/`
- **Script-Templates**: `lernbot_framework/templates/scripts/`
- **Vollständiger Workflow**: `lernbot_framework/processes/bot_creation.md`
- **Intake-SOP**: `lernbot_framework/sops/material_intake.md`

---

## ❓ Häufige Fragen

### Wie lange dauert die Erstellung?
- Erstes Mal: 2-3 Stunden
- Mit Übung: 1-1,5 Stunden
- Bei ähnlichem Material: 30-60 Minuten

### Was, wenn Material fehlt?
Der Material-Analyst markiert Lücken mit `{{PLACEHOLDER}}`. Du kannst:
1. Material nachliefern
2. Platzhalter manuell ausfüllen
3. Scripts ohne diese Teile generieren

### Kann ich den Bot anpassen?
Ja! Ändere:
- Tonalität in `_meta.yaml`
- Scaffolds in TASK-Blöcken
- Kriterien in RUBRIC-Blöcken
- Reflexionsfragen in DEBRIEF-Block

### Wie teste ich den Bot?
1. Gib eine teilweise korrekte Antwort
2. Prüfe: Wird Feedback korrekt gegeben?
3. Frage nach Hints
4. Prüfe: Werden Scaffolds gestuft angeboten?
