# RUBRIC-BLOCKS: Tagung im Hotel Dock 03

> **Hinweis:** Rubrik-Details werden für Feedback nach dem 1. Lösungsversuch genutzt.
> Die Level-Beschreibungen sind generisch gehalten und können angepasst werden.

## RB_T0_1: Auftragsklärung

```yaml
# ============================================
# RUBRIC-BLOCK: RB_T0_1
# ============================================
RUBRIC_ID: "RB_T0_1"
GILT_FUER: "T0_1_AUFTRAGSKLAERUNG"
SKALA: "0-2"
HINWEISE_BEWERTUNG: "Kriteriumsbezogen, mit Belegen aus der Schülerantwort. Kurz und konstruktiv."

KRITERIEN:
  - KRITERIUM_ID: "C1_Ziele_Constraints"
    KRITERIUM: "Ziele und Einschränkungen des Auftrags erkannt"
    LEVEL_0: "Ziele/Constraints nicht oder falsch erkannt"
    LEVEL_1: "Teilweise erkannt, aber unvollständig oder unpräzise"
    LEVEL_2: "Alle wesentlichen Ziele und Constraints korrekt benannt"
    ANKERBEISPIEL: "Korrekt: 50 Personen, 3-Gänge-Lunch, Zeitdruck durch Krankheitsausfall"

  - KRITERIUM_ID: "C2_Priorisierung"
    KRITERIUM: "To-Dos sinnvoll priorisiert"
    LEVEL_0: "Keine Priorisierung oder komplett unlogische Reihenfolge"
    LEVEL_1: "Priorisierung erkennbar, aber nicht optimal begründet"
    LEVEL_2: "Logische Priorisierung mit nachvollziehbarer Begründung"
    ANKERBEISPIEL: "Korrekt: 1. Bedarf ermitteln, 2. Bestand prüfen, 3. Lieferant wählen"

  - KRITERIUM_ID: "C3_Risiken_Massnahmen"
    KRITERIUM: "Risiken erkannt und Gegenmaßnahmen genannt"
    LEVEL_0: "Keine Risiken genannt oder keine Maßnahmen"
    LEVEL_1: "1 Risiko mit Maßnahme oder mehrere ohne Maßnahmen"
    LEVEL_2: "Mindestens 2 Risiken mit passenden Gegenmaßnahmen"
    ANKERBEISPIEL: "Risiko: Zeitknappheit → Maßnahme: Prioritäten setzen, Kollegen einbinden"
```

---

## RB_T1_1: Warenanforderung

```yaml
# ============================================
# RUBRIC-BLOCK: RB_T1_1
# ============================================
RUBRIC_ID: "RB_T1_1"
GILT_FUER: "T1_1_BEDARF"
SKALA: "0-2"
HINWEISE_BEWERTUNG: "Kriteriumsbezogen, mit Belegen aus der Schülerantwort. Kurz und konstruktiv."

KRITERIEN:
  - KRITERIUM_ID: "C1_Skalierung"
    KRITERIUM: "Rezepte korrekt auf 50 Personen skaliert"
    LEVEL_0: "Keine Skalierung oder komplett falsche Berechnung"
    LEVEL_1: "Skalierungsfaktor erkannt, aber Rechenfehler bei einzelnen Zutaten"
    LEVEL_2: "Alle Zutaten korrekt mit richtigem Faktor hochgerechnet"
    ANKERBEISPIEL: "Pannfisch (5 Pers.) ×10 = 50 Pers., Grütze (10 Pers.) ×5 = 50 Pers."

  - KRITERIUM_ID: "C2_Vollstaendigkeit"
    KRITERIUM: "Alle notwendigen Zutaten aufgeführt"
    LEVEL_0: "Weniger als 50% der Zutaten genannt"
    LEVEL_1: "50-80% der Zutaten genannt"
    LEVEL_2: "Mehr als 80% der Zutaten genannt, alle Hauptzutaten vorhanden"
    ANKERBEISPIEL: "Vollständig: Fisch, Kartoffeln, Spinat, Beeren, Grieß, Sahne, Möhren, Croutons"

  - KRITERIUM_ID: "C3_Einheiten"
    KRITERIUM: "Korrekte und einheitliche Einheiten verwendet"
    LEVEL_0: "Einheiten fehlen oder sind falsch"
    LEVEL_1: "Einheiten teilweise vorhanden, aber inkonsistent"
    LEVEL_2: "Alle Mengen mit korrekten, einheitlichen Einheiten (kg, g, L, Stk)"
    ANKERBEISPIEL: "Korrekt: 20kg Kartoffeln, 10L Sahne, 500g Butter"

  - KRITERIUM_ID: "C4_Quelle_Moehrensuppe"
    KRITERIUM: "Quelle für Möhrensuppe-Rezept angegeben"
    LEVEL_0: "Keine Quelle angegeben"
    LEVEL_1: "Quelle genannt, aber unspezifisch (z.B. 'Internet')"
    LEVEL_2: "Konkrete Quelle genannt (Website, Buch, Bot-Recherche)"
    ANKERBEISPIEL: "Korrekt: 'Rezept recherchiert über SIMcoach' oder 'chefkoch.de'"
```

---

## RB_T2_1: Bestandsabgleich

```yaml
# ============================================
# RUBRIC-BLOCK: RB_T2_1
# ============================================
RUBRIC_ID: "RB_T2_1"
GILT_FUER: "T2_1_BESTAND"
SKALA: "0-2"
HINWEISE_BEWERTUNG: "Kriteriumsbezogen, mit Belegen aus der Schülerantwort. Kurz und konstruktiv."

KRITERIEN:
  - KRITERIUM_ID: "C1_Korrekte_Abzuege"
    KRITERIUM: "Bestand korrekt vom Bedarf abgezogen"
    LEVEL_0: "Abzüge nicht durchgeführt oder komplett falsch"
    LEVEL_1: "Abzüge teilweise korrekt, aber Rechenfehler"
    LEVEL_2: "Alle Abzüge korrekt: Bedarf - Bestand = Bestellung"
    ANKERBEISPIEL: "Bedarf 20kg - Bestand 5kg = Bestellung 15kg"

  - KRITERIUM_ID: "C2_Plausibilitaet"
    KRITERIUM: "Bestellmengen sind plausibel"
    LEVEL_0: "Bestellmengen unplausibel (zu viel/wenig, negative Werte)"
    LEVEL_1: "Größtenteils plausibel, aber einzelne Ausreißer"
    LEVEL_2: "Alle Bestellmengen plausibel und praxisnah"
    ANKERBEISPIEL: "Plausibel: Auf Gebindegrößen gerundet (volle Packungen)"

  - KRITERIUM_ID: "C3_Dokumentation"
    KRITERIUM: "Änderungen nachvollziehbar dokumentiert"
    LEVEL_0: "Keine Erklärung der Änderungen"
    LEVEL_1: "Erklärung vorhanden, aber unvollständig"
    LEVEL_2: "Alle wesentlichen Änderungen erklärt und begründet"
    ANKERBEISPIEL: "Butter nicht bestellt, da 2kg im Bestand ausreichend"
```

---

## RB_T3_1: Angebotsvergleich

```yaml
# ============================================
# RUBRIC-BLOCK: RB_T3_1
# ============================================
RUBRIC_ID: "RB_T3_1"
GILT_FUER: "T3_1_ANGEBOT"
SKALA: "0-2"
HINWEISE_BEWERTUNG: "Kriteriumsbezogen, mit Belegen aus der Schülerantwort. Kurz und konstruktiv."

KRITERIEN:
  - KRITERIUM_ID: "C1_Kriterienanwendung"
    KRITERIUM: "Kriterien systematisch angewendet"
    LEVEL_0: "Keine Kriterien verwendet oder genannt"
    LEVEL_1: "Einige Kriterien genannt, aber nicht systematisch angewendet"
    LEVEL_2: "Mehrere Kriterien systematisch auf alle Angebote angewendet"
    ANKERBEISPIEL: "Kriterien: Preis, Lieferzeit, Qualität, Mindestbestellwert"

  - KRITERIUM_ID: "C2_Nachvollziehbarkeit"
    KRITERIUM: "Entscheidung nachvollziehbar begründet"
    LEVEL_0: "Keine Begründung oder nicht nachvollziehbar"
    LEVEL_1: "Begründung vorhanden, aber lückenhaft"
    LEVEL_2: "Klare, logische Begründung mit Bezug zu Kriterien"
    ANKERBEISPIEL: "Lieferant X gewählt, weil: günstigster Preis + schnelle Lieferung"

  - KRITERIUM_ID: "C3_Wirtschaftlichkeit"
    KRITERIUM: "Wirtschaftliche Aspekte berücksichtigt"
    LEVEL_0: "Wirtschaftlichkeit nicht berücksichtigt"
    LEVEL_1: "Preis genannt, aber nicht vollständig (z.B. ohne Lieferkosten)"
    LEVEL_2: "Vollständige Kostenbetrachtung (Preis, Lieferkosten, Rabatte)"
    ANKERBEISPIEL: "Gesamtkosten inkl. Lieferung und Rabatt berechnet"

  - KRITERIUM_ID: "C4_Qualitaet_Risiko"
    KRITERIUM: "Qualität und Risiken berücksichtigt"
    LEVEL_0: "Qualität/Risiken nicht erwähnt"
    LEVEL_1: "Qualität oder Risiken erwähnt, aber nicht beide"
    LEVEL_2: "Sowohl Qualität als auch Risiken in Entscheidung einbezogen"
    ANKERBEISPIEL: "Qualität durch Bewertungen geprüft, Lieferausfall als Risiko bedacht"
```
