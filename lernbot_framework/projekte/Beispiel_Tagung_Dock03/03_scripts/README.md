# 03_scripts - Generierte Script-Blöcke

**Projekt:** Tagung im Hotel Dock 03
**Generiert:** 2026-01-14
**Status:** ✅ Vollständig

---

## Inhalt

| Datei | Beschreibung | Status |
|-------|--------------|--------|
| `meta_block.md` | Bot-Konfiguration und Metadaten | ✅ |
| `phase_blocks.md` | 5 Phasen (P0-P4) | ✅ |
| `task_blocks.md` | 4 Aufgaben (T0-T3) | ✅ |
| `rubric_blocks.md` | 4 Bewertungsrubriken | ✅ |
| `debrief_block.md` | Debriefing-Struktur | ✅ |

---

## Übersicht der Blöcke

### Phasen

| ID | Name | Tasks |
|----|------|-------|
| P0_BRIEF | Briefing / Startlayout | T0_1 |
| P1_BEDARF | Bedarf ermitteln | T1_1 |
| P2_BESTAND | Bestand abgleichen | T2_1 |
| P3_ANGEBOT | Angebote vergleichen | T3_1 |
| P4_DEBRIEF | Debriefing | - |

### Aufgaben

| ID | Name | Rubrik |
|----|------|--------|
| T0_1_AUFTRAGSKLAERUNG | Auftragsklärung | RB_T0_1 |
| T1_1_BEDARF | Warenanforderung | RB_T1_1 |
| T2_1_BESTAND | Bestandsabgleich | RB_T2_1 |
| T3_1_ANGEBOT | Angebotsvergleich | RB_T3_1 |

---

## Besonderheiten

### Recherche-Funktion

Der Bot hat Internetzugang und kann:
- Rezepte recherchieren (z.B. Möhrensuppe)
- Lieferanten im Raum Hamburg suchen

Entsprechende Hinweise sind in den Tasks eingebaut.

### Feedback-Timing

- **Erst-Ausgabe:** Lernziele → Aufgabe → Eingabeaufforderung
- **Nach 1. Versuch:** Hints, Scaffolds, Rubrik-Feedback

---

## Nächster Schritt

→ **Prompt-Builder** starten: System-Prompt aus diesen Scripts assemblieren

```
projekte/Beispiel_Tagung_Dock03/04_system_prompt/
```
