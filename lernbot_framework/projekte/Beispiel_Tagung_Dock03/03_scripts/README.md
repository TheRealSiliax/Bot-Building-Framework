# 📝 03_scripts — Generierte Scripts

Hier speicherst du die **generierten Script-Blöcke**.

## Was gehört hierher?

- `scripts_komplett.md` — Alle Script-Blöcke in einem Dokument

## Script-Typen

| Block-Typ | Beschreibung |
|-----------|--------------|
| META | Dokument-Metadaten |
| PHASE | Ablaufphasen |
| RESOURCE | Material-Referenzen |
| TASK | Aufgaben mit Scaffolds |
| RUBRIC | Bewertungskriterien |
| MODEL | Musterlösungen |
| DEBRIEF | Reflexion & Transfer |

## Scripts generieren

### Prompt für Script-Generator

```markdown
# Auftrag: Script-Generierung

Basierend auf der folgenden Material-Analyse, generiere alle Script-Blöcke.

## Material-Analyse
{{Hier die Analyse aus 02_analyse/material_analyse.md einfügen}}

---

Generiere:
1. META-Block
2. PHASE-Blöcke
3. RESOURCE-Blöcke
4. TASK-Blöcke (mit Scaffolds)
5. RUBRIC-Blöcke
6. MODEL-Blöcke (falls möglich)
7. DEBRIEF-Block

Verwende die Block-Syntax: [BLOCK]...[/BLOCK]
Stelle sicher, dass alle IDs eindeutig und Referenzen gültig sind.
```

## Checkliste

- [ ] Script-Generator ausgeführt
- [ ] Scripts als `scripts_komplett.md` gespeichert
- [ ] Alle Block-Typen vorhanden
- [ ] IDs eindeutig und Referenzen gültig
- [ ] Keine unerwünschten Platzhalter

## Nächster Schritt

Wenn Scripts vollständig → **Phase 4: System-Prompt**
