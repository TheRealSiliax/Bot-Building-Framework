# PHASE-BLOCKS: Tagung im Hotel Dock 03

## P0: Briefing / Startlayout

```yaml
# ============================================
# PHASE-BLOCK: P0_BRIEF
# ============================================
PHASE_ID: "P0_BRIEF"
PHASE_NAME: "Briefing / Startlayout"
PHASE_TYP: "einfuehrung"
DAUER_MIN: 0
POSITION: 1

BESCHREIBUNG: |
  Szenario verstehen, Ziele klären, Gesamtauftrag erfassen.
  Dies ist die Startphase mit vollständigem Überblick.

LERNZIELE_PHASE:
  - "Szenario und Auftrag korrekt zusammenfassen"
  - "Prioritäten setzen"
  - "Risiken erkennen"

STARTLAYOUT: |
  ## 🏨 Willkommen bei SIMcoach!
  
  **Deine Situation:**
  In einem Hotel ist eine Tagung von ca. 50 Personen geplant. Es gibt einen 
  3-Gänge-Lunch, der im Hotelküchenbereich produziert werden soll. Aufgrund 
  einer Krankmeldung ist der Küchenchef nicht verfügbar – du musst kurzfristig 
  die Aufgaben übernehmen!
  
  **Dein Gesamtauftrag:**
  1. Warenanforderung ermitteln (Speisen & Getränke)
  2. Bestand abgleichen und Bestellung bereinigen
  3. Angebote vergleichen, Lieferant wählen und begründen
  
  **So läuft's ab:**
  Phase 1 → Bedarf ermitteln
  Phase 2 → Bestand abgleichen
  Phase 3 → Angebote vergleichen
  Phase 4 → Reflexion
  
  💡 **Tipp:** Du kannst mich jederzeit bitten, Informationen zu recherchieren!

TASKS_PHASE:
  - "T0_1_AUFTRAGSKLAERUNG"

UEBERGANG_ZU:
  naechste_phase: "P1_BEDARF"
  bedingung: "Wenn T0_1 abgeschlossen"
  hinweis: "Super! Du hast den Auftrag verstanden. Weiter zur Bedarfsermittlung!"
```

---

## P1: Bedarf ermitteln

```yaml
# ============================================
# PHASE-BLOCK: P1_BEDARF
# ============================================
PHASE_ID: "P1_BEDARF"
PHASE_NAME: "Bedarf ermitteln"
PHASE_TYP: "hauptteil"
DAUER_MIN: 0
POSITION: 2

BESCHREIBUNG: |
  Rezepte analysieren und Warenbedarf für 50 Personen berechnen.
  Skalierung der Rezepte ist der Kern dieser Phase.

LERNZIELE_PHASE:
  - "Warenbedarf für 50 Personen korrekt ableiten"
  - "Skalierung durchführen"
  - "Vollständigkeit sicherstellen"

TASKS_PHASE:
  - "T1_1_BEDARF"

RECHERCHE_HINWEIS: |
  💡 Du kannst mich bitten, ein Rezept für die Möhrensuppe zu recherchieren!
  Sage einfach: "Recherchiere ein Rezept für Möhrensuppe für 10 Personen"

UEBERGANG_ZU:
  naechste_phase: "P2_BESTAND"
  bedingung: "Wenn Warenanforderung vollständig"
  hinweis: "Gut gemacht! Jetzt prüfen wir, was schon im Lager ist."
```

---

## P2: Bestand abgleichen

```yaml
# ============================================
# PHASE-BLOCK: P2_BESTAND
# ============================================
PHASE_ID: "P2_BESTAND"
PHASE_NAME: "Bestand abgleichen & Bestellung bereinigen"
PHASE_TYP: "hauptteil"
DAUER_MIN: 0
POSITION: 3

BESCHREIBUNG: |
  Lagerbestand prüfen, Bestellung korrigieren und bereinigen.
  Differenz zwischen Bedarf und Bestand ermitteln.

LERNZIELE_PHASE:
  - "Bedarf und Bestand korrekt abgleichen"
  - "Bestellung logisch bereinigen"
  - "Änderungen dokumentieren"

TASKS_PHASE:
  - "T2_1_BESTAND"

UEBERGANG_ZU:
  naechste_phase: "P3_ANGEBOT"
  bedingung: "Wenn Bestellung bereinigt"
  hinweis: "Perfekt! Jetzt suchen wir den passenden Lieferanten."
```

---

## P3: Angebote vergleichen

```yaml
# ============================================
# PHASE-BLOCK: P3_ANGEBOT
# ============================================
PHASE_ID: "P3_ANGEBOT"
PHASE_NAME: "Angebote vergleichen & Lieferant auswählen"
PHASE_TYP: "hauptteil"
DAUER_MIN: 0
POSITION: 4

BESCHREIBUNG: |
  Kriterien anwenden, Angebote vergleichen, Entscheidung begründen.
  Dies ist die komplexeste Phase mit Entscheidungsfindung.

LERNZIELE_PHASE:
  - "Angebote systematisch vergleichen"
  - "Kriterien anwenden"
  - "Lieferant nachvollziehbar begründen"

TASKS_PHASE:
  - "T3_1_ANGEBOT"

RECHERCHE_HINWEIS: |
  💡 Du kannst mich bitten, Großhändler im Raum Hamburg zu recherchieren!

UEBERGANG_ZU:
  naechste_phase: "P4_DEBRIEF"
  bedingung: "Wenn Lieferantenentscheidung begründet"
  hinweis: "Sehr gut! Lass uns jetzt reflektieren, was du gelernt hast."
```

---

## P4: Debriefing

```yaml
# ============================================
# PHASE-BLOCK: P4_DEBRIEF
# ============================================
PHASE_ID: "P4_DEBRIEF"
PHASE_NAME: "Debriefing / Reflexion & Transfer"
PHASE_TYP: "debriefing"
DAUER_MIN: 0
POSITION: 5

BESCHREIBUNG: |
  Strukturierte Reflexion der Lernerfahrung.
  Transfer des Gelernten auf reale Situationen.

LERNZIELE_PHASE:
  - "Eigene Entscheidungen reflektieren"
  - "Fehlerquellen erkennen"
  - "Transfer in die Berufspraxis herstellen"

TASKS_PHASE: []  # Debriefing-Block wird separat gesteuert

UEBERGANG_ZU:
  naechste_phase: null
  bedingung: "Wenn alle Reflexionsfragen beantwortet"
  hinweis: "Vielen Dank! Du hast die Simulation erfolgreich abgeschlossen. 🎉"
```
