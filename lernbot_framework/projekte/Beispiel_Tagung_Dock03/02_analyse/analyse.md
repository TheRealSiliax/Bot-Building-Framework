# Material-Analyse: Tagung im Hotel Dock 03

**Projekt:** Beispiel_Tagung_Dock03
**Erstellt:** 2026-01-14
**Status:** Analyse abgeschlossen

---

## 1. Metadaten

```yaml
simulation_id: "SIM_TAGUNG_DOCK03_2026_01"
titel: "Tagung im Hotel Dock 03"
version: "v1.1 (kompakt)"
thema: "Warenwirtschaft und Lieferantenmanagement"
zielgruppe: "Berufsschüler*innen Gastronomie/Hotelwesen, 2. Lehrjahr"
voraussetzungen: "Grundkenntnisse Rezeptberechnung, Tabellenkalkulation"
dauer_gesamt: 0  # Wird dynamisch angepasst
anzahl_phasen: 5
anzahl_aufgaben: 4
```

---

## 2. Bot-Konfiguration

```yaml
bot_name: "SIMcoach"
tonalitaet: "freundlich"
sprachniveau: "B1"
standard_modus: "Schüler*innen-Modus"

# WICHTIG: Recherche-Funktion
recherche_hinweis: |
  💡 **Hinweis zur Rezeptrecherche:**
  Du kannst mich bitten, Rezepte im Internet zu recherchieren!
  Sage einfach: "Recherchiere ein Rezept für Möhrensuppe für 10 Personen"
  Ich habe Internetzugang und kann dir bei der Recherche helfen.

internet_zugang: true
recherche_erlaubt: true
```

---

## 3. Lernziele

```yaml
lernziele:
  hauptziel: "Die Lernenden können eigenständig einen Wareneinkauf für eine Veranstaltung planen, durchführen und begründen."
  
  teilziele:
    - id: "LZ1"
      beschreibung: "Szenario und Auftrag korrekt zusammenfassen"
      bloom_stufe: 2  # Verstehen
      phase: "P0_BRIEF"
      
    - id: "LZ2"
      beschreibung: "Prioritäten setzen und Risiken erkennen"
      bloom_stufe: 4  # Analysieren
      phase: "P0_BRIEF"
      
    - id: "LZ3"
      beschreibung: "Warenbedarf für 50 Personen korrekt berechnen (Skalierung)"
      bloom_stufe: 3  # Anwenden
      phase: "P1_BEDARF"
      
    - id: "LZ4"
      beschreibung: "Lagerbestand prüfen und Bestellung bereinigen"
      bloom_stufe: 3  # Anwenden
      phase: "P2_BESTAND"
      
    - id: "LZ5"
      beschreibung: "Angebote systematisch vergleichen"
      bloom_stufe: 4  # Analysieren
      phase: "P3_ANGEBOT"
      
    - id: "LZ6"
      beschreibung: "Lieferantenentscheidung nachvollziehbar begründen"
      bloom_stufe: 5  # Bewerten
      phase: "P3_ANGEBOT"
      
    - id: "LZ7"
      beschreibung: "Entscheidungen reflektieren und auf Praxis transferieren"
      bloom_stufe: 5  # Bewerten
      phase: "P4_DEBRIEF"
```

---

## 4. Phasen

```yaml
phasen:
  - id: "P0_BRIEF"
    name: "Briefing / Startlayout"
    typ: "einfuehrung"
    dauer_min: 0
    position: 1
    beschreibung: "Szenario verstehen, Ziele klären, Regeln, Gesamtauftrag"
    tasks: ["T0_1_AUFTRAGSKLAERUNG"]
    uebergang_zu: "P1_BEDARF"
    bedingung: "Wenn T0_1 abgeschlossen"
    
  - id: "P1_BEDARF"
    name: "Bedarf ermitteln"
    typ: "hauptteil"
    dauer_min: 0
    position: 2
    beschreibung: "Rezepte/Speisenplan → Warenbedarf für 50 Personen"
    tasks: ["T1_1_BEDARF"]
    uebergang_zu: "P2_BESTAND"
    bedingung: "Wenn Warenanforderung vollständig"
    hinweis_recherche: "Schüler*innen können den Bot bitten, Rezepte zu recherchieren"
    
  - id: "P2_BESTAND"
    name: "Bestand abgleichen & Bestellung bereinigen"
    typ: "hauptteil"
    dauer_min: 0
    position: 3
    beschreibung: "Lagerbestand prüfen, Bestellung korrigieren"
    tasks: ["T2_1_BESTAND"]
    uebergang_zu: "P3_ANGEBOT"
    bedingung: "Wenn Bestellung bereinigt"
    
  - id: "P3_ANGEBOT"
    name: "Angebote vergleichen & Lieferant auswählen"
    typ: "hauptteil"
    dauer_min: 0
    position: 4
    beschreibung: "Kriterien anwenden, Entscheidung begründen"
    tasks: ["T3_1_ANGEBOT"]
    uebergang_zu: "P4_DEBRIEF"
    bedingung: "Wenn Lieferantenentscheidung begründet"
    
  - id: "P4_DEBRIEF"
    name: "Debriefing / Reflexion & Transfer"
    typ: "debriefing"
    dauer_min: 0
    position: 5
    beschreibung: "Lernen sichern, Transfer herstellen"
    tasks: []
    uebergang_zu: null
    bedingung: "Ende der Simulation"
```

---

## 5. Aufgaben (Tasks)

### T0_1: Auftragsklärung

```yaml
task_id: "T0_1_AUFTRAGSKLAERUNG"
phase: "P0_BRIEF"
titel: "Auftragsklärung"
typ: "analyse"
dauer_min: 0

lernziele:
  - "Szenario und Auftrag korrekt zusammenfassen"
  - "Prioritäten setzen"
  - "Risiken erkennen"

aufgabenstellung: |
  **Situation**
  In einem Hotel ist eine Tagung von ca. 50 Personen geplant. Es gibt einen 
  3-Gänge-Lunch, der im Hotelküchenbereich produziert werden soll. Aufgrund 
  einer Krankmeldung ist der Küchenchef aber nicht verfügbar und du musst 
  kurzfristig die Aufgaben übernehmen.
  
  **Gesamtauftrag (Überblick)**
  1) Warenanforderung ermitteln (Speisen & Getränke)
  2) Bestand abgleichen und Bestellung bereinigen
  3) Angebote vergleichen, Lieferant wählen und Entscheidung begründen

eingabeaufforderung: |
  Schreibe jetzt dein Kurzprotokoll (5–8 Sätze) und danach 3 Bulletpoints: 
  Risiken/To-Dos in Reihenfolge.

abgabeformat: "Kurzprotokoll + 3 Bulletpoints"

rubrik: "RB_T0_1"
resources: ["R_TEXT_SITUATION", "R_BRIEF_VERANSTALTER", "R_TEXT_TASKS"]

scaffolds:
  - hint1: "Markiere Ziele und Constraints im Auftrag"
  - hint2: "Priorisiere die To-Dos nach Dringlichkeit"
  - hint3: "Nenne 2 Risiken und mögliche Gegenmaßnahmen"
```

### T1_1: Warenanforderung ermitteln

```yaml
task_id: "T1_1_BEDARF"
phase: "P1_BEDARF"
titel: "Warenanforderung feststellen"
typ: "berechnung"
dauer_min: 0

lernziele:
  - "Warenbedarf für 50 Personen korrekt ableiten"
  - "Skalierung durchführen"
  - "Vollständigkeit sicherstellen"
  - "Korrekte Einheiten verwenden"

aufgabenstellung: |
  Im Folgenden sollst du den Warenbedarf (Lebensmittel und Getränke) für die 
  Tagung im Hotel Dock 03 ermitteln.
  
  Für die Tagung sollen die folgenden Speisen angeboten werden:
  - Möhrensuppe mit Croutons (Rezept muss recherchiert werden)
  - Hamburger Pannfisch mit Blattspinat und Bratkartoffeln (Rezept für 5 Personen)
  - Hamburger Rote Grütze mit Vanilleeis (Rezept für 10 Personen)
  
  Getränke:
  - Wasser
  - Apfelsaft
  - Kaffee
  
  **💡 Tipp:** Du kannst mich bitten, ein Rezept für die Möhrensuppe zu 
  recherchieren! Sage einfach: "Recherchiere ein Rezept für Möhrensuppe"

eingabeaufforderung: |
  Gib jetzt deine berechnete Warenanforderung ein (als Liste oder Tabelle) 
  inkl. Einheiten und nenne deine Quelle für das Möhrensuppe-Rezept.

abgabeformat: "Tabelle mit Einheiten + Quellenangabe"

rubrik: "RB_T1_1"
resources: ["R_RECHERCHE_MOEHRENSUPPE", "R_REZEPT_PANNFISCH", "R_REZEPT_ROTEGRUETZE", "R_FUNC_SHEET"]

scaffolds:
  - hint1: "Skaliere die Rezepte auf 50 Personen (Pannfisch ×10, Grütze ×5)"
  - hint2: "Prüfe die Einheiten (kg, g, Liter, Stück)"
  - hint3: "Plausibilitätsprüfung: Sind die Portionen realistisch?"

recherche_erlaubt: true
recherche_beispiel: "Recherchiere ein Rezept für Möhrensuppe mit Croutons für 10 Personen"
```

### T2_1: Bestand abgleichen

```yaml
task_id: "T2_1_BESTAND"
phase: "P2_BESTAND"
titel: "Bestand abgleichen"
typ: "abgleich"
dauer_min: 0

lernziele:
  - "Bedarf und Bestand korrekt abgleichen"
  - "Bestellung logisch bereinigen"
  - "Änderungen dokumentieren"

aufgabenstellung: |
  Nachdem du die Warenanforderung ermittelt hast, sollst du im Folgenden 
  noch den Bestand prüfen.
  
  b) Prüfe den Bestand und gleiche ihn mit der ermittelten Warenanforderung ab.
  c) Bereinige die Bestellung, indem du alle vorhandenen Waren aus der 
     Bestellung streichst oder Mengen anpasst.

eingabeaufforderung: |
  Gib jetzt deine bereinigte Bestellung ein (Liste/Tabelle) und erkläre in 
  3–5 Sätzen deine wichtigsten Änderungen.

abgabeformat: "Bereinigte Bestellliste + Erklärung (3-5 Sätze)"

rubrik: "RB_T2_1"
resources: ["R_TEXT_TASKS"]

scaffolds:
  - hint1: "Markiere zuerst alle Waren, die im Bestand vorhanden sind"
  - hint2: "Berechne: Bedarf - Bestand = zu bestellende Menge"
  - hint3: "Runde sinnvoll auf Gebindegrößen (z.B. ganze Packungen)"
```

### T3_1: Angebote vergleichen

```yaml
task_id: "T3_1_ANGEBOT"
phase: "P3_ANGEBOT"
titel: "Anfrage und Angebot"
typ: "entscheidung"
dauer_min: 0

lernziele:
  - "Angebote systematisch vergleichen"
  - "Kriterien anwenden"
  - "Lieferant nachvollziehbar begründen"

aufgabenstellung: |
  Da du die Bestellung bereinigt hast, sollst du nun einen passenden 
  Lieferanten finden.
  
  d) Recherchiere mögliche Handelspartner im Raum Hamburg und trage diese ein.
  e) Vergleiche Angebote anhand der Kriterien.
  f) Entscheide dich für einen Lieferanten und begründe deine Entscheidung 
     anhand der Kriterien.
  
  **💡 Tipp:** Du kannst mich bitten, Informationen zu Großhändlern im Raum 
  Hamburg zu recherchieren!

eingabeaufforderung: |
  Gib jetzt deinen Angebotsvergleich (oder die wichtigsten Zahlen/Infos) ein 
  und formuliere danach deine Lieferantenentscheidung in 8–12 Sätzen mit 
  Kriterienbezug.

abgabeformat: "Angebotsvergleich + Begründung (8-12 Sätze)"

rubrik: "RB_T3_1"
resources: ["R_WORKSHEET_ANGEBOT", "R_CRITERIA_LIEFERANT", "R_PARTNER_BRAINSTORM"]

scaffolds:
  - hint1: "Nutze die Kriterienliste systematisch"
  - hint2: "Trenne harte Kriterien (Preis, Lieferzeit) von weichen (Qualität, Service)"
  - hint3: "Belege deine Entscheidung mit 2-3 konkreten Zahlen aus der Tabelle"

recherche_erlaubt: true
recherche_beispiel: "Recherchiere Großhändler für Lebensmittel im Raum Hamburg"
```

---

## 6. Ressourcen

```yaml
resources:
  - id: "R_TEXT_SITUATION"
    typ: "input"
    titel: "Situationsbeschreibung (Zeitdruck durch Krankheitsausfall)"
    verwendung: ["T0_1_AUFTRAGSKLAERUNG"]
    
  - id: "R_BRIEF_VERANSTALTER"
    typ: "input"
    titel: "Veranstalter-Infos / Eckdaten Tagung"
    verwendung: ["T0_1_AUFTRAGSKLAERUNG"]
    
  - id: "R_RECHERCHE_MOEHRENSUPPE"
    typ: "aufgabe"
    titel: "Möhrensuppe – Rezept muss recherchiert werden"
    verwendung: ["T1_1_BEDARF"]
    hinweis: "Schüler*innen können den Bot bitten, ein Rezept zu recherchieren"
    
  - id: "R_REZEPT_PANNFISCH"
    typ: "rezept"
    titel: "Hamburger Pannfisch (für 5 Personen)"
    verwendung: ["T1_1_BEDARF"]
    skalierung: "×10 für 50 Personen"
    
  - id: "R_REZEPT_ROTEGRUETZE"
    typ: "rezept"
    titel: "Hamburger Rote Grütze (für 10 Personen)"
    verwendung: ["T1_1_BEDARF"]
    skalierung: "×5 für 50 Personen"
    
  - id: "R_FUNC_SHEET"
    typ: "worksheet"
    titel: "Function Sheet / Warengruppen-Überblick"
    verwendung: ["T1_1_BEDARF"]
    
  - id: "R_WORKSHEET_ANGEBOT"
    typ: "worksheet"
    titel: "Angebotsvergleich (Preis, Transportkosten, Rabatte)"
    verwendung: ["T3_1_ANGEBOT"]
    
  - id: "R_CRITERIA_LIEFERANT"
    typ: "input"
    titel: "Kriterien zur Lieferantenentscheidung"
    verwendung: ["T3_1_ANGEBOT"]
```

---

## 7. Bewertungsrubriken

### RB_T0_1: Auftragsklärung

```yaml
rubrik_id: "RB_T0_1"
gilt_fuer: "T0_1_AUFTRAGSKLAERUNG"
skala: "0-2"

kriterien:
  - id: "C1_Ziele_Constraints"
    beschreibung: "Ziele und Einschränkungen des Auftrags erkannt"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
    
  - id: "C2_Priorisierung"
    beschreibung: "To-Dos sinnvoll priorisiert"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
    
  - id: "C3_Risiken_Massnahmen"
    beschreibung: "Risiken erkannt und Gegenmaßnahmen genannt"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
```

### RB_T1_1: Warenanforderung

```yaml
rubrik_id: "RB_T1_1"
gilt_fuer: "T1_1_BEDARF"
skala: "0-2"

kriterien:
  - id: "C1_Skalierung"
    beschreibung: "Rezepte korrekt auf 50 Personen skaliert"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
    
  - id: "C2_Vollstaendigkeit"
    beschreibung: "Alle notwendigen Zutaten aufgeführt"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
    
  - id: "C3_Einheiten"
    beschreibung: "Korrekte und einheitliche Einheiten verwendet"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
    
  - id: "C4_Quelle_Moehrensuppe"
    beschreibung: "Quelle für Möhrensuppe-Rezept angegeben"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
```

### RB_T2_1: Bestandsabgleich

```yaml
rubrik_id: "RB_T2_1"
gilt_fuer: "T2_1_BESTAND"
skala: "0-2"

kriterien:
  - id: "C1_Korrekte_Abzuege"
    beschreibung: "Bestand korrekt vom Bedarf abgezogen"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
    
  - id: "C2_Plausibilitaet"
    beschreibung: "Bestellmengen sind plausibel"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
    
  - id: "C3_Dokumentation"
    beschreibung: "Änderungen nachvollziehbar dokumentiert"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
```

### RB_T3_1: Angebotsvergleich

```yaml
rubrik_id: "RB_T3_1"
gilt_fuer: "T3_1_ANGEBOT"
skala: "0-2"

kriterien:
  - id: "C1_Kriterienanwendung"
    beschreibung: "Kriterien systematisch angewendet"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
    
  - id: "C2_Nachvollziehbarkeit"
    beschreibung: "Entscheidung nachvollziehbar begründet"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
    
  - id: "C3_Wirtschaftlichkeit"
    beschreibung: "Wirtschaftliche Aspekte berücksichtigt"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
    
  - id: "C4_Qualitaet_Risiko"
    beschreibung: "Qualität und Risiken berücksichtigt"
    level_0: "{{Beschreibung Level 0 - AUSFÜLLEN}}"
    level_1: "{{Beschreibung Level 1 - AUSFÜLLEN}}"
    level_2: "{{Beschreibung Level 2 - AUSFÜLLEN}}"
    ankerbeispiel: "{{optional}}"
```

---

## 8. Debriefing

```yaml
debrief_id: "D_P4"
zugehoerige_phasen: ["P0_BRIEF", "P1_BEDARF", "P2_BESTAND", "P3_ANGEBOT"]
ziel: "Entscheidungen reflektieren, Fehlerquellen erkennen, Transfer herstellen"

fragen:
  beschreibung:
    - "Welche Entscheidung war am schwierigsten und warum?"
    - "Wo gab es Unsicherheiten (Einheiten, Mengen, Lieferantenwahl)?"
    
  analyse:
    - "Welche Daten/Tabellen waren entscheidend?"
    - "Welche Annahmen habt ihr getroffen?"
    
  transfer:
    - "Welche Routine/Checkliste würdet ihr für echte Wareneinkäufe ableiten?"
    
  alternativen:
    - "Welche andere Lieferantenentscheidung wäre vertretbar – unter welchen Bedingungen?"

abschlussprodukt: "6–8 Sätze Reflexion + 3 Learnings (Bulletpoints)"
```

---

## 9. Bot-Hinweise (für System-Prompt)

```yaml
bot_hinweise:
  recherche:
    aktiviert: true
    hinweistext: |
      💡 **Hinweis:** Du kannst mich bitten, Informationen im Internet zu 
      recherchieren! Zum Beispiel:
      - "Recherchiere ein Rezept für Möhrensuppe"
      - "Suche Großhändler für Lebensmittel in Hamburg"
    
  bei_aufgaben_mit_recherche:
    - task_id: "T1_1_BEDARF"
      hinweis: "Du kannst den Bot bitten, das Möhrensuppe-Rezept zu recherchieren"
    - task_id: "T3_1_ANGEBOT"
      hinweis: "Du kannst den Bot bitten, Lieferanten in Hamburg zu recherchieren"
```

---

## 10. Offene Punkte (Rubrik-Details)

⚠️ **Noch auszufüllen:**

Die Rubrik-Level-Beschreibungen müssen noch ergänzt werden. 
Für jedes Kriterium benötige ich:

1. **Level 0** - Was bedeutet "nicht erfüllt"?
2. **Level 1** - Was bedeutet "teilweise erfüllt"?
3. **Level 2** - Was bedeutet "vollständig erfüllt"?

**Beispiel zur Orientierung:**

```yaml
# Kriterium C1_Skalierung
level_0: "Keine Skalierung durchgeführt oder komplett falsche Berechnung"
level_1: "Skalierungsfaktor erkannt, aber Rechenfehler bei einzelnen Zutaten"
level_2: "Alle Zutaten korrekt mit richtigem Faktor hochgerechnet"
```

---

**Analyse-Status:** ✅ Abgeschlossen (Rubrik-Details offen)
**Nächster Schritt:** Rubrik-Details ergänzen oder direkt zu Script-Generierung
