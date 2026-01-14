# ✅ 05_quality — Quality-Check

Hier speicherst du die **Validierungsergebnisse**.

## Was gehört hierher?

- `quality_report.md` — Quality-Check Report

## Quality-Check durchführen

### Prompt für Quality-Checker

```markdown
# Auftrag: Quality-Check

Prüfe den folgenden System-Prompt auf Qualität und Konsistenz.

## System-Prompt
{{Hier den System-Prompt aus 04_system_prompt/system_prompt.md einfügen}}

---

Prüfe:
1. Strukturelle Konsistenz (IDs, Referenzen, Block-Syntax)
2. Didaktische Qualität (Lernziele, Scaffolds, Feedback)
3. Inhaltliche Korrektheit (Fakten, Musterlösungen)
4. Technische Qualität (Formatierung, Token-Limit)

Erstelle einen Quality-Report mit Freigabe-Empfehlung.
```

## Freigabe-Stufen

| Status | Bedeutung | Aktion |
|--------|-----------|--------|
| ✅ FREIGEGEBEN | Keine kritischen Fehler | → Phase 6: Export |
| ⚠️ ÜBERARBEITUNG | Behebbare Fehler | → Zurück zu Phase 3 oder 4 |
| ❌ ABGELEHNT | Fundamentale Probleme | → Zurück zu Phase 1 oder 2 |

## Checkliste

- [ ] Quality-Checker ausgeführt
- [ ] Report als `quality_report.md` gespeichert
- [ ] Freigabe-Status: {{STATUS}}
- [ ] Alle kritischen Fehler behoben

## Nächster Schritt

Wenn **FREIGEGEBEN** → **Phase 6: Export**
