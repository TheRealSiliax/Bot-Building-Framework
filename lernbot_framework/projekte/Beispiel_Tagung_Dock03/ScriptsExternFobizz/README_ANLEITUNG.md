# 📋 Anleitung: Export nach Fobizz

## Schritt 1: System-Prompt einfügen

1. Öffne die Datei `SYSTEM_PROMPT_FOBIZZ.md`
2. Kopiere den **gesamten Inhalt** (ab der Zeile mit den drei Strichen `---`)
3. Füge ihn in das System-Prompt-Feld auf Fobizz ein

---

## Schritt 2: Dateien anhängen (max. 5)

### Empfohlene Dateien:

| Nr. | Datei | Beschreibung | Pfad |
|-----|-------|--------------|------|
| **1** | 📄 **Aufgabenblatt (PDF)** | Original-Unterrichtsmaterial | `01_material/Vorlage, Aufgabenmaterial und -stoff_ Finaler Teil 1_ Tagung-im-Hotel-Dock-03-Material-1-bis-3c.docx.pdf` |
| **2** | 📄 **Musterlösung** | Beispiellösungen für Lehrkraft-Modus | `01_material/Musterlösung Aufgabe 1 Tagung_003.docx` |
| **3** | 📄 **Rezepte** | Pannfisch & Rote Grütze Rezepte | `ScriptsExternFobizz/Rezepte_3Gang_Menu.md` |
| **4** | 📄 **Rubrics** | Bewertungskriterien | `ScriptsExternFobizz/Bewertungskriterien_Rubrics.md` |
| **5** | *(optional)* | Bestandsliste, falls vorhanden | - |

---

## Checkliste vor dem Start

- [ ] System-Prompt eingefügt
- [ ] Aufgabenblatt (PDF) angehängt
- [ ] Musterlösung angehängt
- [ ] Rezepte-Datei angehängt
- [ ] Rubrics-Datei angehängt
- [ ] Internetrecherche für den Bot aktiviert (falls verfügbar)

---

## Wichtige Hinweise

### 🔍 Internetrecherche
Der Bot soll in der Lage sein, zu recherchieren:
- **Möhrensuppe-Rezept** (für Aufgabe 2)
- **Großhändler in Hamburg** (für Aufgabe 4)

Falls Fobizz keine Internetrecherche unterstützt, können Schüler*innen selbst recherchieren und die Ergebnisse eingeben.

### 📝 Ablauf
1. Bot startet mit Aufgabe 1 (Ziel- und Auftragsklärung)
2. Nach jeder Aufgabe gibt der Bot Feedback
3. Rezepte werden erst in Aufgabe 2 freigegeben
4. Am Ende: Reflexion (Debriefing)

### ⚠️ Keine Sofortlösungen
Der Bot ist so konfiguriert, dass er Musterlösungen nur nach echtem Versuch zeigt.

---

## Dateistruktur im Export-Ordner

```
ScriptsExternFobizz/
├── README_ANLEITUNG.md      ← Diese Datei (nicht hochladen)
├── SYSTEM_PROMPT_FOBIZZ.md  ← System-Prompt für Fobizz
├── Rezepte_3Gang_Menu.md    ← Datei 3: Anhängen!
└── Bewertungskriterien_Rubrics.md ← Datei 4: Anhängen!
```

---

## Support

Bei Fragen oder Problemen:
- Prüfe, ob alle 4-5 Dateien korrekt angehängt sind
- Teste mit einer einfachen Eingabe wie "Hallo" oder "Los geht's"
- Der Bot sollte mit der Handlungssituation (Aufgabe 1) starten
