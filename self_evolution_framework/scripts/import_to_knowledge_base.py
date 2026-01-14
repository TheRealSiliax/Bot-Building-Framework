#!/usr/bin/env python3
"""
Import Tool für die Knowledge Base des Self-Evolution Frameworks.

Importiert PDFs, Textdateien und andere Dokumente in die Knowledge Base
und macht sie für die Agenten zugänglich.

Verwendung:
    python import_to_knowledge_base.py --source "path/to/file.pdf" --category personal
    python import_to_knowledge_base.py --source "path/to/file.txt" --category research
    python import_to_knowledge_base.py --source "path/to/folder" --category imported --batch
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path


def extract_pdf_text(pdf_path: str) -> str:
    """Extrahiert Text aus einer PDF-Datei."""
    try:
        from pdfminer.high_level import extract_text
        return extract_text(pdf_path)
    except ImportError:
        print("⚠️  pdfminer.six nicht installiert. Installiere mit: pip install pdfminer.six")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Fehler bei PDF-Extraktion: {e}")
        return ""


def read_text_file(file_path: str) -> str:
    """Liest eine Textdatei."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Fehler beim Lesen der Datei: {e}")
        return ""


def create_metadata_header(source_file: str, category: str, tags: list = None) -> str:
    """Erstellt einen YAML-Metadaten-Header."""
    today = datetime.now().strftime("%Y-%m-%d")
    tags_str = str(tags) if tags else "[]"
    
    return f"""---
date: {today}
type: imported
source: {source_file}
category: {category}
tags: {tags_str}
status: active
---

"""


def get_output_path(knowledge_base_path: str, category: str, original_filename: str) -> str:
    """Generiert den Ausgabepfad basierend auf Kategorie."""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Bereinige den Dateinamen
    base_name = Path(original_filename).stem
    safe_name = "".join(c if c.isalnum() or c in ['-', '_'] else '_' for c in base_name)
    
    # Bestimme den Zielordner
    category_paths = {
        'personal': 'personal/imported',
        'research': 'research',
        'patterns': 'patterns',
        'goals': 'goals',
        'notes': 'personal/notes',
        'journals': 'personal/journals',
    }
    
    sub_path = category_paths.get(category, 'personal/imported')
    output_dir = os.path.join(knowledge_base_path, sub_path)
    
    # Erstelle Verzeichnis falls nicht vorhanden
    os.makedirs(output_dir, exist_ok=True)
    
    output_filename = f"{today}_{safe_name}.md"
    return os.path.join(output_dir, output_filename)


def import_file(source_path: str, knowledge_base_path: str, category: str, tags: list = None) -> bool:
    """Importiert eine einzelne Datei in die Knowledge Base."""
    
    if not os.path.exists(source_path):
        print(f"❌ Datei nicht gefunden: {source_path}")
        return False
    
    # Bestimme Dateityp und extrahiere Text
    file_ext = Path(source_path).suffix.lower()
    
    if file_ext == '.pdf':
        print(f"📄 Extrahiere PDF: {source_path}")
        content = extract_pdf_text(source_path)
    elif file_ext in ['.txt', '.md', '.text']:
        print(f"📝 Lese Textdatei: {source_path}")
        content = read_text_file(source_path)
    else:
        print(f"⚠️  Unbekannter Dateityp: {file_ext}. Versuche als Text zu lesen...")
        content = read_text_file(source_path)
    
    if not content:
        print(f"❌ Keine Inhalte extrahiert aus: {source_path}")
        return False
    
    # Erstelle Ausgabedatei
    output_path = get_output_path(knowledge_base_path, category, os.path.basename(source_path))
    
    # Füge Metadaten-Header hinzu
    header = create_metadata_header(source_path, category, tags)
    
    # Schreibe Datei
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(header)
            f.write(f"# Importiert: {os.path.basename(source_path)}\n\n")
            f.write(content)
        
        print(f"✅ Erfolgreich importiert nach: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Fehler beim Schreiben: {e}")
        return False


def import_folder(folder_path: str, knowledge_base_path: str, category: str, tags: list = None) -> int:
    """Importiert alle unterstützten Dateien aus einem Ordner."""
    
    if not os.path.isdir(folder_path):
        print(f"❌ Verzeichnis nicht gefunden: {folder_path}")
        return 0
    
    supported_extensions = {'.pdf', '.txt', '.md', '.text'}
    imported_count = 0
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            ext = Path(filename).suffix.lower()
            if ext in supported_extensions:
                if import_file(file_path, knowledge_base_path, category, tags):
                    imported_count += 1
    
    return imported_count


def main():
    parser = argparse.ArgumentParser(
        description='Importiert Dokumente in die Self-Evolution Knowledge Base'
    )
    parser.add_argument(
        '--source', '-s',
        required=True,
        help='Pfad zur Quelldatei oder zum Quellordner'
    )
    parser.add_argument(
        '--category', '-c',
        choices=['personal', 'research', 'patterns', 'goals', 'notes', 'journals'],
        default='personal',
        help='Zielkategorie in der Knowledge Base (default: personal)'
    )
    parser.add_argument(
        '--tags', '-t',
        nargs='+',
        help='Tags für die importierte Datei (z.B. --tags stress arbeit)'
    )
    parser.add_argument(
        '--batch', '-b',
        action='store_true',
        help='Importiere alle Dateien aus einem Ordner'
    )
    parser.add_argument(
        '--knowledge-base', '-kb',
        default=None,
        help='Pfad zur Knowledge Base (default: auto-detect)'
    )
    
    args = parser.parse_args()
    
    # Bestimme Knowledge Base Pfad
    if args.knowledge_base:
        kb_path = args.knowledge_base
    else:
        # Auto-detect: Suche knowledge_base relativ zum Script
        script_dir = Path(__file__).parent
        kb_path = script_dir.parent / 'knowledge_base'
        
        if not kb_path.exists():
            # Fallback: Im aktuellen Verzeichnis suchen
            kb_path = Path('self_evolution_framework/knowledge_base')
    
    kb_path = str(kb_path)
    
    if not os.path.exists(kb_path):
        print(f"❌ Knowledge Base nicht gefunden: {kb_path}")
        print("   Bitte --knowledge-base Pfad angeben oder aus dem Framework-Verzeichnis ausführen.")
        sys.exit(1)
    
    print(f"📚 Knowledge Base: {kb_path}")
    print(f"📁 Kategorie: {args.category}")
    print(f"🏷️  Tags: {args.tags or 'keine'}")
    print("-" * 50)
    
    if args.batch:
        count = import_folder(args.source, kb_path, args.category, args.tags)
        print("-" * 50)
        print(f"📊 {count} Datei(en) importiert")
    else:
        success = import_file(args.source, kb_path, args.category, args.tags)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
