# 🎯 04_system_prompt — Finaler System-Prompt

Hier speicherst du den **assemblierten System-Prompt**.

## Was gehört hierher?

- `system_prompt.md` — Der vollständige, einsatzbereite System-Prompt

## System-Prompt bauen

### Prompt für Prompt-Builder

```markdown
# Auftrag: System-Prompt Assembly

Kombiniere die folgenden Scripts zu einem finalen System-Prompt.

## Bot-Konfiguration
- Name: {{aus _meta.yaml}}
- Tonalität: {{aus _meta.yaml}}
- Sprachniveau: {{aus _meta.yaml}}

## Generierte Scripts
{{Hier die Scripts aus 03_scripts/scripts_komplett.md einfügen}}

---

Erstelle den finalen System-Prompt nach der Vorlage in:
`lernbot_framework/templates/scripts/system_prompt_base.md`

Der Output soll direkt kopierbar sein.
```

## Checkliste

- [ ] Prompt-Builder ausgeführt
- [ ] Prompt als `system_prompt.md` gespeichert
- [ ] Keine `{{PLATZHALTER}}` mehr vorhanden
- [ ] Alle Scripts integriert
- [ ] Bereit für Quality-Check

## Nächster Schritt

Wenn Prompt vollständig → **Phase 5: Quality**
