# 🔍 02_analyse — Material-Analyse

Hier speicherst du die **strukturierte Analyse** deines Materials.

## Was gehört hierher?

- `material_analyse.md` — Ausgabe des Material-Analyst-Agents

## Analyse erstellen

### Prompt für Material-Analyst

```markdown
# Auftrag: Material-Analyse

Analysiere das folgende Unterrichtsmaterial und erstelle eine strukturierte Analyse.

## Metadaten
- Fach: {{aus _meta.yaml}}
- Zielgruppe: {{aus _meta.yaml}}
- Dauer: {{aus _meta.yaml}}

## Lernziele
{{aus _meta.yaml}}

## Material
{{Hier das Material einfügen oder Datei-Inhalt}}

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

## Checkliste

- [ ] Material-Analyst ausgeführt
- [ ] Analyse als `material_analyse.md` gespeichert
- [ ] Lücken dokumentiert
- [ ] Bereit für Script-Generierung

## Nächster Schritt

Wenn Analyse vollständig → **Phase 3: Scripts**
