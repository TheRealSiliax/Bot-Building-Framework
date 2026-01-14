# TASK-BLOCKS: Tagung im Hotel Dock 03

## T0_1: Auftragsklärung

```yaml
# ============================================
# TASK-BLOCK: T0_1_AUFTRAGSKLAERUNG
# ============================================
TASK_ID: "T0_1_AUFTRAGSKLAERUNG"
PHASE: "P0_BRIEF"
TASK_NAME: "Auftragsklärung"
TASK_TYP: "analyse"
DAUER_MIN: 0

LERNZIELE:
  - "Szenario und Auftrag korrekt zusammenfassen"
  - "Prioritäten setzen"
  - "Risiken erkennen"

ORIENTIERUNGSFILTER: |
  **Bewertungskriterien:**
  - C1: Ziele/Constraints erkannt
  - C2: To-Dos priorisiert
  - C3: Risiken + Maßnahmen genannt

AUFGABE: |
  **Situation**
  In einem Hotel ist eine Tagung von ca. 50 Personen geplant. Es gibt einen 
  3-Gänge-Lunch, der im Hotelküchenbereich produziert werden soll. Aufgrund 
  einer Krankmeldung ist der Küchenchef aber nicht verfügbar und du musst 
  kurzfristig die Aufgaben übernehmen.
  
  **Gesamtauftrag (Überblick)**
  1) Warenanforderung ermitteln (Speisen & Getränke)
  2) Bestand abgleichen und Bestellung bereinigen
  3) Angebote vergleichen, Lieferant wählen und Entscheidung begründen

EINGABEAUFFORDERUNG: |
  📝 Schreibe jetzt dein Kurzprotokoll (5–8 Sätze) und danach 
  3 Bulletpoints: Risiken/To-Dos in Reihenfolge.

ABGABEFORMAT: "Kurzprotokoll (5-8 Sätze) + 3 Bulletpoints"

# Nach 1. Lösungsversuch ausgeben
RESOURCES: ["R_TEXT_SITUATION", "R_BRIEF_VERANSTALTER", "R_TEXT_TASKS"]
RUBRIK: "RB_T0_1"

SCAFFOLDS:
  HINT_1: "Markiere im Auftrag alle Ziele und Einschränkungen (Constraints)"
  HINT_2: "Priorisiere die To-Dos nach Dringlichkeit – was muss zuerst erledigt werden?"
  HINT_3: "Nenne mindestens 2 Risiken und schlage je eine Gegenmaßnahme vor"
```

---

## T1_1: Warenanforderung ermitteln

```yaml
# ============================================
# TASK-BLOCK: T1_1_BEDARF
# ============================================
TASK_ID: "T1_1_BEDARF"
PHASE: "P1_BEDARF"
TASK_NAME: "Warenanforderung feststellen"
TASK_TYP: "berechnung"
DAUER_MIN: 0

LERNZIELE:
  - "Warenbedarf für 50 Personen korrekt ableiten (Skalierung)"
  - "Vollständigkeit sicherstellen"
  - "Korrekte Einheiten verwenden"
  - "Quelle für recherchiertes Rezept angeben"

ORIENTIERUNGSFILTER: |
  **Bewertungskriterien:**
  - C1: Skalierung korrekt
  - C2: Vollständigkeit
  - C3: Einheiten richtig
  - C4: Quelle Möhrensuppe angegeben

AUFGABE: |
  **Warenanforderung feststellen**
  
  Im Folgenden sollst du den Warenbedarf (Lebensmittel und Getränke) für die 
  Tagung im Hotel Dock 03 ermitteln.
  
  Für die Tagung sollen die folgenden Speisen angeboten werden:
  - **Möhrensuppe mit Croutons** (Rezept muss recherchiert werden)
  - **Hamburger Pannfisch** mit Blattspinat und Bratkartoffeln (Rezept für 5 Personen)
  - **Hamburger Rote Grütze** mit Vanilleeis (Rezept für 10 Personen)
  
  Getränke:
  - Wasser
  - Apfelsaft
  - Kaffee
  
  💡 **Tipp:** Du kannst mich bitten, ein Rezept für die Möhrensuppe zu 
  recherchieren! Sage einfach: *"Recherchiere ein Rezept für Möhrensuppe"*
  
  **a) Ermittle die Warenanforderung der Tagung und fülle die Tabelle aus.**

EINGABEAUFFORDERUNG: |
  📝 Gib jetzt deine berechnete Warenanforderung ein (als Liste oder Tabelle) 
  inkl. Einheiten und nenne deine Quelle für das Möhrensuppe-Rezept.

ABGABEFORMAT: "Tabelle/Liste mit Einheiten + Quellenangabe Möhrensuppe"

# Nach 1. Lösungsversuch ausgeben
RESOURCES: ["R_RECHERCHE_MOEHRENSUPPE", "R_REZEPT_PANNFISCH", "R_REZEPT_ROTEGRUETZE", "R_FUNC_SHEET"]
RUBRIK: "RB_T1_1"

SCAFFOLDS:
  HINT_1: "Skaliere die Rezepte auf 50 Personen: Pannfisch (5→50) = ×10, Grütze (10→50) = ×5"
  HINT_2: "Prüfe die Einheiten – verwende kg, g, Liter, Stück einheitlich"
  HINT_3: "Plausibilitätsprüfung: Sind die Portionsgrößen realistisch für eine Tagung?"

RECHERCHE_ERLAUBT: true
```

---

## T2_1: Bestand abgleichen

```yaml
# ============================================
# TASK-BLOCK: T2_1_BESTAND
# ============================================
TASK_ID: "T2_1_BESTAND"
PHASE: "P2_BESTAND"
TASK_NAME: "Bestand abgleichen"
TASK_TYP: "abgleich"
DAUER_MIN: 0

LERNZIELE:
  - "Bedarf und Bestand korrekt abgleichen"
  - "Bestellung logisch bereinigen"
  - "Änderungen dokumentieren"

ORIENTIERUNGSFILTER: |
  **Bewertungskriterien:**
  - C1: Korrekte Abzüge
  - C2: Plausibilität
  - C3: Dokumentation

AUFGABE: |
  **Bestand abgleichen**
  
  Nachdem du die Warenanforderung ermittelt hast, sollst du im Folgenden 
  noch den Bestand prüfen.
  
  **b) Prüfe den Bestand und gleiche ihn mit der ermittelten 
  Warenanforderung ab.**
  
  **c) Bereinige die Bestellung, indem du alle vorhandenen Waren aus der 
  Bestellung streichst oder Mengen anpasst.**

EINGABEAUFFORDERUNG: |
  📝 Gib jetzt deine bereinigte Bestellung ein (Liste/Tabelle) und erkläre 
  in 3–5 Sätzen deine wichtigsten Änderungen.

ABGABEFORMAT: "Bereinigte Bestellliste + Erklärung (3-5 Sätze)"

# Nach 1. Lösungsversuch ausgeben
RESOURCES: ["R_TEXT_TASKS"]
RUBRIK: "RB_T2_1"

SCAFFOLDS:
  HINT_1: "Markiere zuerst alle Waren, die bereits im Bestand vorhanden sind"
  HINT_2: "Berechne: Bedarf - Bestand = zu bestellende Menge"
  HINT_3: "Runde sinnvoll auf Gebindegrößen (z.B. ganze Packungen, volle Liter)"
```

---

## T3_1: Angebote vergleichen

```yaml
# ============================================
# TASK-BLOCK: T3_1_ANGEBOT
# ============================================
TASK_ID: "T3_1_ANGEBOT"
PHASE: "P3_ANGEBOT"
TASK_NAME: "Anfrage und Angebot"
TASK_TYP: "entscheidung"
DAUER_MIN: 0

LERNZIELE:
  - "Angebote systematisch vergleichen"
  - "Kriterien anwenden"
  - "Lieferant nachvollziehbar begründen"

ORIENTIERUNGSFILTER: |
  **Bewertungskriterien:**
  - C1: Kriterienanwendung
  - C2: Nachvollziehbarkeit
  - C3: Wirtschaftlichkeit
  - C4: Qualität/Risiko berücksichtigt

AUFGABE: |
  **Anfrage und Angebot**
  
  Da du die Bestellung bereinigt hast, sollst du nun einen passenden 
  Lieferanten finden.
  
  **d) Recherchiere mögliche Handelspartner im Raum Hamburg und trage 
  diese ein.**
  
  **e) Vergleiche Angebote anhand der Kriterien.**
  
  **f) Entscheide dich für einen Lieferanten und begründe deine 
  Entscheidung anhand der Kriterien.**
  
  💡 **Tipp:** Du kannst mich bitten, Informationen zu Großhändlern im 
  Raum Hamburg zu recherchieren!

EINGABEAUFFORDERUNG: |
  📝 Gib jetzt deinen Angebotsvergleich (oder die wichtigsten Zahlen/Infos) 
  ein und formuliere danach deine Lieferantenentscheidung in 8–12 Sätzen 
  mit Kriterienbezug.

ABGABEFORMAT: "Angebotsvergleich + Begründung (8-12 Sätze mit Kriterienbezug)"

# Nach 1. Lösungsversuch ausgeben
RESOURCES: ["R_WORKSHEET_ANGEBOT", "R_CRITERIA_LIEFERANT", "R_PARTNER_BRAINSTORM"]
RUBRIK: "RB_T3_1"

SCAFFOLDS:
  HINT_1: "Nutze die Kriterienliste systematisch – gehe Punkt für Punkt durch"
  HINT_2: "Trenne harte Kriterien (Preis, Lieferzeit) von weichen (Qualität, Service)"
  HINT_3: "Belege deine Entscheidung mit 2-3 konkreten Zahlen aus der Vergleichstabelle"

RECHERCHE_ERLAUBT: true
```
