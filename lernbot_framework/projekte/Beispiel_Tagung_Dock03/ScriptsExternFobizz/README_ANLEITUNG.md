# 📋 Anleitung: Export nach Fobizz

## Schritt 1: System-Prompt einfügen

1. Öffne die Datei `SYSTEM_PROMPT_FOBIZZ.md` (oder `.pdf`)
2. Kopiere den **gesamten Inhalt** (ab der Zeile mit den drei Strichen `---`)
3. Füge ihn in das System-Prompt-Feld auf Fobizz ein

---

## Schritt 2: Dateien anhängen (max. 5)

### PDF-Dateien zum Anhängen:

| Nr. | Datei | Beschreibung |
|-----|-------|--------------|
| **1** | 📄 **Aufgabenblatt (PDF)** | Original-Unterrichtsmaterial |
| **2** | 📄 **Musterloesungen_Komplett.pdf** | Alle Musterlösungen, Toleranzen und Kriterien |
| **3** | 📄 **Rezepte_3Gang_Menu.pdf** | Pannfisch & Rote Grütze Rezepte |
| **4** | 📄 **Bewertungskriterien_Rubrics.pdf** | Bewertungskriterien/Rubrics |

---

## Aufgaben-Übersicht (6 Aufgaben + Reflexion)

| Nr. | Aufgabe | Beschreibung |
|-----|---------|--------------|
| **1** | Ziel- und Auftragsklärung | Was ist zu tun? Planung erstellen |
| **2** | Warenanforderung | Mengen berechnen für 50 Personen |
| **3** | Bestand abgleichen | Bestellung bereinigen |
| **4** | Geschäftliche Anfrage | Brief an Frischfisch Jürgens |
| **5** | Angebot prüfen | Fehler im Angebot finden |
| **6** | Lieferantenauswahl | Vergleichen und entscheiden |
| ✓ | Reflexion | Debriefing & Transfer |

---

## Checkliste vor dem Start

- [ ] System-Prompt eingefügt
- [ ] Aufgabenblatt (PDF) angehängt
- [ ] Musterloesungen_Komplett.pdf angehängt
- [ ] Rezepte_3Gang_Menu.pdf angehängt
- [ ] Bewertungskriterien_Rubrics.pdf angehängt
- [ ] Internetrecherche aktiviert (falls verfügbar)

---

## Wichtige Hinweise

### 🔄 Zwei-Phasen-Logik

**Phase 0 (Erstausgabe):**
- Nur Aufgabe + Eingabeaufforderung
- KEINE Hilfen/Scaffolds
- KEINE Feedback-Hinweise

**Nach erster Eingabe:**
- Feedback geben
- Scaffolds/Hilfen zeigen
- Zur Überarbeitung auffordern
- Nach Korrektur → Nächste Aufgabe

### 🔍 Internetrecherche
Der Bot kann recherchieren:
- **Möhrensuppe-Rezept** (Aufgabe 2)
- **Großhändler in Hamburg** (Aufgabe 6)

### ⚠️ Keine Sofortlösungen
Musterlösungen werden nur nach echtem Versuch gezeigt!

---

## Dateistruktur im Export-Ordner

```
ScriptsExternFobizz/
├── README_ANLEITUNG.md           ← Diese Datei (NICHT hochladen)
├── SYSTEM_PROMPT_FOBIZZ.md       ← System-Prompt (Text kopieren)
├── SYSTEM_PROMPT_FOBIZZ.pdf      ← System-Prompt (PDF-Version)
├── Musterloesungen_Komplett.md   ← Musterlösungen (MD)
├── Musterloesungen_Komplett.pdf  ← Datei 2: ANHÄNGEN!
├── Rezepte_3Gang_Menu.md         ← Rezepte (MD)
├── Rezepte_3Gang_Menu.pdf        ← Datei 3: ANHÄNGEN!
├── Bewertungskriterien_Rubrics.md ← Rubrics (MD)
└── Bewertungskriterien_Rubrics.pdf ← Datei 4: ANHÄNGEN!
```

---

## Support

Bei Fragen oder Problemen:
- Prüfe, ob alle 4-5 PDFs korrekt angehängt sind
- Teste mit einer einfachen Eingabe wie "Hallo" oder "Los geht's"
- Der Bot sollte mit der Handlungssituation (Aufgabe 1) starten
- Hilfen erscheinen erst NACH der ersten Antwort
