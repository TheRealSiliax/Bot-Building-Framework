# 🚀 06_export — Export & Deployment

Hier speicherst du die **finalen, einsatzbereiten Versionen**.

## Was gehört hierher?

- `FINAL_system_prompt.txt` — Bereinigte Version für den Einsatz
- `FINAL_system_prompt_minimal.txt` — Kompakte Version (falls nötig)

## Export erstellen

### Schritt 1: Kopieren
Kopiere den System-Prompt aus `04_system_prompt/system_prompt.md`.

### Schritt 2: Bereinigen
- Entferne Markdown-Formatierungen (falls für Zielplattform nötig)
- Prüfe Encoding (UTF-8)
- Teste Länge (Token-Limit der Zielplattform)

### Schritt 3: Testen
1. In LLM-Plattform einfügen
2. Testdialog durchführen
3. Feedback dokumentieren

## Einsatz-Checkliste

- [ ] System-Prompt in Zielplattform eingefügt
- [ ] Testdialog mit Beispiel-Antworten durchgeführt
- [ ] Feedback funktioniert wie erwartet
- [ ] Scaffolds werden korrekt angeboten
- [ ] Debriefing funktioniert

## Deployment-Notizen

| Plattform | Status | Notizen |
|-----------|--------|---------|
| {{Plattform 1}} | ⬜ Nicht getestet | - |
| {{Plattform 2}} | ⬜ Nicht getestet | - |

## Projekt abschließen

Wenn alles funktioniert:
1. Projekt-README aktualisieren (Status: ✅ Fertig)
2. Änderungen committen
3. Bot produktiv einsetzen 🎉
