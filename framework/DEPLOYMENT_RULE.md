# Deployment-Regel: Cursor → GitHub

## Übersicht

Diese Regel ermöglicht es, mit einem einfachen Befehl an den Operator (AI-Assistenten) das gesamte Projekt automatisch zu GitHub zu deployen.

## Verwendung

### Automatisches Deployment (empfohlen)

Sage einfach dem Operator in Cursor einen der folgenden Befehle:

- **"Sicherung machen"**
- **"Backup erstellen"**
- **"in GitHub sichern"**
- **"zu GitHub hochladen"**
- **"GitHub Backup"**
- **"Deploy zu GitHub"**
- **"Projekt sichern"**

Der Orchestrator erkennt diese Anfragen automatisch und führt das Backup aus.

### Was passiert automatisch?

1. **Git-Status prüfen**: Prüft, ob es Änderungen gibt
2. **Änderungen stagen**: Staged alle Änderungen (respektiert `.gitignore`)
3. **Commit erstellen**: Erstellt einen Commit mit Timestamp
4. **Zu GitHub pushen**: Pusht automatisch zu `git@github.com:TheRealSiliax/Website_v.0.1.git`

### Manuelles Deployment

Falls du das Backup manuell ausführen möchtest:

```bash
python scripts/github_backup.py
```

## Voraussetzungen

### 1. SSH-Authentifizierung

Das Repository verwendet SSH für die Authentifizierung. Stelle sicher, dass:

- **SSH-Key vorhanden ist**: Prüfe mit `ls ~/.ssh/id_rsa.pub` oder `ls ~/.ssh/id_ed25519.pub`
- **SSH-Key zu GitHub hinzugefügt**: Falls nicht, folge dieser Anleitung:
  1. Öffne deinen öffentlichen SSH-Key: `cat ~/.ssh/id_rsa.pub` (oder `id_ed25519.pub`)
  2. Kopiere den gesamten Inhalt
  3. Gehe zu GitHub → Settings → SSH and GPG keys → New SSH key
  4. Füge den Key hinzu

### 2. Abhängigkeiten installiert

```bash
pip install -r requirements.txt
```

### 3. Konfiguration

Die Konfiguration befindet sich in `.github_config.yaml`:
- Repository-URL: `git@github.com:TheRealSiliax/Website_v.0.1.git` (SSH)
- Git-Benutzer: TheRealSiliax
- E-Mail: namyslo.termine@gmail.com

## Fehlerbehebung

### SSH-Authentifizierung fehlgeschlagen

**Problem**: `Permission denied (publickey)`

**Lösung**:
1. Prüfe, ob SSH-Key vorhanden: `ls ~/.ssh/`
2. Teste SSH-Verbindung: `ssh -T git@github.com`
3. Falls kein Key vorhanden, erstelle einen:
   ```bash
   ssh-keygen -t ed25519 -C "namyslo.termine@gmail.com"
   ```
4. Füge den Key zu GitHub hinzu (siehe Voraussetzungen)

### Git nicht initialisiert

**Problem**: `fatal: not a git repository`

**Lösung**: Das Script initialisiert Git automatisch beim ersten Lauf.

### Keine Änderungen

**Problem**: "Keine Änderungen zum Committen vorhanden"

**Lösung**: Das ist normal, wenn alle Änderungen bereits committed sind.

## Sicherheit

- **Sensible Daten werden geschützt**: `.gitignore` verhindert das Committen von:
  - API-Keys, Tokens, Passwörtern
  - `.env` Dateien
  - Private Keys
- **SSH-Authentifizierung**: Sicherer als HTTPS mit Passwort
- **Keine Credentials im Code**: Alle Authentifizierung über SSH-Keys

## Technische Details

- **Script**: `scripts/github_backup.py`
- **Konfiguration**: `.github_config.yaml`
- **Agent**: `framework/agents/backup.md`
- **Orchestrator**: Erkennt Backup-Anfragen automatisch

## Beispiel-Workflow

1. **Arbeite an deinem Projekt** in Cursor
2. **Sage dem Operator**: "Sicherung machen"
3. **Warte auf Bestätigung**: "✅ Backup erfolgreich abgeschlossen!"
4. **Prüfe auf GitHub**: Änderungen sind jetzt im Repository

---

**Hinweis**: Diese Regel ist vollständig in das Agent-Framework integriert und wird automatisch vom Orchestrator erkannt.

