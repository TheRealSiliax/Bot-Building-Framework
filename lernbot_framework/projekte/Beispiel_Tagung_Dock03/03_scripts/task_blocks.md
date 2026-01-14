# TASK-BLOCKS: Tagung im Hotel Dock 03

> **KORRIGIERT:** Aufgaben entsprechen jetzt dem Original-Unterrichtsmaterial

---

## T0_1: Ziel- und Auftragsklärung (Aufgabe 1)

```yaml
# ============================================
# TASK-BLOCK: T0_1_AUFTRAGSKLAERUNG
# ============================================
TASK_ID: "T0_1_AUFTRAGSKLAERUNG"
PHASE: "P0_BRIEF"
TASK_NAME: "Ziel- und Auftragsklärung"
TASK_TYP: "diskussion"
DAUER_MIN: 0

LERNZIELE:
  - "Die Handlungssituation verstehen"
  - "Das Ziel der Situation erkennen"
  - "Gemeinsam klären, was zu tun ist"

ORIENTIERUNGSFILTER: |
  Diese Aufgabe dient der Orientierung und Klärung der Situation.

AUFGABE: |
  **Handlungssituation**
  
  Die Firma „Love it? Save it!" hat in zwei Wochen im Hotel DOCK 03 einen 
  Veranstaltungsraum für eine große Tagung gebucht.
  
  Alle Abteilungen des Hotels DOCK 03 arbeiten unter Hochdruck an den 
  Vorbereitungen, um einen reibungslosen Ablauf zu garantieren.
  
  Für die Tagung ist ein Mittagslunch in Form eines 3-Gang-Menüs vorgesehen:
  - Möhrensuppe mit Croutons
  - Hamburger Pannfisch vom Kabeljau mit Blattspinat und Bratkartoffeln
  - Rote Grütze mit Vanilleeis
  
  Auch hier müssen entsprechende Vorbereitungen getroffen werden. 
  Vor allem müssen die benötigten Lebensmittel bestellt werden. 
  
  **Da der zuständige Koch länger erkrankt ist, seid ihr dafür zuständig.**

EINGABEAUFFORDERUNG: |
  📝 **Ziel- und Auftragsklärung:**
  
  Was ist nun zu tun und wie können wir die neue Situation bewältigen?

ABGABEFORMAT: "Freie Antwort / Diskussion"

# Nach 1. Lösungsversuch ausgeben
RESOURCES: ["R_TEXT_SITUATION"]
RUBRIK: "RB_T0_1"

SCAFFOLDS:
  HINT_1: "Überlege: Was muss alles organisiert werden?"
  HINT_2: "Welche Schritte sind nötig, um Lebensmittel zu bestellen?"
  HINT_3: "Was brauchen wir, bevor wir bestellen können?"

HINWEIS_NACH_ANTWORT: |
  Gut! Du hast die Situation verstanden. Jetzt geht es darum, den 
  konkreten Warenbedarf zu ermitteln. Dafür bekommst du gleich die Rezepte.
```

---

## T1_1: Warenanforderung ermitteln (Aufgabe 2)

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

# ============================================
# HIER WERDEN DIE REZEPTE FREIGEGEBEN!
# ============================================

REZEPT_FREIGABE: |
  📋 **Hier sind die Rezepte für das 3-Gang-Menü:**
  
  ---
  
  **🥕 Möhrensuppe mit Croutons**
  *(Rezept muss recherchiert werden)*
  
  💡 Tipp: Du kannst mich bitten, ein Rezept zu recherchieren!
  Sage: "Recherchiere ein Rezept für Möhrensuppe für 10 Personen"
  
  ---
  
  **🐟 Hamburger Pannfisch vom Kabeljau** (für 5 Personen)
  
  Zutaten:
  - 500g Kabeljaufilet
  - 600g Kartoffeln (festkochend)
  - 200g Blattspinat
  - 100g Speck
  - 2 Zwiebeln
  - 100g Butter
  - 200ml Sahne
  - Salz, Pfeffer, Muskat
  - Senf (körnig)
  
  ---
  
  **🍓 Hamburger Rote Grütze** (für 10 Personen)
  
  Zutaten:
  - 500g gemischte Beeren (Erdbeeren, Himbeeren, Johannisbeeren)
  - 200g Zucker
  - 500ml Wasser
  - 40g Speisestärke
  - 1 Päckchen Vanilleeis (pro Person 1 Kugel = 10 Kugeln)
  
  ---
  
  **🥤 Getränke** (Erfahrungswerte pro Person)
  - Wasser: 0,5L
  - Apfelsaft: 0,3L
  - Kaffee: 2 Tassen

AUFGABE: |
  **Warenanforderung feststellen**
  
  Im Folgenden sollst du den Warenbedarf (Lebensmittel und Getränke) für 
  die Tagung im Hotel Dock 03 ermitteln.
  
  **Die Tagung hat ca. 50 Personen.**
  
  **a) Ermittle die Warenanforderung der Tagung.**
  
  Berechne die benötigten Mengen für alle Zutaten, indem du die Rezepte 
  auf 50 Personen hochrechnest.

EINGABEAUFFORDERUNG: |
  📝 Gib jetzt deine berechnete Warenanforderung ein (als Liste oder Tabelle) 
  inkl. Einheiten.
  
  Wenn du für die Möhrensuppe ein Rezept recherchiert hast, nenne auch die Quelle.

ABGABEFORMAT: "Tabelle/Liste mit Einheiten + Quellenangabe Möhrensuppe"

# Nach 1. Lösungsversuch ausgeben
RESOURCES: ["R_REZEPT_PANNFISCH", "R_REZEPT_ROTEGRUETZE", "R_RECHERCHE_MOEHRENSUPPE"]
RUBRIK: "RB_T1_1"

SCAFFOLDS:
  HINT_1: "Skaliere die Rezepte: Pannfisch (5→50) = ×10, Grütze (10→50) = ×5"
  HINT_2: "Prüfe die Einheiten – verwende kg, g, Liter, Stück einheitlich"
  HINT_3: "Plausibilitätsprüfung: Sind die Portionsgrößen realistisch?"

RECHERCHE_ERLAUBT: true
```

---

## T2_1: Bestand abgleichen (Aufgabe 3)

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
RESOURCES: ["R_BESTANDSLISTE"]
RUBRIK: "RB_T2_1"

SCAFFOLDS:
  HINT_1: "Markiere zuerst alle Waren, die bereits im Bestand vorhanden sind"
  HINT_2: "Berechne: Bedarf - Bestand = zu bestellende Menge"
  HINT_3: "Runde sinnvoll auf Gebindegrößen (z.B. ganze Packungen, volle Liter)"
```

---

## T3_1: Angebote vergleichen (Aufgabe 4)

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
  
  **d) Recherchiere mögliche Handelspartner im Raum Hamburg.**
  
  **e) Vergleiche Angebote anhand der Kriterien.**
  
  **f) Entscheide dich für einen Lieferanten und begründe deine 
  Entscheidung anhand der Kriterien.**
  
  💡 Tipp: Du kannst mich bitten, Großhändler in Hamburg zu recherchieren!

EINGABEAUFFORDERUNG: |
  📝 Gib jetzt deinen Angebotsvergleich ein und formuliere deine 
  Lieferantenentscheidung mit Begründung.

ABGABEFORMAT: "Angebotsvergleich + Begründung"

# Nach 1. Lösungsversuch ausgeben
RESOURCES: ["R_WORKSHEET_ANGEBOT", "R_CRITERIA_LIEFERANT"]
RUBRIK: "RB_T3_1"

SCAFFOLDS:
  HINT_1: "Nutze Kriterien wie: Preis, Lieferzeit, Qualität, Mindestbestellwert"
  HINT_2: "Trenne harte Kriterien (muss erfüllt sein) von weichen (wäre gut)"
  HINT_3: "Belege deine Entscheidung mit konkreten Zahlen"

RECHERCHE_ERLAUBT: true
```
